import os
import sys

TEMP_FILE_SIGNIFIERS = ['~'] # gonna do something with this; re.match??

def kill_temps(paths, recursive=False):
    for p in paths:
        path = os.path.expanduser(p)
        files = os.listdir(path)
        temp_files = filter(lambda f: f[-1] == '~', files)
        map(lambda t: os.remove(path + '/' + t), temp_files)    

def main():
    """
    Deletes all temporary files in each of the path names given as args.
    The path names may be absolute or relative.
    If no argument is given, temp files in the current directory will be 
    killed.
    """
    if len(sys.argv) == 1:
        kill_temps('.')
    else:
        kill_temps(sys.argv[1:])


if __name__ == '__main__':
    main()
