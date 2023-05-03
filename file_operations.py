import shutil
import os

def copy_file(source, destination, recursive=False):

    directory = os.path.dirname(destination)
    
    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    if recursive:
        shutil.copytree(source, os.path.join(destination, os.path.basename(source)))
    else:
        shutil.copy2(source, destination)

def move_file(source, destination, recursive=False):
    if recursive:
        shutil.move(source, os.path.join(destination, os.path.basename(source)))
    else:
        shutil.move(source, destination)

def delete_file(source, recursive=False):
    if recursive:
        shutil.rmtree(source)
    else:
        os.remove(source)
