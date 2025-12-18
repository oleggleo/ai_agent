import os

def get_files_info(working_dir, dir='.'):
    
    try:
        working_abs = os.path.abspath(working_dir)
        target_dir = os.path.normpath(os.path.join(working_abs, dir))

        if not os.path.isdir(target_dir):
            return f'Error: {dir} is not a directory' 

        if os.path.commonpath([working_abs, target_dir]) != working_abs:
            return f'Error cannot list {dir}.'

        lines = []

        for name in os.listdir(target_dir):
            full_path = os.path.join(target_dir, name)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)

            lines.append(f'- {name}: file_size= {file_size} bytes, is_dir={is_dir}')
        
        return '\n'.join(lines)
    except Exception as e:
        return f'Error: {e}'