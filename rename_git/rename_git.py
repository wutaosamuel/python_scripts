# Aims:
# 1. rename all file at the same directory

import os
import sys
import getopt

class rename_git:

  # init rename_git
  def __init__(self, in_folder="./", ot_folder="./"):
    self.in_folder = in_folder
    self.ot_folder = ot_folder
  
  # recall variables

  # execution for command line
  def exec_opt(self, argv):
    try:
      opts, args = getopt.getopt(argv, "hi:o:c:f:n:ps",
        ["help", "input=", "output=", "char=", "format=", "number=", "prefix", "suffix"])
    except getopt.GetoptError:
      print("Error: invalid usage")
      print()
      self.usage()

    # read argv
    for opt, arg in opts:
      if opt in ("-h", "--help", "help"):
        self.print_help()
    

  def exec_git(self):
    pass

  #################### HELP ####################

  def print_more_help(self):
    print("rename_git.py -h || --help for more helps")

  def usage(self):
    print("rename_git.py [-i <inputfolder>] [option]")
    print("or")
    print()
    self.print_more_help()

  def print_help(self):
    self.usage()
    print()
    print("-i, --input \t directory of files required to rename")
    print()
    print("Option:")
    print("-c, --char \t add same char on files, combined with -p | -s")
    print("-f, --format \t change format of files")
    print("-h, --help \t list all the helps and exit")
    print("-n, --number \t add integer number at end of file name, start with n")
    print("-o, --output \t directory where renamed fires move to")
    print("-p, --prefix \t add extra characteristic on the start of file name, default is _")
    print("-s, --suffix \t add extra characteristic on the end of file name, default is _")

    # TODO: rename all files with options
    sys.exit(0)


if __name__ == "__main__":
  pass
