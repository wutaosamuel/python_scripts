# sort_in_git

[English](./README.md) | 中文

整理指定文件夹下所有拥有相同后缀的文件，
把他们拷贝到指定的文件夹下面或者子文件下，文件名为sort_XXX 。
利用git的版本记录来记录所有文件改变的情况。

## 使用方法

    sort_in_git.py [-s <suffix>] [-i <inputfolder>] [option]
    or
    sort_in_git.py [--suffix=<suffix>] [--input=<inputfolder>] [option]

    Where:
    -s, --suffix      suffix of files at the same directory
    -i, --input       directory that requires sort
    
    Options:
    -h, --help        list all help and exit
    -o, --output      directory that keeps all sorted file
