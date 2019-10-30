
import shutil
import os
from os import path

#shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
#shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext

#print(os.path.realpath(__file__))

def main():

    # make duplicate of an existing file
    if path.exists("Copyfile_Src-Des.py"):

    # Get path from the current directory
        src = path.realpath("Copyfile_Src-Des.py")

    # Separate the path form the filter
    head,tail = path.split(src)
    print("File location => " + head)
    print("Filename => " + tail)

    # Let's make a backup copy by appending "bak" to name
    dst = src + ".bak"

    # Use the shell to make a copy of the file
    shutil.copy(src,dst)

    # Copy over permission, modification
    shutil.copystat(src,dst)


if __name__ == "__main__":
    main()

