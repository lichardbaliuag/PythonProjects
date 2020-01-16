
# Github PA Token: 76d794b72e02b9c8a3dd0b7091aa9f2892298338
# Using Username & Password: <lichardb:password>

import subprocess
import requests
import sys
import os
import pygit2

from github import Github

#gup = Github("lichardbaliuag","password")
gat = Github("76d794b72e02b9c8a3dd0b7091aa9f2892298338")
cur_dir = os.getcwd()
default_dir = os.chdir('C:\\Projects\\PythonProjects')
projectName = 'TestProjectRepo01'
projectDesc = 'First test project using this script'

def main():

    # 1. Create Github instance
    # reg = requests.post(
    #     "https://api.github.com/users/lichardbaliuag/repos?access_token=76d794b72e02b9c8a3dd0b7091aa9f2892298338",
    #     data={
    #         "name": "NewProject01",
    #         "description": "Test first repository using python",
    #         "homepage": "https://github.com",
    #         "private": false,
    #         "has_issues": true,
    #         "has_projects": true,
    #         "has_wiki": true
    #     }
    # )
    # if reg.status_code != 200:
    # sys.exit()
    
    # --- Show Repository List --- #
    # for repo in gat.get_user().get_repos():
    #     print(repo.name)

    # 1. Create Github instance
    
    try:
        org = gat.get_organization('codicepiratica')
        repo = org.create_repo(projectName, description = projectDesc)
        repo.create_file("/README.md", "init commit", readmeText)

        repoClone = pygit2.clone_repository(repo.git_url, default_dir)
        repoClone.remotes.seturl("origin", repo.clone_url)
        index = repoClone.index
        index.add_all()
        index.write()

        print("Current working directory", os.getcwd())


    except OSError:
        print("Error encountered in while cloning.")

### --------------------------------- ###
###         IMPLEMENTATION            ###
### --------------------------------- ###

if __name__ == '__main__':
    main()
