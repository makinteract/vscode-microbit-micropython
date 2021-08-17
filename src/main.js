const vscode = require('vscode')
// const path = require('path')
// const clone = require('git-clone');
const ui = require('./ui');
// const { readdirSync, stat } = require('fs');
// const { EXAMPLES_REPO, MICROBIT_LIBS, EXTENSION_ID } = require('./constants');
const { uflash,
  ufs,
  getCurrentWorkspace,
  getFilesInCurrentWorkspace,
  assertFileIsIncluded } = require('./extension')





/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

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

  // COMMANDS
  /*
    const init = vscode.commands.registerCommand('extension.init', async function () {
      try {
        await initWorkspace();
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
    
    context.subscriptions.push(flash);
    context.subscriptions.push(rmAll);
    context.subscriptions.push(rmFile);
    context.subscriptions.push(fetchExmls);
  
    */

  context.subscriptions.push(flashMicropython);
}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
  activate,
  deactivate
}
