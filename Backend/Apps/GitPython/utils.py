import logging
import binascii
import os
from django.http import HttpResponse, JsonResponse
from git import Repo, Commit




local_repo_directory = os.path.join(os.getcwd(),'Python FullStack Test')
# repo = Repo(local_repo_directory)
# assert not repo.bare
destination = 'master'

def get_repo():
    return Repo(local_repo_directory)

def clone_repo():
    if os.path.exists(local_repo_directory):
        print("Directory exists, pulling changes from main branch")
        repo = Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(destination)
    else:
        print("Directory does not exists, cloning")
        Repo.clone_from("https://github.com/JulioGiovanni/fullstack-interview-test.git",
                        local_repo_directory, branch=destination)

def add_and_commit_changes(request):
    print("Commiting changes")
    print(request)
    # repo.git.add(update=True)
    # repo.git.commit("-m", "Adding a new line to the file.text file")

def get_branches(request):
    repo = Repo(local_repo_directory)
    branches = []
    print(repo.branches)
    for branch in repo.branches:
        branches.append(branch.name)
    return JsonResponse(branches,safe=False)

def branch(request,branch):
    repo = Repo(local_repo_directory)   
    commits = []
    for commit in repo.iter_commits('master'):
        commits.append({
            'id': commit.hexsha,
            'author': commit.author.name,
            'message': commit.message,
            'time': commit.authored_datetime
        })
    return JsonResponse({'commits': commits})


def push_changes(repo):
    print("Push changes")
    repo.git.push("--set-upstream", 'origin', destination)

def chdirectory(path):
    os.chdir(path)



