# rename_git

English | [中文](./README_CN.md)

rename all files in same directory or modified file extension.
git for keep changed history(TODO:)

extra:

1. rename all file at the same directory with --number
2. add prefix or suffix with --number & --char (fixed)
3. del prefix or suffix.
4. change extension from --form .txt to --char .doc

## Libraries

- glob
- getopt

## Usage

    -i, --input     directory of files required to rename
    Option:
    -g, --git       store git history in git, require git
    -o, --output    directory where renamed fires move to
    -h, --help      list all the helps and exit
    -c, --char      add same char on files, combined with -p | -s
    -n, --number    add integer number at end of file name, start with n
    -f, --form      change form of files, e.g. mp4 of a.mp4
    -r, --rename    rename files with --number
    -p, --prefix    add extra characteristic on the start of file name, default is _
    -s, --suffix    add extra characteristic on the end of file name, default is _
    -d, --delete    delete first or last characteristics with -s or -p flag
