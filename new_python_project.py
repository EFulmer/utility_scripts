import os
import shutil
import subprocess
import sys

def make_readme(proj_name):
    """Make a basic README.md in folder proj_name."""
    subprocess.call(['touch', proj_name + 'README.md'])

def make_setup(proj_name):
    """Make a basic setup.py file in the new project directory proj_name."""
    shutilcopyfile('~/Projects/utility_scripts/setup.py', 
                   proj_name + 'setup.py')

def main():
    # loop through all given arg names; for each, make a project skeletin 
    # (top level folder, src folder, doc folder, tests folder, __init__.py)
    # advanced/for later: set up a git repo and virtualenv?
    for arg in sys.argv[1:]:
        root = './' + arg + '/'
        os.makedirs(root)
        os.makedirs(root + arg)
        os.makedirs(root + 'tests')
        os.makedirs(root + 'docs')
        make_readme(root)
        make_setup(root)

if __name__ == '__main__':
    main()
