import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    working_path = os.path.abspath(working_directory)
    absolute_path = (os.path.abspath(os.path.join(working_directory, directory)))

    if not absolute_path.startswith(working_path):
        return f'Error: cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files = []
        for file in os.listdir(absolute_path):
            file_path = os.path.join(absolute_path, file)
            files.append(f"- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")
        return "\n".join(files)

    except Exception as e:
        return f"Error: {str(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)