const vscode = require('vscode')
const ui = require('./ui');
const { 
  extensionUri,
  uflash,
  ufs,
  getCurrentWorkspace,
  getFilesInCurrentWorkspace,
  assertFileIsIncluded,
  listFilesOnMicrobit,
  removeFilesFromMicrobit,
  getFileFromMicrobit,
  deleteFileFromDir,
  cloneRepository,
  checkFileExist,
  isOnline
} = require('./extension')


// GLOBALS
const EXAMPLES_REPO = "https://github.com/makinteract/micropython-examples";
const MICROBIT_LIBS_REPO = "https://github.com/makinteract/microbit.git";



// const pipeAsync =  async (...fns) => async (x) => await fns.reduce( async (v, f) => await f(v), x);



/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

  const init = vscode.commands.registerCommand('extension.init', async function () {
    try{
    // get workspace
    const workspace= await getCurrentWorkspace();
    // check whether microbit folder is there
    // clone it if not there
    const libs = await checkFileExist("microbit", workspace.uri);
    if (!libs){
      cloneRepository(MICROBIT_LIBS_REPO, "microbit", workspace.uri);
    }

    // check whether examples are there
    // download them if not
    const examplesExist = await checkFileExist("examples", extensionUri());
    if (!examplesExist && await isOnline()){
      cloneRepository(EXAMPLES_REPO,"examples",extensionUri());
      ui.vsInfo("Downloading examples");
      ui.outInfo("Downloading examples");
    }

    // if examples exist, get list of folder examples
    // show it to the user 
    // copy the files of examples to workspace

  } catch (e) {
    ui.vsError(`${e}`);
    ui.outError(e);
  }
  });


  const flashMicropython = vscode.commands.registerCommand('extension.flash-micropython', async function () {
    try {
      await uflash();
      ui.vsInfo("MicroPython successfully installed");
      ui.outInfo("MicroPython successfully installed");
    } catch (e) {
      ui.vsError(`${e}`);
      ui.outError(e);
    }
  });

  const flash = vscode.commands.registerCommand('extension.flash', async function () {
    try {
      // get all files in the workspace
      const workspaceFiles = await getFilesInCurrentWorkspace();
      // is main.py inclued?
      assertFileIsIncluded("main.py", workspaceFiles);

      // Flash files one by one
      for (let { path: filename } of workspaceFiles) {
        // it might throw an error
        await ufs(`put ${filename}`);
        ui.outInfo(`File ${filename} copied on micro:bit`);
      }
      ui.vsInfo("Files successfully uploaded");

    } catch (e) {
      ui.vsError(`${e}`);
      ui.outError(e);
    }
  });


  const rmAll = vscode.commands.registerCommand('extension.rmAll', async function () {
    try{
      const files = await listFilesOnMicrobit();
      await removeFilesFromMicrobit (files);
    } catch (e) {
      ui.vsError(`${e}`);
      ui.outError(e);
    }
  });


  const rmFile = vscode.commands.registerCommand('extension.rmFile', async function () {
    try {
      const files = await listFilesOnMicrobit();
      const fileToRemove = await ui.showQuickPick(files, '')

      if (!fileToRemove) throw new Error("No input specified");
      await removeFilesFromMicrobit ([fileToRemove]);
    } catch (e) {
      ui.vsError(`${e}`);
      ui.outError(e);
    }
  });


  const getFile = vscode.commands.registerCommand('extension.getFile', async function () {
    try {
      const workspace = await getCurrentWorkspace();
      const files = await listFilesOnMicrobit();
      const fileSelected = await ui.showQuickPick(files, '')
      if (!fileSelected) throw new Error("No input specified");
      
      getFileFromMicrobit(fileSelected, workspace.uri);

    } catch (e) {
      ui.vsError(`${e}`);
      ui.outError(e);
    }
  });


  const fetchExamples = vscode.commands.registerCommand('extension.fetch-examples', async function () {
    try{
    	if (! await isOnline()) 
        throw new Error ("No internet connection.")

        // delete if already exists
      const examplesExist = await checkFileExist("examples", extensionUri());
      if (examplesExist){
        await deleteFileFromDir ("examples", extensionUri());
      }
      // clone again examples
      cloneRepository(EXAMPLES_REPO,"examples",extensionUri());
      ui.vsInfo("Examples successfully downloaded");
      ui.outInfo("Examples successfully downloaded");
    }
     catch (e) {
      // console.log(`Folder ${todelete.toString()} not found`);
      ui.vsError(`${e}`);
      ui.outError(e);    }
  });


  // COMMANDS
   context.subscriptions.push(init);
   context.subscriptions.push(flashMicropython);
   context.subscriptions.push(flash);
   context.subscriptions.push(rmAll);
   context.subscriptions.push(rmFile);
   context.subscriptions.push(getFile);
   context.subscriptions.push(fetchExamples);

}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
  activate,
  deactivate
}
