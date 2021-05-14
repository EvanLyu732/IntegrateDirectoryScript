import sys
import os
import argparse
from shutil import copyfile

# start with directory A copy alls its file to a given directory
# and puts its content into map, After that, go to the second directory
# and check if its second directory contains same file
# if is then copy, if not then continue.


def fircopyfile(firdir: str, ndir: str) -> map:
    firfilesmap = {}

    for _, subdir, subfiles in os.walk(firdir):
        for dir in subdir:
            path = os.path.join(ndir, dir)
            os.mkdir(path)
            for file in subfiles:
                # temp list store files
                templist = set()
                templist.add(file)
                firfilesmap[dir] = templist

                firfpath = os.path.join(firdir, dir, file)
                ndirfpath = os.path.join(ndir, dir, file)
                copyfile(firfpath, ndirfpath)

    print("---copy files for dir: %s success!---" % firdir)
    return firfilesmap


def seccopyFile(secdir: str, ndir: str, filesset: set):
    for _, subdir, subfiles in os.walk(secdir):
        for dir in subdir:
            firfilesset = filesset.get(dir)
            for file in subfiles:
                # if file is contained in list, then continue, else copy
                if file in firfilesset:
                    continue
                else:
                    secfpath = os.path.join(secdir, dir, file)
                    ndirfpath = os.path.join(ndir, dir, file)
                    copyfile(secfpath, ndirfpath)

    print("---copy files for dir: %s success!---" % secdir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("firdir", help="first directory absolute root path")
    parser.add_argument("secdir", help="second directory absolute root path")
    parser.add_argument("newdir", help="new directory absolute root path")
    args = parser.parse_args()

    # firdir = sys.argv[1]
    # secdir = sys.argv[2]
    # newdir = sys.argv[3]
    firdir = args.firdir
    secdir = args.secdir
    newdir = args.newdir

    os.makedirs(newdir)

    # copy firdir files to newdir
    firmap = fircopyfile(firdir, newdir)
    seccopyFile(secdir, newdir, firmap)
