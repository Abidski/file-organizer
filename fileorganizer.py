import os, time, shutil
from tkinter import messagebox 

#takes a list of files in the download directory
original = os.listdir(r"C:\Users\Abid\Downloads")


def checkfolder(name,element):
    if (element.find(name) != -1):
                try:
                    shutil.move("C:\\Users\\Abid\\Downloads\\" + element ,  "C:\\Users\\Abid\\Desktop\\" + name)
                except shutil.Error:
                    messagebox.showinfo("Duplicate File", "Warning the file you just downloaded already exits, the file will be placed in the Trash folder")
                    shutil.move("C:\\Users\\Abid\\Downloads\\" + element ,  r"C:\Users\Abid\Desktop\Recycle Bin")


#checks to see if new files is added by comparing files in the old directory in comparison to the new directory
while True:
    for element in original:
        checkfolder("352",element)
        checkfolder("348",element)
    for element2 in original:
        checkfolder("pdf",element2)
        
#    time.sleep(10)
 #   print ("test")
  #  new = os.listdir(r"C:\Users\Abid\Downloads")
   # for element in new:
    #    if element not in original:
     #       checkfolder("352",element)
      #      checkfolder("348",element)
       #     checkfolder("Assignment",element)
        #    checkfolder(".pdf",element)
            
         
    original=os.listdir(r"C:\Users\Abid\Downloads")
