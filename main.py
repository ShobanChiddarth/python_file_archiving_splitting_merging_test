import py7zr
import pathlib


# Compress and Archive a single file
def archive_single_file(input_file: str, output_file: str, archive_name: str = None) -> None:
    """\
This function is to be used for archiving a single file into a 7z archive.

Args:
- `input_file`
    Path of the file to be archived.
- `output_file`
    Path of the archive to be created.
- `archive_name`
    Name of the file to be archived in the archive, including the extension.
    If left empty, the basename of the input file will be used.
"""
    if archive_name is None:
        archive_name = pathlib.Path(input_file).name
    with py7zr.SevenZipFile(output_file, 'w') as archive:
        archive.write(input_file, archive_name)


# Extract and Decompress an archive
def extract_archive(input_file: str, output_folder: str = None) -> None:
    """\
This function is to be used to extract a 7z archive to a folder

Args:
- `input_file`
    Path of the archive to be extracted.
- `output_folder`
    Path of the folder to extract the archive to.
    If left empty, the archive will be extracted to the folder that contains `input_file`
"""
    if output_folder is None:
        output_folder = str(pathlib.Path(input_file).parent)
        if not output_folder.endswith('/'):
            output_folder += '/'
        elif not output_folder.endswith('\\'):
            output_folder += '\\'
    with py7zr.SevenZipFile(input_file, 'r') as archive:
        archive.extractall(path=output_folder)

