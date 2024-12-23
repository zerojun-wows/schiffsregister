"""
    Every 60 seconds all files in repo will be pushed to Github

    Source: 
    https://mathspp.com/blog/til/automatically-push-code-changes-during-live-coding
"""
from pathlib import Path
from time import sleep, strftime

from git import Repo

repo = Repo(Path(__file__).parent)

while True:
    print(f'{strftime("%Y_%m_%d-%H_%M")} : Auto sync commit')
    repo.index.add("*")
    repo.index.commit("Auto sync commit")
    repo.remote().push()
    sleep(60)
