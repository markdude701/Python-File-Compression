import glob
import os
import tarfile
import bz2

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
    # https://docs.python.org/3/library/tarfile.html

'''Check for and delete old archives to stop doubling additions '''
def deleteTar():
    global file_names
    for file in file_names:
        if os.path.exists(file):
            os.remove(file)
            print("Deleted old " + str(file))
    #https://www.w3schools.com/python/python_file_remove.asp

def results():
    #global targzSize, tarSize, originalSize
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

'''Read archive tar.gz - NOT CURRENTLY USED  '''
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
    #https://docs.python.org/3/library/tarfile.html



'''Testing Function'''
def test(files):
    print('')
    '''
    data = files

    comp = bz2.BZ2Compressor()
    out = b""


    for chunk in range(0 , len(data)):
        # Provide data to the compressor object
        out = out + comp.compress((data[chunk]).encode())
    # Finish the compression process.  Call this once you have
    # finished providing data to the compressor.
    out = out + comp.flush()

    with bz2.open("myfile.bz2", "wb") as f:
        # Write compressed data to file

        unused = f.write(out)

    with bz2.open("myfile.bz2", "rb") as f:
        # Decompress data from file
        content = f.read()

    if (content == data):
        print("BZ COMPLETE SUCCESS")
    else:
        print("BZ FAIL")
        '''


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

    test(files)

main()



