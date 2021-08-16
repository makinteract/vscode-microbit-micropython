// General utilities for the extension
const vscode = require('vscode');
const path = require('path')
const util = require('util');
const clone = require('git-clone');
const { ListFormat } = require('typescript');
const exec = util.promisify(require('child_process').exec);


// Globals to determine which python version is installed
let python2 = true;
let python3 = true;

/**
 * 
 * @param {String} command - command to run with python
 * @returns 
 */
async function runWithPython(command) {
	// try with python 3
	if (python3) {
		try {
			const { stdout, stderr } = await exec(`python3 ${command}`)
			return { stdout, stderr };
		} catch (e) {
			// python not found
			python3 = false;
		}
	}

	// try with python 2
	if (python2) {
		try {
			const { stdout, stderr } = await exec(`python ${command}`)
			return { stdout, stderr };
		} catch (e) {
			python2 = false;
			throw e;
		}
	}

	// none found
	throw new Error("Could not exectute command");
}


function getWorkspace(openDocument) {
	if (!openDocument) return undefined;
	const workspace = vscode.workspace.getWorkspaceFolder(openDocument.uri);
	return workspace;
}

function getOpenWorkspace() {
	const document = vscode.window.activeTextEditor.document;
	return getWorkspace(document);
}

async function getCurrentWorkspace() {
	const openDocumnet = vscode.window.activeTextEditor?.document;
	if (openDocumnet)
		return getOpenWorkspace();

	// else get all workspaces
	const workspaces = vscode.workspace.workspaceFolders;
	// if there is only one open, return it

	if (workspaces?.length == 1) return workspaces[0];
	// else no workspaces or > 1, therfore ask the user to pick one
	const selection = await vscode.window.showWorkspaceFolderPick()
	return selection;
}


async function isFileInWorkspace(filename, workspace) {
	// get all the python files in the workspace and copy them to the microbit
	const file = await vscode.workspace.findFiles(
		filename
	);
	return file.length > 0;
}

async function isFileInCurrentWorkspace(filename) {
	const workspace = getCurrentWorkspace();

	// get all the python files in the workspace and copy them to the microbit
	const file = await vscode.workspace.findFiles(
		filename
	);
	return file.length > 0;
}

/**
 * 
 * @param {String} pattern - pattern to find files. Default is '*' = all
 * @returns - the files in the workspace
 */
async function getFilesInCurrentWorkspace(pattern = "*") {
	const workspace = await getCurrentWorkspace();

	if (!workspace) return []; // no files

	// get all the [python] files in the workspace and copy them to the microbit
	const workspaceFiles = await vscode.workspace.findFiles(
		new vscode.RelativePattern(workspace, pattern)
	);
	return workspaceFiles;
}



module.exports = {
	runWithPython,
	getWorkspace,
	getOpenWorkspace,
	getCurrentWorkspace,
	getFilesInCurrentWorkspace,
	isFileInCurrentWorkspace,
	isFileInWorkspace
};





// const ui = require('./ui');
// 

// // this method is called when your extension is activated
// // your extension is activated the very first time the command is executed

// /**
//  * @param {vscode.ExtensionContext} context
//  */
// function activate(context) {

// 	const extRoot = vscode.extensions.getExtension("MAKinteract.micro-bit-python").extensionPath;
// 	const uflash = path.join(extRoot, "tools", "uflash-master", "uflash.py")
// 	const ufs = path.join(extRoot, "tools", "microfs-master", "ufs.py")
// 	const output = vscode.window.createOutputChannel("micro:bit");
// 	let python2 = true;
// 	let python3 = true;




// 	async function isInWorkspace(filename) {
// 		const document = vscode.window.activeTextEditor.document;
// 		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

// 		// get all the python files in the workspace and copy them to the microbit
// 		const file = await vscode.workspace.findFiles(
// 			filename
// 		);

// 		return file.length > 0;
// 	}



// 	// copy files
// 	async function copyFilesFromWorkspaceToDevice(srcPattern) {

// 		const document = vscode.window.activeTextEditor.document;
// 		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

// 		// get all the python files in the workspace and copy them to the microbit
// 		const workspaceFiles = await vscode.workspace.findFiles(
// 			new vscode.RelativePattern(workspace, `${srcPattern}`)
// 		);

// 		for (let { path } of workspaceFiles) {
// 			// it might throw an error
// 			await runWithPython(`${ufs} put ${path}`);
// 		}
// 	}


// 	async function copyFileFromExtensionToWorkspace(srcFilename, destFilename, overwrite = false) {
// 		const document = vscode.window.activeTextEditor.document;
// 		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

// 		const main = await isInWorkspace("main.py");
// 		if (main && !overwrite) return;

// 		const src = vscode.Uri.file(path.join(extRoot, srcFilename));
// 		const dest = vscode.Uri.file(path.join(workspace.uri.path, destFilename));
// 		vscode.workspace.fs.copy(src, dest, { "overwrite": overwrite });
// 	}


// 	function getCurrentWorkspace() {

// 		const openDocumnet = vscode.window.activeTextEditor.document;
// 		if (openDocumnet)
// 			return vscode.workspace.getWorkspaceFolder(openDocumnet.uri);

// 		// else
// 		const workspaces = vscode.workspace.workspaceFolders;
// 		if (workspaces.length == 1) return workspaces[0];
// 		else {
// 			const selection = vscode.window.showWorkspaceFolderPick()
// 		}

// 	}


// 	// Init microbit
// 	let initCmd = vscode.commands.registerCommand('extension.init-sketch', async function () {

// 		// const extRoot = context.asAbsolutePath('.');

// 		const ws = getCurrentWorkspace()
// 		console.log(ws.name);
// 		const res = await ui.showQuickPick(['a', 'b', 'c'], "Choose a file")
// 		console.log(res);
// 		const res2 = await ui.showInputBox("a", "b", (text) => "File does not exist")
// 		console.log(res2);
// 		/*copyFileFromExtensionToWorkspace("main_template.py", "main.py");

// 		const microbitFolder = await isInWorkspace('microbit/**'); // a folder called microbit with files inside
// 		if (!microbitFolder){
// 			clone("https://github.com/makinteract/microbit.git", path.join(workspace.uri.path, "microbit"))
// 		}	*/
// 	});


// 	// Setup MicroPython
// 	let initMicrobit = vscode.commands.registerCommand('extension.init-microbit', async function () {
// 		try {
// 			// run uflas without parameters to install MicroPython on microbit
// 			await runWithPython(`${uflash}`);
// 			vscode.window.showInformationMessage('MicroPython correctly installed on micro:bit');
// 		} catch (e) {
// 			vscode.window.showErrorMessage('MicroPython could not be installed on micro:bit');
// 		}
// 	});

// 	// Flash sketch
// 	let flashSketchCmd = vscode.commands.registerCommand('extension.flash-sketch', async function () {

// 		// check if main.py (entry point) is present
// 		if (! await isInWorkspace("main.py")) {
// 			vscode.window.showErrorMessage('Could not locate main.py');
// 			return;
// 		}

// 		try {
// 			copyFilesFromWorkspaceToDevice("*.{py}")
// 		} catch (e) {
// 			vscode.window.showErrorMessage('Could not upload the sketch on the micro:bit');
// 		}

// 		vscode.window.showInformationMessage('Sketch succssfully uploaded');
// 	});


// 	context.subscriptions.push(initCmd);
// 	context.subscriptions.push(initMicrobit);
// 	context.subscriptions.push(flashSketchCmd);
// }

// // this method is called when your extension is deactivated
// function deactivate() { }

// module.exports = {
// 	activate,
// 	deactivate
// }
