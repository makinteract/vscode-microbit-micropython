// globals
  





/**
 * Get the path of the examples folder 
 * @returns - path of examples folder
//  */
// function examplesPath() {
//  const extRoot = extensionRootPath();
//  return path.join(extRoot, "examples");
// }




  





  async function getListFilesOnMicrobit() {
    const { stdout: filenames, stderr: err } = await ufs("ls");

    if (filenames.includes("Could not find micro:bit")) {
      throw new Error("Could not find micro:bit");
    }
    if (err) {
      throw new Error(err)
    }

    const files = filenames.split(" ").filter(name => name.length > 0);
    return files;
  }

  async function getFileSelectionFromUser(filesAvailable) {
    const fileToRemove = await ui.showQuickPick(filesAvailable, '')

    if (!fileToRemove) throw new Error("No input specified");
    return [fileToRemove];
  }

  async function removeFilesFromMicrobit(removeAll = false) {

    // may throw an exception
    let filesToRemove = await getFilesOnMicrobit();
    // Check whether these files are valid (non-empty list)
    if (!filesToRemove || filesToRemove.length == 0) {
      throw new Error("No files on micro:bit");
    }

    if (!removeAll) filesToRemove = await getFileSelectionFromUser(filesToRemove);

    // remove the files
    for (let file of filesToRemove) {
      await ufs(`rm ${file}`);
    }
    const names = filesToRemove.join(', ');
    ui.vsInfo("Files successfully removed");
    outInfo(`Files ${names} removed from micro:bit`);
  }

  async function initWorkspace() {
    let workspace = await extension.getCurrentWorkspace();

    if (!workspace) {
      // select a workspace
      workspace = await vscode.commands.executeCommand("vscode.openFolder");
      // this will refresh VScode
    }

    // clone microbit repo if not already there
    const microbitFolder = await extension.isFileInCurrentWorkspace('microbit/**'); // a folder called microbit with files inside
    if (!microbitFolder) {
      clone(MICROBIT_LIBS, path.join(workspace.uri.path, "microbit"))
    }

    // pick from template
    const example = await getExampleUri();
    if (example) {
      console.log(example);
      //   const src = vscode.Uri.file(path.join(extensionRootPath(), "examples", example));
      //  const dest = vscode.Uri.file(path.join(workspace.uri.path, ));

    }

    // if main not there, alert user
    const main = await extension.isFileInCurrentWorkspace('main.py');
    if (main) ui.vsInfo("Sketch ready");
    else ui.vsInfo("Remember to create a main.py file");
  }

  const getDirectories = source =>
    readdirSync(source, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name)
      .filter(name => !name.startsWith('.'));


  // HERE
  async function getExampleUri() {
    let examplesDir = "";
    try {
      examplesDir = path.join(extensionRootPath(), "examples");
    } catch (e) {
      throw new Error("Fetch the examples first");
    }
    // stat(examplesDir, function (err, stat) {
    //   if (err == null) {
    //   }
    // });

    const list = getDirectories(examplesDir);
    const pick = await ui.showQuickPick(list, 'empty');
    if (pick) {
      const uri = vscode.Uri.joinPath(vscode.Uri.file(examplesDir), pick);
      return uri;
    }
    return undefined;
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
