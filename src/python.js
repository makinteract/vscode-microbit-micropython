// A simple Python wrapper that keeps track of the version that works

const util = require('util');
const exec = util.promisify(require('child_process').exec);


function PythonException(message) {
  this.message = message;
  this.name = 'PythonException';
}

class Python {
  constructor() {
    this.python2 = true;
    this.python3 = true;
  }

  async run(command) {
    // try with python 3
    if (this.python3) {
      try {
        const { stdout, stderr } = await exec(`python3 ${command}`)
        return { stdout, stderr };
      } catch (e) {
        // python not found

        // this.python3 = false;
      }
    }

    // try with python 2
    if (this.python2) {
      try {
        const { stdout, stderr } = await exec(`python ${command}`)
        return { stdout, stderr };
      } catch (e) {
        // this.python2 = false;
        throw e;
      }
    }

    // none found
    throw new PythonException("Could not exectute command");
  }
}

// Create a singleton and prevent changes
const python = new Python();
Object.freeze(python);


module.exports = {
  PythonException,
  python
};