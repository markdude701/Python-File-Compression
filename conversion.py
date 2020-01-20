import tarfile
import os
import public as public



def openTar():
    tar = tarfile.open("sample.tar.gz")
    tar.extractall()
    tar.close()
    print(tar)

def resetArchive():
    def reset(tarinfo):
        tarinfo.uid = tarinfo.gid = 0
        tarinfo.uname = tarinfo.gname = "root"
        return tarinfo
    tar = tarfile.open("sample.tar.gz", "w:gz")
    tar.add("conversion.py", filter=reset)
    tar.close()

def readAchieve():
    tar = tarfile.open("sample.tar.gz", "r:gz")
    for tarinfo in tar:
        print
        tarinfo.name, "is", tarinfo.size, "bytes in size and is",
        if tarinfo.isreg():
            print
            "a regular file."
        elif tarinfo.isdir():
            print
            "a directory."
        else:
            print
            "something else."
    tar.close()


resetArchive()
openTar()
readAchieve()