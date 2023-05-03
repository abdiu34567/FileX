import argparse
import file_operations
import os

parser = argparse.ArgumentParser(
    description='A command-line tool for file operations')


def main():
    parser = argparse.ArgumentParser(description='Perform file operations.')
    parser.add_argument('operation', choices=[
                        'copy_file', 'move_file', 'delete_file', 'copy_dir',
                        'move_dir', 'delete_dir', 'copy_path, move_path, delete_path'],
                        help='The file operation to perform')
    parser.add_argument('source', help='The source file or directory')
    parser.add_argument('destination', nargs='?', default='.',
                        help='The destination file or directory')

    args = parser.parse_args()

    # check if the file exist
    if not os.path.exists(args.source):
        print(f'Error: {args.source} does not exist')
        exit()

    if args.operation in ['move', 'copy'] and not os.path.exists(args.destination):
        print(f'Error: {args.destination} does not exist')
        exit()

    if args.operation in ['move', 'copy'] and os.path.isdir(args.source) and os.path.isfile(args.destination):
        print(f'Error: Cannot copy/move a directory to a file')
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


if __name__ == '__main__':
    main()
