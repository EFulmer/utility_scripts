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
    f_stat = os.stat(f)
    try:
        b_stat = os.stat(backup)
        return f_stat.st_ctime > b_stat.st_ctime
    except OSError:
        # if file hasn't been backed up before, True by default
        return True


def backup(f, backup_loc):
    """
    Back up file f to backup_loc. If f is a folder instead, 
    back its contents up to backup_loc.
    """
    # TODO automatically add stuff to repo, commit + push it
    # check what f is:
    # if f is a file, just do copy(f, os.path.join(f, backup_loc)
    # otherwise, os.walk over the directory and move each of the files.
    if os.path.isfile(f):
        shutil.copy(f, os.path.join(f, backup_loc))
        print('Found and backed up newer version of {0}'.format(f))
    else:
        dir_tree = os.walk(f)
        # TODO this is ugly. make it nicer.
        for item in dir_tree:
            for fil in item[2]:
                backup(fil, backup_loc) 
            for fld in item[1]:
                backup(fld, backup_loc)


def get_updated_cfgs(configs, backup_loc):
    updated_cfgs = [ f for f in configs 
                     if newer_version(f, backup_loc + os.path.split(f)[1]) ] # if this doesn't work try adding os.path.isfile(f) as another condition
    return updated_cfgs


def main():
    cfgs = list(map(get_home, CONFIG_FILES))
    backup_loc = get_home(BACKUP_FOLDER)
    files_to_bkup = get_updated_cfgs(cfgs, backup_loc)
    for f in files_to_bkup:
        backup(f, backup_loc)


if __name__ == '__main__':
    main()
