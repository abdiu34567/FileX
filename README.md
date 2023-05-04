# FileX 👉 File Operations CLI Tool

`Flex` is a `command-line interface (CLI)` tool that performs file operations such as moving, copying, or deleting files. The tool is written in Python and is designed to be simple and easy to use.

## Features

> - [x] **Move files from one directory to another**
> - [x] **Copy files from one directory to another**
> - [x] **Delete files from a directory**
> - [x] **Support for file patterns to select multiple files**
> - [x] **Support for custom destination directory**
> - [x] **Support for multiple file operations in a single command**
> - [x] **Error handling to check for file/directory existence and user permissions**
> - [x] **Recursive operations to copy/move entire directories and their contents**
> - [x] **Support for different types of file operations, such as renaming or creating new files**
> - [x] **Support for different types of files, such as symbolic links or device files**
> - [x] **Custom file filters to select files based on criteria such as file size or modification date**
> - [x] **Platform-specific support for Windows or macOS.**

<br>

## Usage

The tool accepts the following command-line arguments:

```bash
python filetool.py [operation] [source] [destination]
```

### Where:

- operation can be one of `move_file`, `copy_file`, or `delete_file`, `move_dir`, `copy_dir`, `delete_dir`, `copy_path`, `move_path` `delete_path`'

- source is the path to the file(s) to be operated on. It can contain wildcards to match multiple files.

- destination is the path to the directory where the file(s) should be moved/copied. It is optional and defaults to the current directory for the delete operation.

<br>

## Examples

- To move all .txt files from /path/to/source to /path/to/destination:

```bash
python filetool.py move /path/to/source/*.txt /path/to/destination
```

- To copy all .jpg files from /path/to/source to /path/to/destination:

```bash
python filetool.py copy /path/to/source/*.jpg /path/to/destination
```

To delete all .log files from /path/to/source:

```bash
python filetool.py delete /path/to/source/*.log
```

<br>

## Future Enhancements

The tool can be further improved by adding the following features:

- Support for other types of file operations, such as archive or compression
- Improved user interface, such as interactive mode or progress indicators
- Batch processing of files with custom scripts or commands
- Integration with cloud storage services or remote servers
- Support for other platforms or operating systems.
