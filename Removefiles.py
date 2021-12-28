import os
import shutil
import time

path = input("Enter the path of the old files that needs deletion: ")
days = 17

seconds = time.time()-(days*24*60*60)
print(seconds)

if os.path.exists(path):
    print("Path Exists")
    listFiles = os.listdir(path)

    print(listFiles)

    final = os.path.join(path,"MatWork.pdf")
    print(final)


    ctime = os.stat(final).st_ctime
    print(ctime)

    if ctime > seconds:
        os.remove(final)
        print("Files removed successfully")





else:
    print("Error! Path not found")



    


