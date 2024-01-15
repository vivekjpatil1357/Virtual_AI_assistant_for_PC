const { exec } = require('child_process');

// Replace 'your_script.py' with the name of your Python script
const pythonScript = 'app.py';

// Replace 'path_to_python_script_directory' with the actual path to your Python script
const scriptDirectory = 'path_to_python_script_directory';

// Command to run the Python script in a new cmd instance
const command = ` python ${pythonScript}`;

console.log("jelsdff")
exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (stderr) {
    console.error(`stderr: ${stderr}`);
    return;
  }

  console.log(`stdout: ${stdout}`);
});
