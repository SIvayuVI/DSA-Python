from configparser import ConfigParser

# config file contains user settings
config_file = '/home/gst/Documents/siva/DataEngineer/Config_git.ini'
config = ConfigParser()
config.read(config_file)
  
# get all settings from config file
access_token = config.get('Git', 'github_token')
repo_name = config.get('Git', 'repo_name')
first_file = config.get('Git', 'commit_file')
msg = config.get('Git', 'first_commit_msg')
github_name = config.get('Git', 'github_name')
  
pc_directory = config.get('Git', 'directory')
repo_directory = pc_directory + '/' + repo_name

import subprocess
from pathlib import Path

def create_local_git_repo():
  
   # create directory if it doesn't exist
   check_dir = Path(pc_directory)
   if check_dir.exists():
       print("Directory exists. Skip create directory")
   else:
       subprocess.run(["mkdir", pc_directory])

# create repo folder if it doesn't exist
   print("Creating repo: %s" % repo_directory)
  
   check_repo = Path(repo_directory)
   if check_repo.exists():
       print("Repo already exists. Skip git init")
   else:
       subprocess.run(["mkdir", repo_directory])
       # init repo
       subprocess.run(["git", "init"], cwd=repo_directory)

def create_local_repo_file():
  
   file_path = repo_directory + "/" + first_file
   print("Adding file: %s" % file_path)
  
   # create file if it doesn't exist
   check_file = Path(file_path)
   if check_file.exists():
       print("File already exists. Skip create file")
   else:
       subprocess.run(["touch", first_file], cwd=repo_directory)
   pass
   
def add_files_for_commit():
  
   # stage file created
   subprocess.run(["git", "add", first_file], cwd=repo_directory)
   pass
  
  
def commit_files():
  
   # commit file
   subprocess.run(["git", "commit", "-m", msg], cwd=repo_directory)
   pass
create_local_git_repo()
