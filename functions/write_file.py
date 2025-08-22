import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_path = os.path.abspath(working_directory)
    absolute_path = (os.path.abspath(os.path.join(working_directory, file_path)))

    if not absolute_path.startswith(working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(absolute_path):
            path = os.path.dirname(absolute_path)
            os.makedirs(path, exist_ok=True)
        with open(absolute_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates or overwrites a file with provided content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file you wish to create or overwrite, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)