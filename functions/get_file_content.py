import os
from config import *
from google.genai import types

def get_file_content(working_directory, file_path):
    
    working_path = os.path.abspath(working_directory)
    absolute_path = (os.path.abspath(os.path.join(working_directory, file_path)))

    if not absolute_path.startswith(working_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(absolute_path, "r") as f:
            file_contents = f.read(MAX_CHARS)
            if len(file_contents) == MAX_CHARS:
                return file_contents + f'[...File "{file_path}" truncated at {MAX_CHARS} characters].'
            return file_contents

    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Outputs the content of a file as a string, limited by length to the variable MAX_CHARS, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to export, relative to the working directory.",
            ),
        },
    ),
)