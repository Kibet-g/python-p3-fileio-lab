def write_file(file_name, file_content):
    """Writes content to a file, creating the file if it doesn't exist."""
    with open(f"{file_name}.txt", 'w') as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """Appends content to an existing file. Creates the file if it doesn't exist."""
    with open(f"{file_name}.txt", 'a') as f:
        f.write(append_content)


def read_file(file_name):
    """Reads the content of a file and returns it."""
    with open(f"{file_name}.txt", 'r') as f:
        return f.read()
