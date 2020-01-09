# Aims:
# 1. rename all file at the same directory

import os
import sys
import glob
import getopt

class rename_git:
  # TODO: allow file[n]

  # init rename_git
  def __init__(self, in_folder=None, ot_folder=None):
    self.in_folder = in_folder
    if ot_folder == None:
      self.ot_folder = in_folder
    else:
      self.ot_folder = ot_folder
    self.char = None
    self.form = None
    self.number = -1
    self.prefix = False
    self.suffix = False
  
  # recall variables
  def __call__(self, in_folder=None, ot_folder=None, char=None,
              form=None, number=-1, prefix=False, suffix=True):
    self.in_folder = in_folder
    if ot_folder == None:
      self.ot_folder = in_folder
    else:
      self.ot_folder = ot_folder
    self.char = char
    self.form = form
    self.number = number
    self.prefix = prefix
    self.suffix = suffix

  # execution for command line
  def exec_opt(self, argv):
    try:
      opts, args = getopt.getopt(argv, "hi:o:c:f:n:ps",
        ["help", "input=", "output=", "char=", "form=", "number=", "prefix", "suffix"])
    except getopt.GetoptError:
      print("Error: invalid usage")
      print()
      self.usage()

    # read argv
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        self.print_help()
      elif opt in ("-i", "--input"):
        self.in_folder = arg
      elif opt in ("o", "--output"):
        self.ot_folder = arg
      elif opt in ("c", "--char"):
        self.char = arg
      elif opt in ("f", "--form"):
        self.form = arg
      elif opt in ("n", "--number"):
        self.number = arg
      elif opt in ("p", "--prefix"):
        self.prefix = arg
      elif opt in ("s", "--suffix"):
        self.suffix = arg
      else:
        # print error info && exit
        print("sort_in_git.py: invalid option", opt)
        print("Try \'--help\' for  for more informion")
        sys.exit(2)

    # input must have value & check input folder
    if self.in_folder == None:
      print("Error: invalid usage. Must need input folder path!")
      self.usage()
      print("[-h | --help]")
      print()
      print("sort_in_git.py --help list all helps")
      sys.exit(2)
    if not os.path.exists(self.in_folder):
      print("Error: input folder", self.in_folder, "not exist")
      sys.exit(2)
    # double check ot_folder is None & check output folder
    if self.ot_folder == None:
      self.ot_folder = self.in_folder
    if not os.path.exists(self.ot_folder):
      print("Error: output folder", self.ot_folder, "not exist")
      sys.exit(2)

  def exec_form(self):
    #check char & form exist
    if self.char == None or self.form == None:
      print("Error: changing file format requires char and form")
      print()
      self.usage()
      sys.exit(2)
    # find files under specific folder
    files = glob.glob(self.in_folder+"*."+self.form)
    form_num = len(self.form)
    # TODO: opt future
    for f in files:
      os.rename(self.in_folder+f,
                self.ot_folder+f[:len(f)-form_num]+self.char)

  def exec_ps(self):
    # only process char or number
    if self.char != None and self.number != -1:
      print("Error: changing file format requires char and form")
      print()
      self.usage()
      sys.exit(2)
    # execute number

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
    print("-f, --form \t change form of files, e.g. mp4 of a.mp4")
    print("-h, --help \t list all the helps and exit")
    print("-n, --number \t add integer number at end of file name, start with n")
    print("-o, --output \t directory where renamed fires move to")
    print("-p, --prefix \t add extra characteristic on the start of file name, default is _")
    print("-s, --suffix \t add extra characteristic on the end of file name, default is _")

    # TODO: rename all files with options
    sys.exit(0)


if __name__ == "__main__":
  pass
