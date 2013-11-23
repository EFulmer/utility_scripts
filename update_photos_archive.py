import os
import sys
import tarfile


IMAGE_DIR = '/Users/eric/Dropbox/Camera Uploads'
ARCHIVE_FILE = '/Users/eric/Dropbox/Camera Uploads/photo_archive.tar.gz'
IMAGE_FILE_EXTS = ('.bmp', '.gif', '.jpeg', '.jpg', '.png', )


def is_image_file(f):
    """True if f is an image file. Checked by investigating f's extension."""
    return os.path.splitext(f)[1] in IMAGE_FILE_EXTS


def get_image_files(folder=IMAGE_DIR):
    """Return a list of all image files in folder."""
    fldr_contents = os.listdir(path=folder)
    img_files = [ os.path.join(folder, f) for f in os.listdir(path=folder) 
                  if is_image_file(f) ]
    return img_files


def archive_image_files(img_files, archive_name=ARCHIVE_FILE, mode='w:gz' 
                        delete_after_archive=False):
    # TODO handle existing archives; either rename archive_name if it
    # exists or somehow make a new archive and merge it with the 
    # existing one.
    with tarfile.open(archive_name, mode) as tar:
        for img in img_files: 
            tar.add(img)
            if delete_after_archive:
                os.remove(img)


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
