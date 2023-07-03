def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:
        return 'the file has no extension'
    else:
        return filename_parts[-1]

