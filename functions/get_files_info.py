import os

def get_files_info(working_directory, directory="."):

    working_path = os.path.abspath(working_directory)
    absolute_path = (os.path.abspath(os.path.join(working_directory, directory)))

    if not absolute_path.startswith(working_path):
        return f'Error: cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
