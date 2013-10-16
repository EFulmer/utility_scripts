import os
import sys

TEMP_FILE_SIGNIFIERS = ['~']

def kill_temps(path, recursive=False):
    for p in os.path.expanduser(path):
        files = os.listdir(p)
        temp_files = filter(lambda f: f[-1] == '~', files)
        map(lambda t: os.remove(p + '/' + t), temp_files)    

def main():
    """
    Deletes all temporary files in each of the path names given as args.
    The path names may be absolute or relative.
    """
    if len(sys.argv) == 1:
        print 'Please provide at least one path name.'
    else:


if __name__ == '__main__':
    main()
