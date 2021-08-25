const vscode = require('vscode');


/**
 *
 * @param {String} message - An info message to display as a VSCode toaster
 */
function vsInfo(message) {
  vscode.window.showInformationMessage(message);
}

/**
 *
 * @param {String} message - An error message to display as a VSCode toaster
 */
function vsError(message) {
  vscode.window.showErrorMessage(message);
}

/**
 * Show a quick pick
 * @param {String[]} itemArray - List of possible picks
 * @param {String} placeHolder - String placeholder
 * @returns synchronously returns the picked string
 */
async function showQuickPick(itemArray, placeHolder) {
  const result = await vscode.window.showQuickPick(itemArray, {
    placeHolder,
    onDidSelectItem: (item) => item
  });
  return result?.trim();
}

/**
 * Show an input text box in VSCode
 * @param {*} value - initial value
 * @param {*} placeHolder - placeholder string
 * @param {function} validationFn - function to validate the value, take text as input
 * @returns synchronously returns the picked string
 */
async function showInputBox(value, placeHolder, validationFn) {
  const result = await vscode.window.showInputBox({
    value,
    placeHolder,
    validateInput: (text) => validationFn(text),
  });
  return result;
}

/**
 * Ask for confirmation
 * @param {*} msg - the question to ask
 * @param {String[]} options - array of options
 * @returns - return one of the options
 */
async function confirmationMessage(msg, options) {
  return vscode.window
    .showInformationMessage(
      msg,
      ...options
    );
}


// Output command line

const output = vscode.window.createOutputChannel("micro:bit");

/**
 * Output info on console
 * @param {String} msg - the message to output
 */
function outInfo(msg) {
  const date = `[${new Date()}]`;
  output.appendLine(`SUCCESS ${date}\n${msg}\n`);
}

/**
 * Output error on console
 * @param {String} msg - the message to output
 */
function outError(msg) {
  const date = `[${new Date()}]`;
  output.appendLine(`ERROR ${date}\n${msg}\n`);
}

/**
 * Get image map (as in https://github.com/cpwood/Pico-Go)
 * @param {vscode.Uri} imageUrl 
 * @returns html cod eto render the image in a separte tab
 */
function getPinMap(imageUrl) {
  return `<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pico Pin Map</title>
        <style type="text/css">
            body {
                background-color: #191c2b;
            }
        </style>
    </head>
    <body>
        <img src="${imageUrl}" />
    </body>
    </html>`;
}



module.exports = {
  vsInfo,
  vsError,
  showQuickPick,
  showInputBox,
  confirmationMessage,
  outInfo,
  outError,
  getPinMap
};