import argparse
import file_operations

parser = argparse.ArgumentParser(description='A command-line tool for file operations')

def main():
    parser = argparse.ArgumentParser(description='Perform file operations.')
    parser.add_argument('operation', choices=['copy', 'move', 'delete'], help='The file operation to perform')
    parser.add_argument('source', help='The source file or directory')
    parser.add_argument('destination', nargs='?', default='.', help='The destination file or directory')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively perform the operation')
    args = parser.parse_args()

    if args.operation == 'copy':
        file_operations.copy_file(args.source, args.destination, recursive=args.recursive)
    elif args.operation == 'move':
        file_operations.move_file(args.source, args.destination, recursive=args.recursive)
    elif args.operation == 'delete':
        file_operations.delete_file(args.source, recursive=args.recursive)

if __name__ == '__main__':
    main()