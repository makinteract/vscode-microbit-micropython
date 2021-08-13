const vscode = require('vscode');
// const child_process = require('child_process');
const path = require('path')
const util = require('util');
const exec = util.promisify(require('child_process').exec);


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	const dir = vscode.extensions.getExtension("MAKinteract.vscode-microbit-micropython").extensionPath;
	const uflash = path.join(dir, "res", "uflash-master", "uflash.py")
	const ufs = path.join(dir, "res", "microfs-master", "ufs.py")
	const output = vscode.window.createOutputChannel("micro:bit");


	function checkPython() {
		const fn = vscode.window.activeTextEditor.document.fileName;
		if (!fn.endsWith(".py")) {
			vscode.window.showErrorMessage(`Error: the current document (${fn}) is not a Python file. Please make sure the cursor is in an active Python file, before trying that command again.`)
			return false;
		}
		return true;
	}

	async function runWithPython(command) {
		// try with python 3
		try {
			const { stdout, stderr } = await exec(`python3 ${command}`)
			output.appendLine(`Command "${command}" successfully executed: ${stdout}`);
			if (!stderr) return;
		} catch (e) {
		}

		// try with python 2
		try {
			const { stdout, stderr } = await exec(`python ${command}`)
			output.appendLine(`Command "${command}" successfully executed: ${stdout}`);
		} catch (e) {
			throw new Error;
		}
	}

	async function isInWorkspace(filename) {
		const document = vscode.window.activeTextEditor.document;
		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

		// get all the python files in the workspace and copy them to the microbit
		const file = await vscode.workspace.findFiles(
			filename
		);

		return file.length > 0;
	}


	// Init microbit
	let initCmd = vscode.commands.registerCommand('extension.initialize', async function () {
		// const a = await isInWorkspace('microbit/**'); // a folder called microbit with files inside
		// const b = await isInWorkspace('main.py');
		// const c = await isInWorkspace('a.py');
		// console.log(a, b, c);

		const document = vscode.window.activeTextEditor.document;
		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);
		const loc = context.asAbsolutePath('.');

		const main = await isInWorkspace('main.py')
		if (!main) {
			const src = vscode.Uri.file(path.join(loc, "templates", "main.py"));
			const dest = vscode.Uri.file(path.join(workspace.uri.path, "main.py"));
			vscode.workspace.fs.copy(src, dest, { "overwrite": true });
		}

	});




	// Flash command
	let flashMicroCmd = vscode.commands.registerCommand('extension.flash-micropython', async function () {
		try {
			// run uflas without parameters to install MicroPython on microbit
			await runWithPython(`${uflash}`);
			vscode.window.showInformationMessage('MicroPython correctly installed on micro:bit');
		} catch (e) {
			vscode.window.showErrorMessage('MicroPython could not be installed on micro:bit');
		}
	});

	// Flash sketch
	let flashSketchCmd = vscode.commands.registerCommand('extension.flash-sketch', async function () {
		const document = vscode.window.activeTextEditor.document;
		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);

		// get all the python files in the workspace and copy them to the microbit
		const workspaceFiles = await vscode.workspace.findFiles(
			new vscode.RelativePattern(workspace, `{*.py}`)
		);

		for (let { path } of workspaceFiles) {
			try {
				await runWithPython(`${ufs} put ${path}`);
			} catch (e) {
				vscode.window.showErrorMessage('Could not upload the sketch on the micro:bit');
				return;
			}
		}
		vscode.window.showInformationMessage('Sketch succssfully uploaded');
	});

	context.subscriptions.push(initCmd);
	context.subscriptions.push(flashMicroCmd);
	context.subscriptions.push(flashSketchCmd);



}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
