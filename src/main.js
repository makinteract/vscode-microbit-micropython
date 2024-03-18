const vscode = require('vscode');
const ui = require('./ui');
const {
  extensionUri,
  ufs,
  getCurrentWorkspace,
  getFilesInDir,
  getVisibleFoldersInDir,
  assertFileIsIncluded,
  listFilesOnMicrobit,
  removeFilesFromMicrobit,
  getFileFromMicrobit,
  deleteFileFromDir,
  cloneRepository,
  checkFileExist,
  isOnline,
  copyFileOrFolder,
  copyFiles,
  moveLast,
  isGitInstalled,
  pickLibraries,
  uploadFirmware,
} = require('./extension');
const { fstat } = require('fs');

// GLOBALS
const EXAMPLES_REPO = 'https://github.com/makinteract/micropython-examples';

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  const init = vscode.commands.registerCommand(
    'extension.init',
    async function () {
      try {
        // 1. Copy libs in current workspace
        // get workspace
        const workspace = await getCurrentWorkspace();
        // check whether microbit folder is there
        // clone it if not there
        const libs = await checkFileExist('microbit', workspace.uri);
        if (!libs) {
          const basicStubsFolder = vscode.Uri.joinPath(
            extensionUri(),
            'Microbit-Basic-Stubs'
          );
          await copyFileOrFolder('microbit', basicStubsFolder, workspace.uri);
        }

        // 2. Add additional libraries
        await pickLibraries();

        // 3. Show to the user the list of template files in examples and ask to pick one
        const examples = vscode.Uri.joinPath(extensionUri(), 'examples');
        const list = await getVisibleFoldersInDir(examples);
        list.unshift('Empty - do not modify the current directory'); // add an empy project to start
        const pick = await ui.showQuickPick(
          list,
          'Select a template for the project'
        );
        if (!pick || pick.startsWith('Empty')) return; // done

        // 4. If the user selected one template
        // Ask user to confirm overriding of project
        const mainExist = await checkFileExist('main.py', workspace.uri);
        if (mainExist) {
          const ans = await ui.confirmationMessage(
            'Are you sure you want to override your project?',
            ['Yes', 'No']
          );
          if (ans === 'No' || ans === undefined) return; // bye bye
        }

        // copy files
        const src = vscode.Uri.joinPath(examples, pick);
        copyFiles(src, workspace.uri);
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const fetchExamples = vscode.commands.registerCommand(
    'extension.fetch-examples',
    async function () {
      try {
        if (!(await isOnline())) throw new Error('No internet connection.');

        if (!(await isGitInstalled()))
          throw new Error(
            'Git not installed. [Install git](https://git-scm.com) first.'
          );

        // delete if already exists
        const examplesExist = await checkFileExist('examples', extensionUri());
        if (examplesExist) {
          await deleteFileFromDir('examples', extensionUri());
        }
        // clone again examples
        cloneRepository(EXAMPLES_REPO, 'examples', extensionUri());
        ui.vsInfo('Examples successfully downloaded');
        ui.outInfo('Examples successfully downloaded');
      } catch (e) {
        // console.log(`Folder ${todelete.toString()} not found`);
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const flashMicropython = vscode.commands.registerCommand(
    'extension.flash-micropython',
    uploadFirmware
  );

  const flash = vscode.commands.registerCommand(
    'extension.flash',
    async function () {
      try {
        // get all files in the workspace
        const workspace = await getCurrentWorkspace();
        const workspaceFiles = await getFilesInDir(workspace.uri);
        // is main.py inclued?
        assertFileIsIncluded('main.py', workspaceFiles);
        // main.py should be flashed last!
        const wsFiles = moveLast('main.py', workspaceFiles);

        // Flash files one by one
        for (let { fsPath: filename } of wsFiles) {
          // it might throw an error
          const { stdout } = await ufs(`put "${filename}"`);
          ui.outInfo(`File "${filename}" copied on micro:bit`);
          ui.outInfo(`out ${stdout}`);
        }
        await ufs(`reset`);
        ui.vsInfo('Files successfully uploaded');
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const rmAll = vscode.commands.registerCommand(
    'extension.rmAll',
    async function () {
      try {
        const files = await listFilesOnMicrobit();
        await removeFilesFromMicrobit(files);
        ui.outInfo(`Files "${files}" removed from micro:bit`);
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const rmFile = vscode.commands.registerCommand(
    'extension.rmFile',
    async function () {
      try {
        const files = await listFilesOnMicrobit();
        const fileToRemove = await ui.showQuickPick(files, '');

        if (!fileToRemove) throw new Error('No input specified');
        await removeFilesFromMicrobit([fileToRemove]);
        ui.outInfo(`File "${fileToRemove}" removed from micro:bit`);
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const getFile = vscode.commands.registerCommand(
    'extension.getFile',
    async function () {
      try {
        const workspace = await getCurrentWorkspace();
        const files = await listFilesOnMicrobit();
        if (!files || files.length == 0)
          throw new Error('No files found on micro:bit');

        const fileSelected = await ui.showQuickPick(files, '');
        if (!fileSelected) throw new Error('No input specified');

        const fileExist = await checkFileExist(fileSelected, workspace.uri);
        if (fileExist) {
          const ans = await ui.confirmationMessage(
            `Are you sure you want to override ${fileSelected}?`,
            ['Yes', 'No']
          );
          if (ans === 'No' || ans === undefined) return; // bye bye
        }
        // get the file
        getFileFromMicrobit(fileSelected, workspace.uri);
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const listFiles = vscode.commands.registerCommand(
    'extension.listFiles',
    async function () {
      try {
        const files = await listFilesOnMicrobit();
        if (!files || files.length == 0)
          throw new Error('No files found on micro:bit');

        await ui.showQuickPick(files, '');
      } catch (e) {
        ui.vsError(`${e}`);
        ui.outError(e);
      }
    }
  );

  const showPinMap = vscode.commands.registerCommand(
    'extension.showPinMap',
    async function () {
      const panel = vscode.window.createWebviewPanel(
        'pins',
        'micro:bit Pins',
        vscode.ViewColumn.Active,
        {
          // Only allow the webview to access resources in our extension's media directory
          localResourceRoots: [vscode.Uri.joinPath(extensionUri(), 'images')],
        }
      );

      const onDiskPath = vscode.Uri.file(
        vscode.Uri.joinPath(extensionUri(), 'images', 'pinout.png').fsPath
      );
      const imageUrl = panel.webview.asWebviewUri(onDiskPath);

      panel.webview.html = ui.getPinMap(imageUrl);
    }
  );

  // COMMANDS
  context.subscriptions.push(init);
  context.subscriptions.push(fetchExamples);
  context.subscriptions.push(flashMicropython);
  context.subscriptions.push(flash);
  context.subscriptions.push(rmAll);
  context.subscriptions.push(rmFile);
  context.subscriptions.push(getFile);
  context.subscriptions.push(listFiles);
  context.subscriptions.push(showPinMap);
}

// this method is called when your extension is deactivated
function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
