# micro:bit + MicroPython for VSCode

![Version](https://img.shields.io/visual-studio-marketplace/v/MAKinteract.micro-bit-python)
![Downloads](https://img.shields.io/visual-studio-marketplace/d/MAKinteract.micro-bit-python)
![Installs](https://img.shields.io/visual-studio-marketplace/i/MAKinteract.micro-bit-python?color=pink)
![GitHub license](https://img.shields.io/badge/license-MIT-red.svg?style=flat-square)

![V1](https://img.shields.io/badge/micro:bit-V1-green)
![V2](https://img.shields.io/badge/micro:bit-V2-blue)

This extension provides a self-contained developing environment for developing with **MicroPython** using the **micro:bit** platform.

![](images/overview.png)

It allows to initialize a project with an optional template example, to upload a python _sketch_ (terminology borrowed from [Processing](<https://en.wikipedia.org/wiki/Processing_(programming_language)>)) on the micro:bit, or to remove/get files from the micro:bit file system. IntelliSense for function name completion is available for both the default micro:bit functionalities and for user-specified libraries.

> ⚠️ **Possible breaking changes in version 0.1.28+**:
> This version might result in breaking changes as we removed our dependency on the `uflash` project and updgraded to the latest micro:bit firmware. Please report problems using the [issues page](https://github.com/makinteract/vscode-microbit-micropython/issues).

## Commands

To see the commands for the extension, use the command palette (**Windows / Linux**: `CTRL + Shift + P`, **Mac**: `⌘ + Shift + P`) and search for `micro:bit-python`. You will see the following list.

![Commands](images/commands.png)

Each feature is explained in the sections below.

---

## Getting started

For a video tutorial on how to use this extension, please refer to [this link](https://youtu.be/eSGJLu1kqyg).

1. [Download and install](https://www.python.org/downloads/) python on your system preferably python3.
2. Open VSCode and install the [micro:bit python extension](https://marketplace.visualstudio.com/items?itemName=MAKinteract.micro-bit-python)
3. Connect the micro:bit via USB cable (make sure your cable allows for data transfer and it is not only a charging cable)
4. The first time, run the command `micro:bit-python: Flash MicroPython environment on micro:bit`
5. Open an empty workspace (aka folder) in VSCode and run the command `micro:bit-python: Initialize the workspace`. To start, choose the **hello-world** sample code.
6. Upload your files to the micro:bit using the command `micro:bit-python: Flash sketch on the micro:bit`.

---

## Features in detail

### `Flash MicroPython environment on the micro:bit`

Use this command the first time you use MicroPython. It will erase the micro:bit and install the MicroPython interpreter.

The uploaded firmware is a universal firmware composed of the latest MicroPython firmware for micro:bit [V1](https://github.com/bbcmicrobit/micropython/releases/tag/v1.1.1) and [V2](https://github.com/microbit-foundation/micropython-microbit-v2/releases/tag/v2.1.2): `micropython-microbit-v1.1.1.hex` and `micropython-microbit-v2.1.2.hex`.

### `Flash sketch on the micro:bit`

This command copies all the files from the current workspace on the micro:bit. For the command to work, there **must exist** a `main.py` file (the starting point of your program). Furthermore, _folders and files nested in folders will be ignored_ - only files at the root of the workspace will be copied. You can also use the shortcut `CTRL + F6` (Windows / Linux) or `⌘ + F6` (Mac).

For example, in the image below, `main.py` and `anotherfile.py` will be flashed onto the micro:bit, while the folder _microbit_ and all its content will be ignored.

![Flash](images/flash.png)

Under the hood, flashing is achieved using the [microfs](https://github.com/ntoll/microfs) script.

### `Initialize the workspace`

This command initializes the current workspace by copying a _microbit_ folder in the workspace (used to enable VScode IntelliSense), and by prompting the user to select a template file. The user can also optionally select additional libraries for extended IntelliSense support.

![Initialization](images/initialization.png)

For example, if the user were to pick `buttons` or `hello-world` from the list above, the files of these projects would be copied into the current workspace, overriding existing files.

The user can also select `Empty` - in such case, no changes to files occur.

The templates are fetched from this [online repository](https://github.com/makinteract/micropython-examples). The _microbit_ folder is fetched from [this respository](https://github.com/ElTrasho3000/Microbit-Basic-Stubs), while stubs for additional libraries are fetched from [here](https://github.com/ElTrasho3000/Microbit-Extended-Stubs). All these stubs are based on the [official micro:bit documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/).

### `Fetch examples from online`

This command manually fetches the latest example snippets from this [online repository](https://github.com/makinteract/micropython-examples). For this command to work, you must be connected to the Internet and you must have installed [git](https://git-scm.com) on your system.

### `List all files on the micro:bit`

This command shows a list of all the files stored on the micro:bit.

Under the hood, this command uses `ufs ls`.

### `Copy a file from the micro:bit`

This command shows the files stored on the micro:bit file system and prompts the user to pick one to be copied on the user's workspace.

Under the hood, this command uses `ufs get`.

### `Remove all files from the micro:bit`

This command removes all the files on the micro:bit files system (it will not remove the MicroPython interpreter though).

Under the hood, the command uses the `ufs rm` command.

### `Remove a single file from the micro:bit`

This command prompts the user to choose a file to remove from the micro:bit file system.

Under the hood, the command uses the `ufs rm` command.

### `Show micro:bit pins image`

It shows the image with the micro:bit pinout

<img src="images/pinout.png" height="300" />

---

## Requirments

The extension requires Python installed and in the _PATH_ variable. Other dependencies ([microfs](https://github.com/ntoll/microfs)) are taken care of automatically. For using the command `Fetch examples from online` and download the latest examples, you need to have [git](https://git-scm.com) installed on your machine.

This extension also draws some inspiration from [another micro:bit python extension](https://github.com/PhonicCanine/vscode-microbit), which you might want to consider as an alternative.

---

## For developers

If you want to modify this extension, fork and then clone this repository on your machine. Run `npm install`, to install dependencies (need to have Node.js installed). From any javascript file, press `F5` to run the extension locally in debug mode.

---

## Known Issues

The `SoundEffect` feature for micro:bit v2 is currently not supported. Please refer to this [issue](https://github.com/makinteract/vscode-microbit-micropython/issues/7) for a workaround.

For other issues, refer to the [issues page](https://github.com/makinteract/vscode-microbit-micropython/issues). Please file any issues there.

---

## Credits

Extension developed by [MAKinteract](https://makinteract.kaist.ac.kr). Stubs library for IntelliSense developed by [ElTrasho3000](https://github.com/ElTrasho3000). Icon design by [Hye-Young Jo](https://www.hyeyoungjo.com).

---

## Donation

If you like this extension, please consider buying me a coffee via the link below. Any amount is welcome. It will encourage me to improve this extension and make it better!

Support this project with:

<a href="https://www.buymeacoffee.com/andreaHCI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 125px !important" ></a>

---

## License

MIT
