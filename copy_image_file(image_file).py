import os

def copy_image_file(image_file):
    with open(image_file, mode='rb') as f:
        source = f.read()

        name, ext = os.path.splitext(image_file)
        new_name = name + '_copy' + ext

        with open(new_name, mode='wb') as copy:
            copy.write(source)