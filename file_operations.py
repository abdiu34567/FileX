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
        if os.path.isdir(source):
            shutil.rmtree(source)
            print(f'{source} directory deleted')
        else:
            os.remove(source)
            print(f'{source} file deleted')
    except Exception as e:
                print(f'Error: {e}')