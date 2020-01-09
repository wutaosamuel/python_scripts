# Aims:
# 1. sort same suffix file in a folder
# 2. cp all files into sub-folder or specified folder
# 3. store change history in git

import os
import sys
import git  # replace pygit2 && future replace
import glob
import time
import shutil
import getopt


class sort_in_git:
#TODO: remove incorrect suffix file at sort_xxx directory

    # init for sort_in_git
    def __init__(self, suffix=None, in_folder=None, ot_folder=None):
        self.in_folder = in_folder
        self.ot_folder = ot_folder
        self.suffix = suffix

    # recall variables
    def __call__(self, suffix=None, in_folder=None, ot_folder=None):
        self.in_folder = in_folder
        self.ot_folder = ot_folder
        self.suffix = suffix
    # execution for command line
    def exec_opt(self, argv):
        try:
            opts, args = getopt.getopt(argv, "hs:i:o:",
                                       ["help", "suffix=", "input=", "output="])
        except getopt.GetoptError:
            print("Error: invalid usage")
            self.usage()
            print("[-h | --help]")
            print()
            print("sort_in_git.py --help list all helps")
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.print_help()
            elif opt in ("-s", "--suffix"):
                self.suffix = arg
            elif opt in ("-i", "--input"):
                self.in_folder = arg
            elif opt in ("-o", "--output"):
                self.ot_folder = arg
            else:
                # print error info && exit
                print("sort_in_git.py: invalid option", opt)
                print("Try \'--help\' for  for more information")
                sys.exit(2)
        # suffer & input must have value
        if self.suffix == None or self.in_folder == None:
            print("Error: invalid usage. Must need input folder path!")
            self.usage()
            print("[-h | --help]")
            print()
            print("sort_in_git.py --help list all helps")
            sys.exit(2)
        # check input folder exist
        if not os.path.exists(self.in_folder):
            print("Error: ", self.in_folder, "not exist")
            sys.exit(2)
        # check output folder
        if self.ot_folder == None:
            ot_folder = "sort_" + self.suffix
            self.ot_folder = os.path.join(self.in_folder, ot_folder)
            if not os.path.exists(self.ot_folder):
                os.makedirs(self.ot_folder)

    # TODO: c multi-thread for sort
    def exec_sort(self):
        # sort suffix files
        files = glob.glob(self.in_folder+'*.'+self.suffix)
        if len(files) == 0:
            mach_info = "no *."+self.suffix+" match on " + \
                os.path.abspath(self.in_folder)
            print(mach_info)
            return
        # copy to sorted director
        for f in files:
            shutil.copy2(f, self.ot_folder)
        print("files sorted & copied, wait for writing change log")

    # TODO: simple history changed recording without gitpython module, like git
    def exec_git(self):
        git_commit = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        # check .git exit on output folder
        try:
            repo = git.Repo(self.ot_folder)
            print("git exit, add change log")
        except git.exc.InvalidGitRepositoryError:
            repo = git.Repo.init(self.ot_folder)
            print("Initialised git")
        repo.git.add(A=True)
        repo.index.commit(git_commit)
        print("finish to add change log")

    #################### HELP ###################

    def usage(self):
        print("sort_in_git.py [-s <suffix>] [-i <inputfolder>] [option]")
        print("or")
        print(
            "sort_in_git.py [--suffix=<suffix>] [--input=<inputfolder>] [option]")

    def print_help(self):
        self.usage()
        print()
        print("-s, --suffix \t suffix of files at the same directory")
        print("-i, --input \t directory that requires sort ")
        print()
        print("Options: ")
        print("-h, --help \t list all helps and exit")
        print("-o, --output \t directory that keeps all sorted file")
        sys.exit(0)


if __name__ == "__main__":
    sort = sort_in_git()
    sort.exec_opt(sys.argv[1:])
    sort.exec_sort()
    sort.exec_git()
    print("Sort done!")
