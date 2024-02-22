import os
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


# For splitting a large binary file into smaller parts
def split_file(input_file: str,
               output_folder: str = None,
               output_file_basename: str = None,
               max_limit: int = int(2E+9)) -> None:
    """\
This function is to be used to split a large binary file into smaller parts.

Note: Each part is stored as filename.part0, filename.part1, and so on.

Args:
- `input_file`
    Path of the file to be split.
- `output_folder`
    Path of the folder to save the parts to.
    If left empty, the parts will be saved to the folder that contains `input_file`
- `output_file_basename`
    Basename of the parts to be saved.
    If left empty, the basename of the `input_file` will be used.
- `max_limit`
    Limit of each part in bytes. Default is 2 GB.
"""
    if output_folder is None:
        output_folder = str(pathlib.Path(input_file).parent)
        if not output_folder.endswith('/'):
            output_folder += '/'
        elif not output_folder.endswith('\\'):
            output_folder += '\\'
    if output_file_basename is None:
        output_file_basename = pathlib.Path(input_file).name
    
    with open(input_file, 'rb') as fh:
        data = fh.read()
    
    for ii in range(0, (len(data)//max_limit)):
        with open(os.path.join(output_folder, output_file_basename)+f'.part{ii}', 'wb') as fout:
            fout.write(data[ii*max_limit:(ii+1)*max_limit])
    
    with open(os.path.join(output_folder, output_file_basename)+f'.part{ii+1}', 'wb') as fout:
        fout.write(data[(ii+1)*max_limit:])


# For merging parts of a binary file into a single file
def merge_parts(input_folder: str,
                output_file: str = None) -> None:
    """\
This function is to be used to merge parts of a binary file into a single file.

Note: Each part is assumed to be stored as filename.part0, filename.part1, and so on.

Args:
- `input_folder`
    Path of the folder containing the parts to be merged.
- `output_file`
    Path of the file to save the merged data to.
    If left empty, the merged data will be saved to the folder that contains `input_folder`
    with the basename of the first part.
"""
    for root, dirs, files, in os.walk(input_folder):
        parts = sorted([os.path.join(root, file) for file in files])
    
    if output_file is None:
        output_file = os.path.join(input_folder, parts[0].split('.part')[0])
    
    with open(output_file, 'wb') as fout:
        data = b''
        for part in parts:
            with open(part, 'rb') as fin:
                data += fin.read()
        fout.write(data)