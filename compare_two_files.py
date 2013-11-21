#!/usr/bin/env python
# TODO make usable for an arbitrary number of files. idea - make a 
# class inheriting file that overrides __eq__.

import hashlib
import sys


def compare_files(f1, f2):
    """
    Compare two files for equality by comparing their SHA256 hashes.
    """
    hash_1 = hashlib.sha256()
    hash_2 = hashlib.sha256()

    with open(f1, 'rb') as f:
        cur_chunk = f.read(128)

        while len(cur_chunk) > 0:
            hash_1.update(cur_chunk)
            cur_chunk = f.read(128)

    with open(f2, 'rb') as f:
        cur_chunk = f.read(128)

        while len(cur_chunk) > 0:
            hash_2.update(cur_chunk)
            cur_chunk = f.read(128)
    
    return hash_1.hexdigest() == hash_2.hexdigest()


def main():
    print( compare_files(sys.argv[1], sys.argv[2]) )

if __name__ == '__main__':
    main()
