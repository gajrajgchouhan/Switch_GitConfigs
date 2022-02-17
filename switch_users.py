import subprocess
from pathlib import Path
from dotenv import dotenv_values
import shutil
import argparse


def load_config(folder):
    req = PATH / folder
    gitConfigPath = req / "gitConfig"  # file
    sshPath = req / "ssh"  # folder

    return gitConfigPath, sshPath


CONFIG_CMDS = ["git", "config", "--global"]
PATH = Path(__file__).parent

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help="Folder to load config from", required=True)
args = parser.parse_args()
gitConfigPath, sshPath = load_config(args.folder)
envdict = dotenv_values(dotenv_path=gitConfigPath)

for key, value in envdict.items():
    subprocess.run(CONFIG_CMDS + [key, value])

shutil.copytree(sshPath, "/home/gajraj/.ssh/", dirs_exist_ok=True)
