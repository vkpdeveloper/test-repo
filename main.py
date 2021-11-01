# from git import Repo
# repo = Repo.init('.')  # if repo is CWD just do '.'

# repo.git.checkout("-b", "main")

# repo.git.add("main.py")
# repo.git.commit("-m", "new commit at some time")

# origin = repo.remote(name="main")

# origin.add_url("https://github.com/vkpdeveloper/test-repo.git")

# origin.push()

import os
from git import Repo

PATH_OF_GIT_REPO = "."  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    repo = Repo.init(PATH_OF_GIT_REPO)
    repo.git.checkout("-b", "main")
    repo.git.add("main.py")
    repo.git.commit("-m", "new commit at some time")
    remote = repo.create_remote("main", url="https://github.com/vkpdeveloper/test-repo.git")
    remote.push(refspec='{}:{}'.format("main", "main"))  

git_push()