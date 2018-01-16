import urllib.request as req 
import os
import re
from bs4 import BeautifulSoup
from subprocess import call # module to create subprogram instide our program

os.system('cls')
os.system('color e0')
os.system('title URL')

print("1. Current Choice ")
print("2. Change Choice\n")

choice=int(input("Enter Your choice :\n"))
print(" ")
if 0<choice<3:
    if choice==1:
        choice=input("Please Enter The Download Path :\n").replace("\ ","/")
        print(" ")
        os.chdir(choice)

        url=input("Enter URL :\n")
        res=req.urlopen(url)
        data=res.read().decode("utf-8")
        #print(data)
        match=re.findall(r'<title>(.*?)</title',data)
        
        a=match[0]
        v=a[:-10]
        
        folder = v
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        
        print("Started Download\n")
        call("youtube-dl "+url)
        with open("Videos Details.txt", "a") as myfile:
            myfile.write(v)
            myfile.write("\n")
            myfile.write("Video Url\n")
            myfile.write(url)           
        myfile.close()
        print("End Download\n")
        choice=input("Enter Any Key\n")



    if choice==2:
        print("1. Song Choice ")
        print("2. Video Choice")
        print("3. Terminated Application\n")

        choice=int(input("Enter Your choice :\n"))
        print(" ")
        if 0<choice<4:
            if choice==1:
                os.system('mp3.py')

            if choice==2:
                os.system('video.py')
            else:
              os.system('terminate.py')
           
else:
    print("Wrong Input")

