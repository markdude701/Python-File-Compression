import tarfile
import os
import glob
import public as public

originalSize = 0
tarSize = 0
targzSize = 0

#Converts bytes to kb, mb, gb, etc
def convertSize(number):
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if number < 1024:
            return "%3.1f %s" % (number , x)
        number /= 1024
#Reference: https://stackoverflow.com/a/39988702/11571748

def collectFiles():
    global originalSize
    files = []
    fileSize = 0
    for file in glob.glob("*"):
        files.append(file)
        file_info = os.stat(file)
        originalSize = originalSize + file_info.st_size
    # print(convertSize(originalSize))
    return files



def createTar(files):
    global tarSize
    tar = tarfile.open("archive.tar", "w")
    for name in files:
        tar.add(name)
    tar.close()
    print("Created archive.tar")

def openTar():
    tar = tarfile.open("archive.tar.gz")
    tar.extractall()
    tar.close()
    print(tar)

'''Convert tar to tar.gz'''
def resetArchive(files):
    global targzSize
    def reset(tarinfo):
        tarinfo.uid = tarinfo.gid = 0
        tarinfo.uname = tarinfo.gname = "root"
        return tarinfo

    tar = tarfile.open("archive.tar.gz", "w:gz")
    '''tar.add("conversion.py", filter=reset)'''
    for name in files:
        tar.add(name, filter=reset)
        file_info = os.stat(name)
        targzSize = targzSize + file_info.st_size
    tar.close()
    print("Created archive.tar.gz")

'''Read archive and create tar.gz '''
def readAchieve():
    tar = tarfile.open("archive.tar.gz", "r:gz")
    for tarinfo in tar:
        print
        tarinfo.name, "is", tarinfo.size, "bytes in size and is",
        if tarinfo.isreg():
            print(":a regular file.")
        elif tarinfo.isdir():
            print("a directory.")
        else:
            print("something else.")
    tar.close()

'''Check for and delete old archives to stop doubling additions '''
def deleteTar(files):
    if os.path.exists("archive.tar"):
        os.remove("archive.tar")
        print("Deleted old archive.tar")
    if os.path.exists("archive.tar.gz"):
        os.remove("archive.tar.gz")
        print("Deleted old archive.tar.gz")

    '''
    for singleFile in files:
        if singleFile == "archive.tar":
            os.remove("archive.tar")
            print("Deleted old archive.tar")
        elif singleFile == "archive.tar.gz":
            os.remove("archive.tar.gz")
            print("Deleted old archive.tar.gz")
    '''
    #https://www.w3schools.com/python/python_file_remove.asp

def results():
    print("Compression Complete!")
    print("Original Directory File Size: " + convertSize(originalSize))
    file_info = os.stat('archive.tar')
    tarSize = file_info.st_size
    ratio = (tarSize / originalSize) * 100

    print("Tar File Size: " + convertSize(tarSize) + " - Compression : " + str(ratio) + " % ")
    file_info = os.stat('archive.tar.gz')
    targzSize = file_info.st_size
    ratio = (targzSize / originalSize) * 100
    print("Tar.gz File Size: " + convertSize(targzSize) + " - Compression : " + str(ratio) + " % ")


'''Testing Function'''
def test():
    print(glob.glob("*"))


def main():
    files = collectFiles()
    '''Get all files in current directory'''

    deleteTar(files)
    '''Check for and delete old archives to stop doubling additions '''

    files = collectFiles()
    '''Recollect the files'''

    createTar(files)
    resetArchive(files)
    results()
    #readAchieve()

    '''createTar()
    resetArchive()
    openTar()
    readAchieve()'''
    test()

main()



