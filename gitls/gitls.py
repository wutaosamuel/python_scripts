# Aims:
# 1. display status between branches and remotes 


from git import Repo

class gitls:



  def is_git_repo(path):
    try:
      _ = Repo(path).git_dir
      return True
    except GExc.InvalidGitRepositoryError:
      return False
