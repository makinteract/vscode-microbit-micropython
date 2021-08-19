// General utilities for the extension
const vscode = require('vscode')
const {parse} = require('path')
const os = require('os')
const fs = require('fs')
const clone = require('git-clone')
const internetAvailable = require("internet-available")


const { python, PythonException } = require('./python')
const { openStdin } = require('process')

// Globals
const EXTENSION_ID = "MAKinteract.micro-bit-python";


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
	return vscode.Uri.joinPath(extensionUri(), "tools");
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
 * Get a list of all the files in a specified directory
 * @param {vscode.Uri} dirUri - the directory in which to search
 * @param {String} pattern - the pattern representing the files (defaul all "*")
 * @returns return a list of files
 */
async function getFilesInDir(dirUri, pattern = "*") {
	// get all the files matched by the pattern in the workspace and copy them to the microbit
	const workspaceFiles = await vscode.workspace.findFiles(
		new vscode.RelativePattern(dirUri, pattern)
	);
	return workspaceFiles;
}


async function getVisibleFoldersInDir(dirUri) {
	const ls = await vscode.workspace.fs.readDirectory(dirUri);
	return ls
		.filter(f => f[1] > 1) // it is a folder, not a file
		.filter(f => !f[0].startsWith('.')) // not hidden
		.map(f => f[0]) // only the name
}



/**
	 * Get the base name of a file, given 
	 * @param {String} filepath - the path from which to extract the file name
	 * @returns 
	 */
function pathToName(filepath) {
	const filename = parse(filepath).base;
	return filename;
}


/**
 * Assert whether a file is included in a list of files
 * @param {String} filename - the file name
 * @param {vscode.Uri[]} fileList - the list of names
 */
function assertFileIsIncluded(filename, fileList) {
	const files = fileList.map(({ fsPath: path }) => pathToName(path));
	if (!files.includes(filename)) {
		throw new Error(`Can't find file ${filename}`);
	}
}


/**
 * Get a list of all the files stored on the Microbit
 * @returns list of files
 */
async function listFilesOnMicrobit() {
	const { stdout: filenames, stderr: err } = await ufs("ls");

	if (err) {
		throw new Error(err)
	}

	const files = filenames.split(" ").filter(name => name.length > 0);
	return files;
}

/**
 * Remove a file from Microbit b yname
 * @param {String[]} filesToRemove 
 */
async function removeFilesFromMicrobit(filesToRemove) {
	if (!filesToRemove || filesToRemove.length == 0) {
		throw new Error("No files specified for deletion");
	}

	// remove the specified files
	for (let file of filesToRemove) {
		await ufs(`rm ${file}`);
	}
}

/**
 * Get file from Microbit by name and copy it in the destinationUri (overrite)
 * @param {String} filename - file in Microbit
 * @param {vscode.Uri} destinationDirUri - destination folder 
 */
async function getFileFromMicrobit(filename, destinationDirUri) {
	// might throw an exception if the file does not exist
	const dest = vscode.Uri.joinPath(destinationDirUri, filename);
	await ufs(`get ${filename} ${dest}`);
}

/**
 * Run the uflash python script (may throw an exception)
 * @param {String} params - string with parameters passed to "python uflash.py"
 * @returns - stdout and sterr from python command
 */
async function uflash(params = "") {
	const tools = toolsPath();
	const uflash = vscode.Uri.joinPath(tools, "uflash-master", "uflash.py");
	const { stdout, stderr } = await python.run(`${uflash.fsPath} ${params}`)
	return { stdout, stderr };
}

/**
 * Run the ufs python script (may throw an exception)
 * @param {String} params - string with parameters pased to "pyton ufs.py"
 * @returns - stdout and sterr from python command
 */
async function ufs(params = "") {
	const tools = toolsPath();
	const ufs = vscode.Uri.joinPath(tools, "microfs-master", "ufs.py");
	const { stdout, stderr } = await python.run(`${ufs.fsPath} ${params}`);
	// Handle errors
	if (stdout.includes("Could not find micro:bit")) {
		throw new Error("Could not find micro:bit");
	}
	else if (stdout.includes("Errno 13")) {
		if (os.platform() == "linux")
			throw new Error(`Could not open serial port. Do you have permissions?\n
							 Try run "sudo chmod 666 /dev/ttyACM0"`);

		else
			throw new Error("Could not open serial port.");
	}
	else if (stdout.includes("Error"))
		throw new Error(stdout);
	else
		return { stdout, stderr };
}


async function deleteFileFromDir(filename, destinationDirUri) {
	const todelete = vscode.Uri.joinPath(destinationDirUri, filename);
	try {
		await vscode.workspace.fs.delete(todelete, { recursive: true, useTrash: true });
	} catch (e) {
		console.log(`File/folder ${todelete.toString()} not found`);
	}
}

/**
 * Check whether an internet connection is available
 * @param {*} retries - retries, default 2
 * @param {*} timeout - timeout default 500ms
 * @returns true/false
 */
function isOnline(retries = 2, timeout = 500) {
	return new Promise(res =>
		internetAvailable({
			timeout,
			retries,
		}).then(function () {
			res(true)
		}).catch(function () {
			res(false);
		}));
}

/**
 * Clone repository (assume is online, silent if it fails)
 * @param {*} reponame - the name/address of the repository
 * @param {*} targetName - destination folder name
 * @param {*} destinationDirUri - destination base folder URI
 */
async function cloneRepository(reponame, targetName, destinationDirUri) {
	// check whether connected to internet, otherwise throw exception
	const dir = vscode.Uri.joinPath(destinationDirUri, targetName);
	clone(reponame, dir);
}



async function checkFileExist(filename, dirUri) {
	const check = s => new Promise(r => fs.access(s, fs.constants.F_OK, e => r(!e)))
	const loc = vscode.Uri.joinPath(dirUri, filename);
	const result = await check(loc)
	return result;
}

async function copyFiles(sourceDirUri, destDirUri) {
	const files = await getFilesInDir(sourceDirUri);
	files.forEach(file => {
		const fname = pathToName(file.fsPath);
		copyFile(fname, sourceDirUri, destDirUri);
	});
}


async function copyFile(filename, sourceDirUri, destDirUri) {
	const src = vscode.Uri.joinPath(sourceDirUri, filename);
	const dest = vscode.Uri.joinPath(destDirUri, filename);
	vscode.workspace.fs.copy(src, dest, { "overwrite": true });
}



module.exports = {
	uflash,
	ufs,
	extensionUri,
	toolsPath,
	getWorkspace,
	getOpenWorkspace,
	getCurrentWorkspace,
	getFilesInDir,
	getVisibleFoldersInDir,
	assertFileIsIncluded,
	listFilesOnMicrobit,
	removeFilesFromMicrobit,
	getFileFromMicrobit,
	deleteFileFromDir,
	cloneRepository,
	isOnline,
	checkFileExist,
	copyFiles
};