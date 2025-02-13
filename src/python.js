// A simple Python wrapper that keeps track of the version that works

const util = require('util');
const exec = util.promisify(require('child_process').exec);

function PythonException(message) {
  this.message = message;
  this.name = 'PythonException';
}

let python2 = true;
let python3 = true;
let error = false;

class Python {
  constructor() {
    python2 = true;
    python3 = true;
  }

  async run(command, baseDirectoryPath) {
    // try with python 3
    const workingDir = { cwd: baseDirectoryPath };

    if (python3) {
      try {
        const { stdout, stderr } = await exec(`python3 ${command}`, workingDir);
        return { stdout, stderr };
      } catch (e) {
        // python not found
        python3 = false;
        error = e;
      }
    }

    // try with python 2
    if (python2) {
      try {
        const { stdout, stderr } = await exec(`python ${command}`, workingDir);
        return { stdout, stderr };
      } catch (e) {
        python2 = false;
        if (error) throw error;
        throw e;
      }
    }

    // none found
    // reset the variables and throw an exception
    python2 = true;
    python3 = true;
    throw new PythonException('Could not exectute command');
  }
}

// Create a singleton and prevent changes
const python = new Python();
Object.freeze(python);

module.exports = {
  PythonException,
  python,
};
