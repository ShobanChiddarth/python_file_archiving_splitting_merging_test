from main import *
import os

if not os.path.exists('./out'):
    os.makedirs('./out')
if not os.path.exists('./out/multipart'):
    os.makedirs('./out/multipart')
if not os.path.exists('./out/extraction'):
    os.makedirs('./out/extraction')
if not os.path.exists('./out/temp'):
    os.makedirs('./out/temp')

file_to_be_compressed = os.path.join( os.environ.get('HOME'), 'Downloads', 'ISO Files', 'kali-linux-2023.4-installer-everything-amd64.iso' )
archive_to_be_created = './out/myarchive.7z'
multipart_directory = './out/multipart/'
extracting_directory = './out/extraction/'
temp_archive = './out/temp/temp.7z'

archive_single_file(file_to_be_compressed, archive_to_be_created)
split_file(archive_to_be_created, multipart_directory)
merge_parts(multipart_directory, temp_archive)
extract_archive(temp_archive, extracting_directory)

