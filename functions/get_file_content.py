import os

def get_file_content(working_dir, file_path):
    working_abs = os.path.abspath(working_dir)
    target_file = os.path.normpath(os.path.join(working_abs, file_path))

    if os.path.commonpath([working_abs, target_file]) != working_abs:
        return f'Error cannot list {file_path}.'

    if not os.path.isfile(target_file):
        return f'Error: {file_path} is not a file'

    MAX_CHARS = 10000
    content = ''

    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f'Error: {e}'