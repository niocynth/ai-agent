import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):

    working_path = os.path.abspath(working_directory)
    absolute_path = (os.path.abspath(os.path.join(working_directory, file_path)))

    if not absolute_path.startswith(working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'

    if not absolute_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", absolute_path] + args, capture_output=True, cwd=working_path, timeout=30)
        result_string = f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}\n'
        if result.returncode != 0:
            result_str += f"Process exited with code {result.returncode}\n"
        if result.stdout == "" and result.stderr == "":
            result_string += "No output produced.\n"
        return result_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional arguments to pass through to the python file.",
            )
        },
    ),
)