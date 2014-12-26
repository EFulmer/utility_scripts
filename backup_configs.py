#!/usr/local/bin/python3
import os
import os.path
import shutil

CONFIG_FILES = ['~/.vimrc', '~/.vim/', '~/.emacs', '~/.emacs.d/', '~/.zshrc', 
                '~/.tmux.conf', ]
BACKUP_FOLDER = '~/projects/config/'


def get_home(path):
    return path.replace('~', os.environ['HOME'])

 
def newer_version(f, backup):
    """
    Compare the last modified times of f and backup. 
    Returns True if f is newer than backup, otherwise False.
    """
    if not os.path.exists(f):
        return False

    f_modtime = os.path.getmtime(f)
    # backup might not exist, so...
    try:
        b_modtime = os.path.getmtime(backup)
        return f_modtime > b_modtime
    except OSError:
        # if file hasn't been backed up before, True by default
        return True


def backup(f, backup_loc):
    """
    Back up file f to backup_loc. If f is a folder instead, 
    back its contents up to backup_loc.
    """
    if os.path.isfile(f):
        shutil.copy(f, os.path.join(f, backup_loc))
        print('Found and copied newer version of {0} to {1}'.format(f, backup_loc))
    else:
        dir_tree = os.walk(f)
        for _, dirs, files in dir_tree:
            for f in files:
                backup(f, backup_loc) 
            for d in dirs:
                backup(d, backup_loc)


def get_updated_cfgs(configs, backup_loc):
    updated_cfgs = [ f for f in configs 
                     if newer_version(f, backup_loc + os.path.split(f)[1]) ]
    return updated_cfgs


def main():
    cfgs = list(map(get_home, CONFIG_FILES))
    backup_loc = get_home(BACKUP_FOLDER)
    files_to_bkup = get_updated_cfgs(cfgs, backup_loc)
    for f in files_to_bkup:
        backup(f, backup_loc)


if __name__ == '__main__':
    main()
