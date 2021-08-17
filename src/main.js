const vscode = require('vscode')
const path = require('path')
const clone = require('git-clone');
const extension = require('./extension')
const ui = require('./ui');
const { readdirSync, stat } = require('fs');
const {EXAMPLES_REPO, MICROBIT_LIBS, EXTENSION_ID} = require ('./constants');


/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {


  // globals
  const output = vscode.window.createOutputChannel("micro:bit");

  /**
   * Get path where extension is stored in teh filesystem
   * @returns - path of extension root folder
   */
  function extensionRootPath() {
    return vscode.extensions.getExtension("MAKinteract.micro-bit-python").extensionPath;
  }

  /**
   * Get URI of extension folder
   * @returns - URI of extension folder
   */
  function extensionUri() {
    return vscode.extensions.getExtension("MAKinteract.micro-bit-python").extensionUri;
  }

  /**
   * Get the path of the tools folder
   * @returns - path of tools folder
   */
  function toolsPath() {
    const extRoot = extensionRootPath();
    return path.join(extRoot, "tools");
  }

  /**
   * Get the path of the examples folder 
   * @returns - path of examples folder
   */
    function toolsPath() {
      const extRoot = extensionRootPath();
      return path.join(extRoot, "examples");
  }

  /**
   * Run the uflash python script
   * @param {String} params - string with parameters passed to "python uflash.py"
   * @returns - stdout and sterr from python command
   */
  async function uFlash(params = "") {
    const tools = toolsPath();
    const uflash = path.join(tools, "uflash-master", "uflash.py");
    const { stdout, stderr } = await extension.runWithPython(`${uflash} ${params}`)
    return { stdout, stderr };
  }

  /**
   * Run the ufs python script
   * @param {String} params - string with parameters pased to "pyton ufs.py"
   * @returns - stdout and sterr from python command
   */
  async function ufs(params = "") {
    const tools = toolsPath();
    const ufs = path.join(tools, "microfs-master", "ufs.py");
    const { stdout, stderr } = await extension.runWithPython(`${ufs} ${params}`);
    return { stdout, stderr };
  }


  function outInfo(msg) {
    const date = `[${new Date()}]`;
    output.appendLine(`SUCCESS ${date}\n${msg}\n`);
  }

  function outError(msg) {
    const date = `[${new Date()}]`;
    output.appendLine(`ERROR ${date}\n${msg}\n`);
  }

  function pathToName(filepath) {
    const filename = path.parse(filepath).base;
    return filename;
  }




  /**
   * Copy all files in workspace on micro:bit. Throws an error if something goes wrong
   */
  async function flashFilesToMicrobit() {

    // get all the [python] files in the workspace and copy them to the microbit
    const workspaceFiles = await extension.getFilesInCurrentWorkspace();

    // is main.py included?
    const files = workspaceFiles.map(({ path }) => pathToName(path));
    if (!files.includes("main.py")) {
      throw new Error("Can't find main.py");
    }

    // Flash files one by one
    for (let { path } of workspaceFiles) {
      // it might throw an error
      await ufs(`put ${path}`);
    }
    const fileNames = files.join('\n');
    ui.vsInfo("Files successfully uploaded");
    outInfo(`Files copied on micro:bit:\n${fileNames}`);
  }


  async function getFilesOnMicrobit() {
    const { stdout: filenames, stderr: err } = await ufs("ls");

    if (filenames.includes("Could not find micro:bit")) {
      throw new Error("Could not find micro:bit");
    }
    if (err) {
      throw new Error(err)
    }

    const files = filenames.split(" ").filter(name => name.length > 0);
    return files;
  }

  async function getFileSelectionFromUser(filesAvailable) {
    const fileToRemove = await ui.showQuickPick(filesAvailable, '')

    if (!fileToRemove) throw new Error("No input specified");
    return [fileToRemove];
  }

  async function removeFilesFromMicrobit(removeAll = false) {

    // may throw an exception
    let filesToRemove = await getFilesOnMicrobit();
    // Check whether these files are valid (non-empty list)
    if (!filesToRemove || filesToRemove.length == 0) {
      throw new Error("No files on micro:bit");
    }

    if (!removeAll) filesToRemove = await getFileSelectionFromUser(filesToRemove);

    // remove the files
    for (let file of filesToRemove) {
      await ufs(`rm ${file}`);
    }
    const names = filesToRemove.join(', ');
    ui.vsInfo("Files successfully removed");
    outInfo(`Files ${names} removed from micro:bit`);
  }

  async function initWorkspace() {
    let workspace = await extension.getCurrentWorkspace();

    if (!workspace) {
      // select a workspace
      workspace = await vscode.commands.executeCommand("vscode.openFolder");
      // this will refresh VScode
    }

    // clone microbit repo if not already there
    const microbitFolder = await extension.isFileInCurrentWorkspace('microbit/**'); // a folder called microbit with files inside
    if (!microbitFolder) {
      clone(MICROBIT_LIBS, path.join(workspace.uri.path, "microbit"))
    }

    // pick from template
    const example = await getExampleUri();
    if (example) {
      console.log(example);
      //   const src = vscode.Uri.file(path.join(extensionRootPath(), "examples", example));
      //  const dest = vscode.Uri.file(path.join(workspace.uri.path, ));

    }

    // if main not there, alert user
    const main = await extension.isFileInCurrentWorkspace('main.py');
    if (main) ui.vsInfo("Sketch ready");
    else ui.vsInfo("Remember to create a main.py file");
  }

  const getDirectories = source =>
    readdirSync(source, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name)
      .filter(name => !name.startsWith('.'));


  // HERE
  async function getExampleUri() {
    let examplesDir = "";
    try {
      examplesDir = path.join(extensionRootPath(), "examples");
    } catch (e) {
      throw new Error("Fetch the examples first");
    }
    // stat(examplesDir, function (err, stat) {
    //   if (err == null) {
    //   }
    // });

    const list = getDirectories(examplesDir);
    const pick = await ui.showQuickPick(list, 'empty');
    if (pick) {
      const uri = vscode.Uri.joinPath(vscode.Uri.file(examplesDir), pick);
      return uri;
    }
    return undefined;
  }



  // async function copyFileFromExtensionToWorkspace(srcFilename, destFilename, overwrite = false) {
  //   const document = vscode.window.activeTextEditor.document;
  //   const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

  //   const main = await isInWorkspace("main.py");
  //   if (main && !overwrite) return;

  //   const src = vscode.Uri.file(path.join(extRoot, srcFilename));
  //   const dest = vscode.Uri.file(path.join(workspace.uri.path, destFilename));
  //   vscode.workspace.fs.copy(src, dest, { "overwrite": overwrite });
  // }


  // COMMANDS

  const init = vscode.commands.registerCommand('extension.init', async function () {
    try {
      await initWorkspace();
    } catch (e) {
      ui.vsError(`${e}`);
      outError(e);
    }
  });


  const flashMicropython = vscode.commands.registerCommand('extension.flash-micropython', async function () {
    try {
      await uFlash();
      ui.vsInfo("MicroPython successfully installed");
      outInfo("MicroPython successfully installed");
    } catch (e) {
      ui.vsError(`${e}`);
      outError(e);
    }
  });

  const rmFile = vscode.commands.registerCommand('extension.rmFile', async function () {
    try {
      await removeFilesFromMicrobit();
    } catch (e) {
      ui.vsError(`${e}`);
      outError(e);
    }
  });

  const rmAll = vscode.commands.registerCommand('extension.rmAll', async function () {
    try {
      await removeFilesFromMicrobit(true);
    } catch (e) {
      ui.vsError(`${e}`);
      outError(e);
    }
  });

  const flash = vscode.commands.registerCommand('extension.flash', async function () {
    try {
      await flashFilesToMicrobit();
    } catch (e) {
      ui.vsError(`${e}`);
      outError(e);
    }
  });

  const fetchExmls = vscode.commands.registerCommand('extension.fetch-examples', async function () {
    const todelete = vscode.Uri.joinPath(extensionUri(), "examples");

    // delete the existing folder
    try {
      await vscode.workspace.fs.delete(todelete, { recursive: true, useTrash: true });
    } catch (e) {
      console.log(`Folder ${todelete.toString()} not found`);
    }

    // Fetch from github
    const root = extensionRootPath();
    clone(EXAMPLES_REPO, path.join(root, "examples"));
  });







  // Setup MicroPython


  context.subscriptions.push(init);
  context.subscriptions.push(flashMicropython);
  context.subscriptions.push(flash);
  context.subscriptions.push(rmAll);
  context.subscriptions.push(rmFile);
  context.subscriptions.push(fetchExmls);
}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
  activate,
  deactivate
}
