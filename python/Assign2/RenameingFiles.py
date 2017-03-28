#renaming many files in a folder
import os

def rename_files():
    #get file names from folder
    fileList=os.listdir(r"C:\Users\Dell\Desktop\python\Assign2\prank") #letter 'r' before path implies raw path i.e dont interpret \ in other way
    #prints all the file names
    print(fileList)
    os.chdir(r"C:\Users\Dell\Desktop\python\Assign2\prank")
    #for each file, rename filename
    for fileName in fileList:
        #renaming the files i.e removing numbers in filename
        os.rename(fileName,fileName.translate(None,"0123456789"))
rename_files()
