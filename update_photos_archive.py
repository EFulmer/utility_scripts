import sys
import tarfile

# tarfile.open(mode='w:gz') for gzip
# use fileobj kwarg if there's an already-opened file object
# otherwise use name kwarg

PHOTO_FOLDER = '/Users/eric/Dropbox/Camera Uploads'
OUTPUT_FOLDER = '/Users/eric/Dropbox/Camera Uploads'
ARCHIVE_NAME = ''
IMAGE_FILE_EXTS = ('.bmp', '.gif', '.jpeg', '.jpg', '.png', )

def is_image_file(f):
    return os.path.splitext(f)[1] in IMAGE_FILE_EXTS

def get_image_files(folder):
    # get list of files in folder
    # loop over list of files, add each image file to list of img files
    fldr_contents = os.listdir(path=folder)
    img_files = []
    for f in fldr_contents:
        if is_image_file(f):
            img_files.append(f)
    # open up archive file
    # check for existence of any of these image files in the archive file (how?)
    # add new files to archive file


def archive_image_files(img_files, archive_name, mode='w:gz'):
    with tarfile.open(archive_name, mode) as tar:
        for img in img_files:
            tar.add(img) 


def main():
    try:
        img_folder, archive_name = sys.argv[1:]
        
    except ValueError as v:
        print('Expected image folder and archive name as args, '
                'got {0}'.format(v.args()))


if __name__ == '__main__':
    main()
