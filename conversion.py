import tarfile
import os
import glob

originalSize = 0
tarSize = 0
targzSize = 0
file_names = ['archive.tar','archive.tar.gz']

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
    for file in glob.glob("*"):
        files.append(file)
        file_info = os.stat(file)
        originalSize = originalSize + int(file_info.st_size)
    print("Collected Directory items: " + str(glob.glob("*")))
    return files

def createTar(files):
    global tarSize
    global file_names
    tar = tarfile.open(file_names[0], "w")
    for name in files:
        tar.add(name)
    tar.close()
    print("Created archive.tar")

def openTar():
    tar = tarfile.open(file_names[1])
    tar.extractall()
    tar.close()
    print(tar)

'''Convert tar to tar.gz'''
def resetArchive(files):
    global targzSize
    global file_names
    def reset(tarinfo):
        tarinfo.uid = tarinfo.gid = 0
        tarinfo.uname = tarinfo.gname = "root"
        return tarinfo

    tar = tarfile.open(file_names[1], "w:gz")
    '''tar.add("conversion.py", filter=reset)'''
    for name in files:
        tar.add(name, filter=reset)
        file_info = os.stat(name)
        targzSize = targzSize + file_info.st_size
    tar.close()
    print("Created archive.tar.gz")

'''Read archive and create tar.gz '''
def readAchieve():
    tar = tarfile.open(file_names[1], "r:gz")
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
def deleteTar():
    global file_names
    for file in file_names:
        if os.path.exists(file):
            os.remove(file)
            print("Deleted old " + str(file))

    '''
    if os.path.exists("archive.tar"):
        os.remove("archive.tar")
        print("Deleted old archive.tar")
    if os.path.exists("archive.tar.gz"):
        os.remove("archive.tar.gz")
        print("Deleted old archive.tar.gz")
    '''
    #https://www.w3schools.com/python/python_file_remove.asp

def results():
    print("Compression Complete!")
    print("Original Directory File Size: " + convertSize(originalSize))
    file_info = os.stat(file_names[0])
    tarSize = file_info.st_size
    file_info = os.stat(file_names[1])
    targzSize = file_info.st_size

    size = [tarSize, targzSize]
    ratio = [(tarSize / originalSize) * 100 , (targzSize / originalSize) * 100]
    start = ""

    for i in range(0,len(size)):
        if i == 0:
            start = "Tar File Size: "
        if i == 1:
            start = "Tar.gz File Size: "
        print(start + convertSize(size[i]) + " - Compression : " + str(ratio[i]) + " % ")


'''Testing Function'''
def test():
    print('')


def main():
    #Collect init directory
    files = collectFiles()

    #Check for and delete old archives to stop doubling additions
    deleteTar()

    #Recreate dir without tar/tar.gz
    files = collectFiles()

    #Create tar file from files
    createTar(files)

    #create tar.gz from files
    resetArchive(files)

    #Print Results
    results()


    # _______________ DEBUG FUNCTIONS __________________
    #readAchieve()

    '''createTar()
    resetArchive()
    openTar()
    readAchieve()'''
    test()

main()



