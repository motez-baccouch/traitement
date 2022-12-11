import subprocess
import sys

def openFolder(path):
    if sys.platform == 'darwin':
        subprocess.check_call(['open', '--', path])
    elif sys.platform == 'linux2':
        subprocess.check_call(['xdg-open', '--', path])
    elif sys.platform == 'win32':
        subprocess.check_call(['explorer', path])