#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Badly converts an image and resizes it
Written whilst trying to look after a child.

I'm not handling all the cases I should because I simply can't be bothered
"""
import glob
import os

from PIL import Image

size = 500, 500

def get_files(types=['*.jpg', '*.jpeg']):
    """
    """

    files = []
    for e in types:
        files += glob.glob('./'+e)

    return files

def convert_images():
    """
    """

    for i in get_files():
        try:
            im = Image.open(i)
            file_name, _ = os.path.splitext(i)
            im.thumbnail(size, Image.Resampling.LANCZOS)
            im.save('{}.png'.format(file_name.lower()), optimize=True)
            delete_stuff(i)
        except (ValueError, OSError) as e:
            print("yeah mate, you can't convert that image: %s" % e)

def delete_stuff(file):
    """
    """

    try:
        os.remove(file)
    except OSError as e:
        print("can't find %s to delete: %s" % (e.filename, e.strerror))

if __name__ == '__main__':
    convert_images()