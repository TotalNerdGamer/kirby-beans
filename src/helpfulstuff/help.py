import subprocess
import os
import sys

def python(file):
    cmd = f"\"{sys.executable}\" \"{file}\""
    #print(cmd)
    subprocess.call(cmd)