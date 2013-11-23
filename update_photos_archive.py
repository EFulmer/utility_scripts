import os
import sys
import tarfile


IMAGE_DIR = '/Users/eric/Dropbox/Camera Uploads'
ARCHIVE_FILE = '/Users/eric/Dropbox/Camera Uploads/photo_archive.tar.gz'
IMAGE_FILE_EXTS = ('.bmp', '.gif', '.jpeg', '.jpg', '.png', )


def is_image_file(f):
    return os.path.splitext(f)[1] in IMAGE_FILE_EXTS


def get_image_files(folder=IMAGE_DIR):
    fldr_contents = os.listdir(path=folder)
    img_files = []
    for f in fldr_contents:
        if is_image_file(f):
            img_files.append(os.path.join(folder, f))
    return img_files
    # open up archive file
    # check for existence of any of these image files in the archive file (how?)
    # add new files to archive file


def archive_image_files(img_files, archive_name=ARCHIVE_FILE, mode='w:gz'):
    with tarfile.open(archive_name, mode) as tar:
        for img in img_files: 
            tar.add(img)


def main():
    if len(sys.argv) == 1:
        images = get_image_files()
        archive_image_files(images)
    else:
        try:
            img_folder, archive_name = sys.argv[1:]
            images = get_image_files(img_folder)
            archive_image_files(images, archive_name)
        except ValueError as v:
            print('Expected image folder and archive name as args, '
                'got {0}'.format(v.args()))


if __name__ == '__main__':
    main()
