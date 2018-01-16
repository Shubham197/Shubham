import urllib.request as req 
import os
import re

from bs4 import BeautifulSoup
from subprocess import call # module to create subprogram instide our program


os.system('cls')
os.system('color e')
os.system('title Videos')

print("1. Current Choice ")
print("2. Change Choice\n")

choice=int(input("Enter Your choice :\n"))
print(" ")
if 0<choice<3:
    if choice==1:
        choice=input("Please Enter The Download Path :\n").replace("\ ","/")
        os.chdir(choice)
        query=input("\nEnter The Video Name :\n").replace(" ","%20")

        res= req.urlopen(
            "https://www.youtube.com/results?search_query="+query)

        data = res.read().decode("utf-8")

        soup = BeautifulSoup(data,"html.parser")

        hyper = soup.find_all("a",class_="yt-uix-tile-link")

        links = []

        print(" ")
        for index,i in enumerate(hyper):
            print(index+1,i.get("title"))
            links.append(i.get("href"))

     
        choice=int(input("\nEnter Your Choice :\n"))
        videourl = "https://www.youtube.com"+links[choice-1]
        res=req.urlopen(videourl)
        data=res.read().decode("utf-8")

        match=re.findall(r'<title>(.*?)</title',data)
        a=match[0]
        v=a[:-10]
        
        print(v)
        folder = v
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        
        print("Started Download\n")
        
        call("youtube-dl "+videourl)
        with open("Videos Details.txt", "a") as myfile:
            myfile.write(v)
            myfile.write("\n")
            myfile.write("Video Url\n")
            myfile.write(videourl)          
        myfile.close()
        
        print("End Download\n")
        choice=input("Enter Any Key\n")

    if choice==2:
        print("1. Song Choice ")
        print("2. Url Choice")
        print("3. Terminated Application\n")

        choice=int(input("Enter Your choice :\n"))

        if 0<choice<4:
            if choice==1:
                os.system('mp3.py')

            if choice==2:
                os.system('url.py')

            if choice==3:
                print(" ")
                os.system('terminate.py')
        
           
else:
    print("Wrong Input")

