import os
import subprocess

def run_python_file(working_dir, file_path, args=None):
    try: 
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        completed = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        output = []

        if completed.returncode != 0:
            output.append(f'Process exited with code {completed.returncode}')
        if not completed.stdout.strip() and not completed.stderr.strip():
            output.append('No output')
        if completed.stdout.strip():
            output.append(f'STDOUT:\n{completed.stdout.strip()}')
        if completed.stderr.strip():
            output.append(f'STDERR:\n{completed.stderr.strip()}')
        
        return '\n'.join(output)
    except Exception as e:
        return f'Error: {e}'