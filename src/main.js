const vscode = require('vscode')
const path = require('path')
const clone = require('git-clone');
const extension = require('./extension')
const ui = require('./ui')


const EXAMPLES_REPO = "https://github.com/makinteract/micropython-examples";



// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {


  // globals
  const output = vscode.window.createOutputChannel("micro:bit");

  /**
   * 
   * @returns - path of extension root
   */
  function extensionRootPath() {
    return vscode.extensions.getExtension("MAKinteract.micro-bit-python").extensionPath;
  }

  function extensionUri() {
    return vscode.extensions.getExtension("MAKinteract.micro-bit-python").extensionUri;
  }


  /**
   * 
   * @returns - path of tools
   */
  function toolsPath() {
    const extRoot = extensionRootPath();
    return path.join(extRoot, "tools");
  }

  /**
   * 
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
   * 
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
      ui.vsError("Can't find main.py");
      outError("Can't find main.py");
      return
    }

    // flash files
    try {
      // Flash them one by one
      for (let { path } of workspaceFiles) {
        // it might throw an error
        await ufs(`put ${path}`);
      }
      const fileNames = files.join('\n');
      ui.vsInfo("Files successfully uploaded");
      outInfo(`Files copied on micro:bit:\n${fileNames}`);
    } catch (e) {
      ui.vsError("Could not upload files to micro:bit");
      outError(e);
    }
  }

  async function getFilesOnMicrobit() {
    const { stdout: filenames, stderr: err } = await ufs("ls");

    if (err) {
      outError(err);
      return;
    }

    const files = filenames.split(" ").filter(name => name.length > 0);
    return files;
  }

  async function getFileSelectionFromUser(filesAvailable) {
    const fileToRemove = await ui.showQuickPick(filesAvailable, '')

    if (!fileToRemove) throw new Error("No file selected");
    return [fileToRemove];
  }

  async function removeFilesFromMicrobit(removeAll = false) {
    try {
      const files = await getFilesOnMicrobit();
      let filesToRemove = files;

      // ask user to select which file to remove
      if (!removeAll) filesToRemove = await getFileSelectionFromUser(files);
      if (!filesToRemove || filesToRemove.length == 0) {
        ui.vsError("No files to remove");
        outInfo("No files on micro:bit or no input specified");
        return;
      }

      // remove the files
      for (let file of filesToRemove) {
        await ufs(`rm ${file}`);
      }
      const names = filesToRemove.join(', ');
      ui.vsInfo("Files successfully removed");
      outInfo(`Files ${names} removed from micro:bit`);

    } catch (e) {
      outError(e)
    }
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

  const flashMicropython = vscode.commands.registerCommand('extension.flash-micropython', async function () {
    try {
      await uFlash();
      ui.vsInfo("MicroPython successfully installed");
      outInfo("MicroPython successfully installed");
    } catch (e) {
      ui.vsError("Error: check console for info");
      outError(e);
    }
  });

  const rmFile = vscode.commands.registerCommand('extension.rmFile', async function () {
    await removeFilesFromMicrobit()
  });

  const rmAll = vscode.commands.registerCommand('extension.rmAll', async function () {
    await removeFilesFromMicrobit(true)
  });

  const flash = vscode.commands.registerCommand('extension.flash', async function () {
    await flashFilesToMicrobit();
  });

  const fetchExamples = vscode.commands.registerCommand('extension.fetch-examples', async function () {


    vscode.workspace.fs.delete(Uri.joinPath(extensionUri(), "examples");
    const root = extensionRootPath();
    clone(EXAMPLES_REPO, path.join(root, "examples"));
  });





  // Init microbit
  let initCmd = vscode.commands.registerCommand('extension.init-sketch', async function () {


    // const extRoot = context.asAbsolutePath('.');

    // const ws = getCurrentWorkspace()
    // console.log(ws.name);
    // const res = await ui.showQuickPick(['a', 'b', 'c'], "Choose a file")
    // console.log(res);
    // const res2 = await ui.showInputBox("a", "b", (text) => "File does not exist")
    // console.log(res2);


    // copyFileFromExtensionToWorkspace("main_template.py", "main.py");

    // const microbitFolder = await isInWorkspace('microbit/**'); // a folder called microbit with files inside
    // if (!microbitFolder){
    //   clone("https://github.com/makinteract/microbit.git", path.join(workspace.uri.path, "microbit"))
    // }
  });


  // Setup MicroPython


  context.subscriptions.push(rmAll);
  context.subscriptions.push(rmFile);
  context.subscriptions.push(flash);
  context.subscriptions.push(flashMicropython);
  context.subscriptions.push(fetchExamples);
}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
  activate,
  deactivate
}
