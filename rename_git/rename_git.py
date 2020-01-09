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
    self.rename = None
    self.prefix = False
    self.suffix = False
    self.files = []
  
  # recall variables
  def __call__(self, in_folder=None, ot_folder=None, char=None,
              form=None, number=-1, rename=None, 
              prefix=False, suffix=True, files=[]):
    self.in_folder = in_folder
    if ot_folder == None:
      self.ot_folder = in_folder
    else:
      self.ot_folder = ot_folder
    self.char = char
    self.form = form
    self.number = number
    self.rename = rename
    self.prefix = prefix
    self.suffix = suffix
    self.files = files

  # execution for command line
  def exec_opt(self, argv):
    try:
      opts, args = getopt.getopt(argv, "hi:o:c:f:n:r:ps",
        ["help", "input=", "output=", "char=", "form=", "number=", "rename=", "prefix", "suffix"])
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
      elif opt in ("-o", "--output"):
        self.ot_folder = arg
      elif opt in ("-c", "--char"):
        self.char = arg
      elif opt in ("-f", "--form"):
        self.form = arg
      elif opt in ("-n", "--number"):
        self.number = int(arg)
      elif opt in ("-r", "--rename"):
        self.rename = arg
      elif opt in ("-p", "--prefix"):
        self.prefix = True
      elif opt in ("-s", "--suffix"):
        self.suffix = True
      else:
        # print error info && exit
        print("rename_git.py: invalid option", opt)
        print("Try \'--help\' for  for more informion")
        sys.exit(2)

    # input must have value & check input folder
    if self.in_folder == None:
      print("Error: invalid usage. Must need input folder path!")
      self.usage()
      print()
      print("rename_git.py --help list all helps")
      sys.exit(2)
    self.in_folder = os.path.join(self.in_folder, '')
    if not os.path.exists(self.in_folder):
      print("Error: input folder", self.in_folder, "not exist")
      sys.exit(2)
    # double check ot_folder is None & check output folder
    if self.ot_folder == None:
      self.ot_folder = self.in_folder
    else:
      self.ot_folder = os.path.join(self.ot_folder, '')
    if not os.path.exists(self.ot_folder):
      print("Error: output folder", self.ot_folder, "not exist")
      sys.exit(2)
    # if form not None
    if not self.form == None:
      self.files = [os.path.basename(f) for f in glob.glob(self.in_folder+"*."+self.form)]
    else:
      self.files = [os.path.basename(f) for f in glob.glob(self.in_folder+"*.*")]

  def exec_form(self):
    #check char & form exist
    if self.char == None or self.form == None:
      print("Error: changing file format requires char and form")
      print("       --form for old files extention, --char for new")
      print()
      self.usage()
      sys.exit(2)
    # find files under specific folder
    form_num = len(self.form)
    # TODO: opt future
    for f in self.files:
      os.rename(self.in_folder+f,
                self.ot_folder+f[:len(f)-form_num]+self.char)

  def exec_ps(self):
    # execute char first
    if not self.char == None:
      # list all files under specific folder
      if self.prefix:
        for f in self.files:
          os.rename(self.in_folder+f, 
                    self.ot_folder+self.char+f)
      if self.suffix:
        for f in self.files:
          base_split = os.path.splitext(f)
          os.rename(self.in_folder+f,
                    self.ot_folder+base_split[0]+self.char+base_split[1])
      # set default
      if not self.prefix and not self.suffix:
        for f in self.files:
          base_split = os.path.splitext(f)
          os.rename(self.in_folder+f,
                    self.ot_folder+base_split[0]+"_"+self.char+base_split[1])
    # execute number
    if not self.number == -1:
      # list all files under specific folder
      if self.prefix:
        i = self.number
        for f in self.files:
          os.rename(self.in_folder+f, 
                    self.ot_folder+str(i)+f)
          i += 1
      if self.suffix:
        j = self.number
        for f in self.files:
          base_split = os.path.splitext(f)
          os.rename(self.in_folder+f, 
                    self.ot_folder+base_split[0]+str(j)+base_split[1])
          j += 1
      # set default
      if not self.prefix and not self.suffix:
        k = self.number
        for f in self.files:
          base_split = os.path.splitext(f)
          os.rename(self.in_folder+f,
                    self.ot_folder+base_split[0]+'_'+str(k)+base_split[1])
          k += 1
  def exec_rename(self):
    # rename combined with number
    if self.rename != None and self.number == -1:
      print("Error: invalid usage. rename must use number")
      self.usage()
      print()
      print("rename_git.py --help list all helps")
      sys.exit(2)
    # list all files
    if self.prefix:
      i = self.number
      for f in self.files:
        if not self.char == None:
          i_str = str(i) + self.char
        else:
          i_str = str(i)
        os.rename(self.in_folder+f,
                  self.ot_folder+i_str+f)
        i += 1
    if self.suffix:
      i = self.number
      for f in self.files:
        if not self.char == None:
          i_str = self.char + str(i)
        else:
          i_str = str(i)
        base_split = os.path.splitext(f)
        os.rename(self.in_folder+f,
                  self.ot_folder+base_split[0]+i_str+base_split[1])
        i += 1
    # set default
    if not self.prefix and not self.suffix:
      i = self.number
      for f in self.files:
        base_split = os.path.splitext(f)
        os.rename(self.in_folder+f,
                  self.ot_folder+base_split[0]+"_"+str(i)+base_split[1])
      i += 1

  def exec_git(self):
    pass

  def exec_main(self, argv):
    self.exec_opt(argv)
    if not self.rename == None:
      self.exec_rename()
    elif not self.form == None:
      self.exec_form()
    elif self.char != None or self.number != -1:
      self.exec_ps()
    else:
      print("Error: unknown error!")
      self.usage()
      print()
      print("rename_git.py --help list all helps")
    return

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
    print("-o, --output \t directory where renamed fires move to")
    print("-h, --help \t list all the helps and exit")
    print("-c, --char \t add same char on files, combined with -p | -s")
    print("-n, --number \t add integer number at end of file name, start with n")
    print("-f, --form \t change form of files, e.g. mp4 of a.mp4")
    print("-r, --rename \t rename files with --number")
    print("-p, --prefix \t add extra characteristic on the start of file name, default is _")
    print("-s, --suffix \t add extra characteristic on the end of file name, default is _")

    # TODO: rename all files with options
    sys.exit(0)


if __name__ == "__main__":
  rename = rename_git()
  rename.exec_main(sys.argv[1:])
  print("Rename done!")
