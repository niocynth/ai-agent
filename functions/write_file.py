import os

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