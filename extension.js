const vscode = require('vscode');
const path = require('path')
const util = require('util');
const exec = util.promisify(require('child_process').exec);
const clone = require('git-clone');

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	const extRoot = vscode.extensions.getExtension("MAKinteract.vscode-microbit-micropython").extensionPath;
	const uflash = path.join(extRoot, "tools", "uflash-master", "uflash.py")
	const ufs = path.join(extRoot, "tools", "microfs-master", "ufs.py")
	const output = vscode.window.createOutputChannel("micro:bit");
	let python2 = true;
	let python3 = true;

	async function runWithPython(command) {
		// try with python 3
		if (python3){
			try {
				const { stdout, stderr } = await exec(`python3 ${command}`)
				output.appendLine(`Command "${command}" successfully executed: ${stdout}`);
				if (!stderr) return;
			} catch (e) {
				python3= false;
			}
		
		}else if (python2){
			// try with python 2
			try {
				const { stdout, stderr } = await exec(`python ${command}`)
				output.appendLine(`Command "${command}" successfully executed: ${stdout}`);
				if (!stderr) return;

			} catch (e) {
				python2= false;
			}
		}
		
		// none found
		throw new Error("Could not exectute command");
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
	let initCmd = vscode.commands.registerCommand('extension.init-sketch', async function () {
		
		const loc = context.asAbsolutePath('.');
		
		const document = vscode.window.activeTextEditor.document;
		const workspace = vscode.workspace.getWorkspaceFolder(document.uri);
		
		const main = await isInWorkspace("main.py");
		if (!main){
				const src = vscode.Uri.file(path.join(loc, "main_template.py"));
				const dest = vscode.Uri.file(path.join(workspace.uri.path, "main.py"));
				vscode.workspace.fs.copy(src, dest, { "overwrite": false });
		}
			

		const microbitFolder = await isInWorkspace('microbit/**'); // a folder called microbit with files inside
		if (!microbitFolder){
			clone("https://github.com/makinteract/microbit.git", path.join(workspace.uri.path, "microbit"))
		}	
	});


	// Setup MicroPython
	let initMicrobit = vscode.commands.registerCommand('extension.init-microbit', async function () {
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
		
		// check if main.py (entry point) is present
		if (! await isInWorkspace("main.py")){
			vscode.window.showErrorMessage('Could not locate main.py');
			return;
		}
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
	context.subscriptions.push(initMicrobit);
	context.subscriptions.push(flashSketchCmd);
}

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
