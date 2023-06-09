import argparse
import file_operations
import os

parser = argparse.ArgumentParser(
    description='A command-line tool for file operations')


def main():
    parser = argparse.ArgumentParser(description='Perform file operations.')
    parser.add_argument('operation', choices=[
                        'copy_file', 'move_file', 'delete_file', 'copy_dir',
                        'move_dir', 'delete_dir', 'copy_path, move_path, delete_path', 'rename_file', 'create_file'],
                        help='The file operation to perform')
    parser.add_argument('source', help='The source file or directory')
    parser.add_argument('destination', nargs='?', default='.',
                        help='The destination file or directory')

    args = parser.parse_args()

    # check if the file exist
    if not os.path.exists(args.source):
        print(f'Error: {args.source} does not exist')
        exit()

    if args.operation in ['move', 'copy', 'rename',] and not os.path.exists(args.destination):
        print(f'Error: {args.destination} does not exist')
        exit()

    if args.operation in ['move', 'copy', 'rename'] and os.path.isdir(args.source) and os.path.isfile(args.destination):
        print(f'Error: Cannot copy/move a directory to a file')
        exit()

    file_type = os.stat(args.src_file).st_mode
    if os.path.islink(args.src_file):
        print(f"Error: {args.src_file} is a symbolic link.")
        exit()
    elif os.path.isfifo(args.src_file):
        print(f"Error: {args.src_file} is a named pipe.")
        exit()
    elif os.path.isblk(file_type) or os.path.ischr(file_type):
        print(f"Error: {args.src_file} is a device file.")
        exit()

    if args.operation == 'copy_file':
        file_operations.copy_file(args.source, args.destination)
    elif args.operation == 'move_file':
        file_operations.move_file(args.source, args.destination)
    elif args.operation == 'delete_file':
        file_operations.delete_file(args.source)
    elif args.operation == 'move_dir':
        file_operations.move_dir(args.source, args.destination)
    elif args.operation == 'copy_dir':
        file_operations.copy_dir(args.source, args.destination)
    elif args.operation == 'delete_dir':
        file_operations.delete_dir(args.source)
    elif args.operation == 'move_path':
        file_operations.recursive_move(args.source, args.destination)
    elif args.operation == 'copy_path':
        file_operations.recursive_copy(args.source, args.destination)
    elif args.operation == 'delete_path':
        file_operations.recursive_delete(args.source)

    elif args.operation == 'rename_file':
        file_operations.rename_file(args.source, args.destination)

    elif args.operation == 'create_file':
        file_operations.create_file(args.source)


if __name__ == '__main__':
    main()
