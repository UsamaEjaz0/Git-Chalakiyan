import time

import subprocess


for i in range(200000):
    f = open("Chalo_Jee.txt", "a")
    f.write("Kacha Paparr, Pakka Papar, ")
    f.close()
    time.sleep(2)
    subprocess.call([r'C:\Users\uejaz\Desktop\Projects\Git_Chalakiyan\AutomateGit.bat'])
