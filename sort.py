import time
import os

from func_normalize import *
from unzip_files import *

main_path = Path('YOUR FOLDER PATH')
extensions = {
    'Video': ('mp4', 'mov', 'avi', 'mkv'),
    'Image': ('jpg', 'png', 'jpeg', 'svg'),
    'Documents': ('doc', 'docx', 'txt', 'pdf', 'djvu'),
    'Music': ('mp3', 'wav', 'ogg', 'amr'),
    'Archive': ('zip', 'rar', 'tar', 'gz'),
    'Presentation': ('pptx', 'ppt', 'pps', 'key', 'odp'),
    'Spreadsheet': ('xlsx', 'xls', 'xlsm', 'ods'),
    'Gif': ('gif'),
    'Exe': ('exe'),
    'Programming': ('cpp', 'py'),
}
folders = list(extensions.keys())


def get_subfolder_paths(folder_path):
    return (folder.path for folder in os.scandir(folder_path) if folder.is_dir())


def get_file_paths(folder_path):
    return (file.path for file in os.scandir(folder_path) if not file.is_dir())


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                if not os.path.exists(f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}'):
                    print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder')
                    os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')



    folders = get_subfolder_paths(folder_path)
    for folder in folders:
        check_path = os.path.basename(folder)
        if check_path in folders and check_path == "Unrecognized":
            continue
        else:
            sort_files(str(folder_path) + '\\' + check_path)


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1])
            os.rmdir(p)
        if os.path.exists(str(folder_path) + '\\' + p.split('\\')[-1]):
            remove_empty_folders(str(folder_path) + '\\' + p.split('\\')[-1])


def main() -> None:
    transliterator(str(main_path))
    print('Sorting files by extensions in', main_path)
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    unzip_files(str(main_path))
    remove_empty_folders(main_path)


if __name__ == "__main__":
    start_time = time.monotonic()
    main()
    end_time = time.monotonic() - start_time
    print(f'Script execution time: {end_time:.{3}f} seconds')
