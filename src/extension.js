// General utilities for the extension
const vscode = require('vscode');
const path = require('path');
const os = require ('os');

const { python, PythonException } = require('./python');
const { openStdin } = require('process');
// const util = require('util');
// const clone = require('git-clone');

// Globals
const EXAMPLES_REPO = "https://github.com/makinteract/micropython-examples";
const MICROBIT_LIBS_REPO = "https://github.com/makinteract/microbit.git";
const EXTENSION_ID = "MAKinteract.micro-bit-python";



/**
 * Get path where extension is stored in teh filesystem
 * @returns - path of extension root folder
 */
function extensionRootPath() {
	return vscode.extensions.getExtension(EXTENSION_ID).extensionPath;
}

/**
 * Get URI of extension folder
 * @returns - URI of extension folder
 */
function extensionUri() {
	return vscode.extensions.getExtension(EXTENSION_ID).extensionUri;
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
 * Get workspace URI given document as input
 * @param {*} openDocument - the selected document
 * @returns - the workspace URI or undefined if the document parameters was invalid
 */
function getWorkspace(openDocument) {
	if (!openDocument) return undefined;
	const workspace = vscode.workspace.getWorkspaceFolder(openDocument.uri);
	return workspace;
}

/**
 * Get workspace URI given current open document as input
 * @returns - the current workspace URI or undefined if no document is open
 */
function getOpenWorkspace() {
	const document = vscode.window.activeTextEditor.document;
	return getWorkspace(document);
}

/**
 * Get current workspace
 * @returns - return the current workspace 1) if any document is open
 * 2) else if only one workspace is open, return that one
 * 3) else if multiple workspaces are open ask the user to choose
 * 4) else if no workspace is open, ask user to pick one
 */
async function getCurrentWorkspace() {
	// 1) a document is open
	const openDocumnet = vscode.window.activeTextEditor?.document;
	if (openDocumnet)
		return getOpenWorkspace();

	// else get all workspaces
	const workspaces = vscode.workspace.workspaceFolders;

	// 2) if there is only one open, return it
	if (workspaces?.length == 1) return workspaces[0];

	// 3) else multiple workspaces, therfore ask the user to pick one
	const selection = await vscode.window.showWorkspaceFolderPick()
	if (selection) return selection;

	// 4) else if no workspace is open, ask user to open one
	await vscode.commands.executeCommand("vscode.openFolder");
	// this will refresh VScode
}

/**
 * Get the files in the workspace
 * @param {String} pattern - a pattern describing the files to pick (defaul is all '*')
 * @returns - teh files in the workspace
 */
async function getFilesInCurrentWorkspace(pattern = "*") {
	const workspace = await getCurrentWorkspace();
	// the workspace is guaranteed to exist

	// get all the files matched by the pattern in the workspace and copy them to the microbit
	const workspaceFiles = await vscode.workspace.findFiles(
		new vscode.RelativePattern(workspace, pattern)
	);
	return workspaceFiles;
}

/**
	 * Get the base name of a file, given 
	 * @param {String} filepath - the path from which to extract the file name
	 * @returns 
	 */
function pathToName(filepath) {
	const filename = path.parse(filepath).base;
	return filename;
}


/**
 * Assert whether a file is included in a list of files
 * @param {String} filename - the file name
 * @param {vscode.Uri[]} fileList - the list of names
 */
function assertFileIsIncluded(filename, fileList) {
	const files = fileList.map(({ path }) => pathToName(path));
	if (!files.includes(filename)) {
		throw new Error(`Can't find file ${filename}`);
	}
}


async function listFilesOnMicrobit() {
    const { stdout: filenames, stderr: err } = await ufs("ls");

	if (err) {
      throw new Error(err)
    }

    const files = filenames.split(" ").filter(name => name.length > 0);
    return files;
  }

async function removeFilesFromMicrobit(filesToRemove) {
    if (!filesToRemove || filesToRemove.length == 0) {
      throw new Error("No files specified for deletion");
    }

    // remove the specified files
    for (let file of filesToRemove) {
      await ufs(`rm ${file}`);
    }
  }

  async function getFileFromMicrobit(filename, destinationUri){
	  // might throw an exception if the file does not exist
	  const dest = path.join(destinationUri.path, filename);
	  await ufs (`get ${filename} ${dest}`);
  }




/**
 * Run the uflash python script (may throw an exception)
 * @param {String} params - string with parameters passed to "python uflash.py"
 * @returns - stdout and sterr from python command
 */
async function uflash(params = "") {
	const tools = toolsPath();
	const uflash = path.join(tools, "uflash-master", "uflash.py");
	const { stdout, stderr } = await python.run(`${uflash} ${params}`)
	return { stdout, stderr };
}

/**
 * Run the ufs python script (may throw an exception)
 * @param {String} params - string with parameters pased to "pyton ufs.py"
 * @returns - stdout and sterr from python command
 */
async function ufs(params = "") {
	const tools = toolsPath();
	const ufs = path.join(tools, "microfs-master", "ufs.py");
	const { stdout, stderr } = await python.run(`${ufs} ${params}`);
	// Handle errors
	if (stdout.includes("Could not find micro:bit")) {
		throw new Error("Could not find micro:bit");
	}
	else if (stdout.includes("Errno 13")){
		if (os.platform() == "linux")
			throw new Error(`Could not open serial port. Do you have permissions?\n
							 Try run "sudo chmod 666 /dev/ttyACM0"`);

		else	
			throw new Error("Could not open serial port.");
	}
	else if (stdout.includes("Error"))
		throw new Error (stdout);
	else
		return {stdout, stderr};
}










module.exports = {
	uflash,
	ufs,
	extensionRootPath,
	extensionUri,
	toolsPath,
	getWorkspace,
	getOpenWorkspace,
	getCurrentWorkspace,
	getFilesInCurrentWorkspace,
	assertFileIsIncluded,
	listFilesOnMicrobit,
	removeFilesFromMicrobit,
	getFileFromMicrobit
	// runWithPython,
	// getWorkspace,
	// getOpenWorkspace,
	// getCurrentWorkspace,
	// getFilesInCurrentWorkspace,
	// isFileInCurrentWorkspace
};





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
