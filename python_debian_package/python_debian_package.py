# Aims:
# 1. build .deb in terms of architecture

# requirement:
# TODO: deb package dir tree

import os
import sys
import glob
import hashlib
import platform

class python_debian_package:

  # FIXME: auto multi arch
  def __init__(self, deb_dir=None):
    self.deb_dir = deb_dir
    self.debian = None
    self.name=None
    self.system = self.detectSys()
    self.architecture = self.detectArch()
    self.version = -1
    self.make = None

  def exec_opt(self):
    pass
  
  def detectSys(self):
    # FIXME: more system detail
    sys = platform.system()
    if sys == "Linux":
      return "linux"
    else:
      print(sys+" is not support")
      print("Linux system only")
      self.print_help()

  def detectArch(self):
    arch = platform.machine()
    # TODO: support more machine
    if arch == "i386":
      return "386"
    if arch == "x86_64":
      return "amd64"
    if arch == "AMD64":
      return "amd64"
    if arch == "PowerPC":
      return "ppc"
    else:
      print(arch+" is not support")
      self.print_help()
  
  def replace_control(self, version=None, architecture=None):
    # FIXME: modified multi arch
    if version == None or architecture == None:
      print("Please enter version or architecture")
      self.print_help()
    deb = os.path.join(deb_dir, "debian")
    Deb = os.path.join(deb_dir, "DEBIAN")
    if os.path.exists(deb):
      self.debian = deb
    if os.path.exists(Deb):
      self.debian = Deb
    if self.debian == None:
      print("no such "+deb+" or "+Deb+" directory")
      self.print_help()
    control = os.path.join(self.debian, "control")
    if not os.path.exists(control):
      print("no such "+control+" file")
    # replace version and architecture
    file_data = ""
    with os.open(control, "rw") as f:
      for line in f:
        if "Version" in line:
          line = line.replace("Version:"+version)
        if "Architecture" in line:
          line = line.replace("Architecture:"+architecture)
        file_data += line
    with os.open(control, "rw") as f:
      f.writelines(file_data)
  
  def md5sum(self):
    usr = os.path.join(deb_dir, "usr")
    files = []
    md5s = []
    # recode files and each md5 sum
    for f in sorted(
      glob.glob(os.path.join(usr, "**"), recursive=True)):
      if os.path.isfile(f):
        with os.open(f, "rb") as content:
          md5 = hashlib.md5(content.encode("utf-8")).hexdigest()
        # reformat: ./usr/*
        filesplit = os.path.split(f)
        isUsr = False
        filepath = "."
        for index in len(filesplit):
          if filesplit[index] == "usr":
            isUsr = True
          if isUsr:
            filepath += "/"+filesplit[index]
        files.append(filepath)
        md5s.append(md5)
    # write it into md5sum
    # format of md5sums:
    # 3q2...  ./usr/**
    md5file = os.path.join(self.debian, "md5sums")
    md5data = ""
    for line in range(len(files)):
      md5data += md5s[line] + "  " + files[line]
    with os.open(md5file, "w") as md5f:
      md5f.writelines(md5data)
  
  def exec_make(self):
    os.system(self.make)
  
  def exec_deb(self):
    pass

  ################## HELP ###################

  def print_more_help(self):
    print("python_debian_package.py \'-h\' | \'--help\' for more helps")

  def usage(self):
    print("python_debian_package.py [-i <inputfolder>] [option]")
    print("or")
    self.print_more_help()

  def print_help(self):
    helpstring = '''
    -n, --name     name of target program
    -s, --system   target system
    -a, --arch     target architecture
    -V, --Version  target version

    Option:
    -m, --make     make binary package by Makefile
    '''
    self.usage()
    print()
    print(helpstring)
    sys.exit(0)

if __name__ == "__main__":
  deb = python_debian_package()
  print(deb.print_help())