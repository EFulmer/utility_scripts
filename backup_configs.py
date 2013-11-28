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
        return f_stat.st_ctime > b_stat.ctime
    except OSError:
        # if file hasn't been backed up before, True by default
        return True


def backup(f, backup_loc):
    # check what f is:
    # if f is a file, just do copy(f, os.path.join(f, backup_loc)
    # otherwise, os.walk over the directory and move each of the files.
    if os.path.isfile(f):
        copy(f, os.path.join(f, backup_loc))
    else:
        dir_tree = os.walk(f)
        
        


def backup_configs(configs, backup_loc):
    updated_cfgs = [ f for f in configs 
                     if newer_version(f, backup_loc + os.path.split(f)[1]) ] # if this doesn't work try adding os.path.isfile(f) as another condition
    # map(copyfile/dir/whatever, config_files_that_have_been_updated)
    # TODO handle new directories being added to CONFIG_FILES
    print(updated_cfgs)


def main():
    # TODO: move lambda into get_home function
    cfgs = map(get_home, CONFIG_FILES)
    bkup = map(get_home, BACKUP_FOLDER)
    backup_configs(cfgs, bkup)


if __name__ == '__main__':
    main()
