import shutil
import os


def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f'{source} copied to {destination}')
    except Exception as e:
        print(f'Error: {e}')


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f'{source} moved to {destination}')
    except Exception as e:
        print(f'Error: {e}')


def delete_file(source):
    try:
        os.remove(source)
        print(f'{source} file deleted')
    except Exception as e:
        print(f'Error: {e}')


def move_dir(src_dir, dest_dir):
    try:
        shutil.move(src_dir, dest_dir)
        print(f"Moved {src_dir} to {dest_dir}")
    except (shutil.Error, OSError) as e:
        print(f"Error moving directory: {e}")


def copy_dir(src_dir, dest_dir):
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Copied {src_dir} to {dest_dir}")
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
