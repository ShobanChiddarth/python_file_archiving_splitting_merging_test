from main import *
import os

file_to_be_compressed = os.path.join( os.environ.get('HOME'), 'Downloads', 'ISO Files', 'debian-live-12.5.0-amd64-gnome.iso' )
archive_to_be_created = './out/myarchive.7z'
extracting_directory = './out/extraction/'

archive_single_file(file_to_be_compressed, archive_to_be_created)
extract_archive(archive_to_be_created, extracting_directory)
