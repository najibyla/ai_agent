import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    

    if directory == ".":
        header = "Result for current directory:"
    else:
        header = f"Result for '{directory} directory:"
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'{header}\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        

        if not os.path.isdir(target_dir):
            return f'{header}\nError: "{directory}" is not a directory'
        
        msg=""
        for file in os.listdir(target_dir):
            name = file
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_directory = os.path.isdir(file_path)
            msg += f"- {name}: file_size={file_size} bytes, is_dir={is_directory}\n"

        return f"{header}\n{msg}"
    
    except Exception as e:

        return f"{header}\nError: {str(e)}"
        
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
    
