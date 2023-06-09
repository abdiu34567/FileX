import shutil
import os


def copy_file(source, dest_dir):
    try:
        for file in source:
            dest_file_path = os.path.join(dest_dir, os.path.basename(file))
            shutil.copy(file, dest_file_path)
            print(f'{source} copied to {dest_dir}')
    except Exception as e:
        print(f'Error: {e}')


def move_file(source, dest_dir):
    try:
        for file in source:
            dest_file_path = os.path.join(dest_dir, os.path.basename(file))
            shutil.move(file, dest_file_path)
            print(f'{source} moved to {dest_dir}')
    except Exception as e:
        print(f'Error: {e}')


def delete_file(source):
    try:
        for file in source:
            os.remove(file)
            print(f'{file} file deleted')
    except Exception as e:
        print(f'Error: {e}')


def move_dir(src_dir, dest_dir):
    try:
        for file in src_dir:
            dest_file_path = os.path.join(dest_dir, os.path.basename(file))
            shutil.move(file, dest_file_path)
            print(f"Moved {file} to {dest_dir}")
    except (shutil.Error, OSError) as e:
        print(f"Error moving directory: {e}")


def copy_dir(src_dir, dest_dir):
    try:
        for file in src_dir:
            dest_file_path = os.path.join(dest_dir, os.path.basename(file))
            shutil.copytree(file, dest_file_path)
            print(f"Copied {file} to {dest_dir}")
    except (shutil.Error, OSError) as e:
        print(f"Error copying directory: {e}")


def delete_dir(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"Deleted {dir_path}")
    except OSError as e:
        print(f"Error deleting directory: {e}")


def recursive_move(src_path, dest_path):
    try:
        move_dir(src_path, dest_path)
    except NotADirectoryError:
        move_file(src_path, dest_path)
    else:
        for item in os.listdir(src_path):
            src_item_path = os.path.join(src_path, item)
            dest_item_path = os.path.join(dest_path, item)
            recursive_move(src_item_path, dest_item_path)


def recursive_copy(src_path, dest_path):
    try:
        copy_dir(src_path, dest_path)
    except NotADirectoryError:
        copy_file(src_path, dest_path)
    else:
        for item in os.listdir(src_path):
            src_item_path = os.path.join(src_path, item)
            dest_item_path = os.path.join(dest_path, item)
            recursive_copy(src_item_path, dest_item_path)


def recursive_delete(path):
    try:
        delete_dir(path)
    except NotADirectoryError:
        delete_file(path)
    else:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            recursive_delete(item_path)


def rename_file(src_file, dest_file):
    try:
        os.rename(src_file, dest_file)
        print(f"Renamed {src_file} to {dest_file}")
    except OSError as e:
        print(f"Error renaming file: {e}")


def create_file(file_path):
    try:
        open(file_path, 'w').close()
        print(f"Created {file_path}")
    except OSError as e:
        print(f"Error creating file: {e}")
