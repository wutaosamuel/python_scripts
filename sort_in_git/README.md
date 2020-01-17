# sort_in_git

English | [中文](./README_CN.md)

sort out all same suffix files at specified directory
and copy them into specified directory or sub-directory
with name 'sort_xxx'.
The git is used for recording files changed history.

## Libraries

- git
- glob
- time
- shutil
- getopt

## Usage

    sort_in_git.py [-s <suffix>] [-i <inputfolder>] [option]
    or
    sort_in_git.py [--suffix=<suffix>] [--input=<inputfolder>] [option]

    Where:
    -s, --suffix      suffix of files at the same directory
    -i, --input       directory that requires sort
    
    Options:
    -h, --help        list all help and exit
    -o, --output      directory that keeps all sorted file
    -g, --git         store git history in git
