import urllib.request as req
import ssl
import re
import os
from bs4 import BeautifulSoup
from subprocess import call # module to create subprogram instide our program
context = ssl._create_unverified_context()

os.system('cls')
os.system('color e')
os.system('title Audio')

print("1. Current Choice ")
print("2. Change Choice\n")

choice=int(input("Enter Your choice :\n"))
print(" ")
if 0<choice<3:
    if choice==1:
        ch=input("Please Enter The Download Path :\n").replace("\ ","/")
        print(" ")
        os.chdir(ch)
        j=1
        i=0

        #n=int(input("Enter Data:\n"))
        u="https://pagalworld.me/category/11598/Latest%20Bollywood%20Hindi%20Mp3%20Songs%20-%202017/"
        v=".html"
                #main

        def abc(j):
            print("\n\tPAGE"+" ",j)
            s=u+str(j)+v
            res = req.urlopen(s,context=context)

            data = res.read().decode("utf-8")
            match = re.finditer(r'https://pagalworld.info/files/\d+/((.)+?).html',data)
        
            movielist = [] # link of all songs

            for i,value in enumerate(match):
                movielist.append(value.group(0).replace(" ","%20"))
                print(i+1,value.group(1)) # page 1 data

            print(" ")
            print("1. Next Page")
            print("2. Page Details")
            print("3. Download Song")
            print("4. Exit Page")

            if j>1:
                n=6
                print("5. Previse Page\n")
            else:
                n=5
            choice=int(input("\nEnter Above Choice :\n"))

            if choice<0 or choice>n:
                print("Wrong Choice")

            if choice==1 :
                j=j+1
                abc(j)

            if choice==2:
                with open("Page Details.txt", "a") as myfile:
                    myfile.write('Dowloading Web Side Is PAGAL-WORLD')
                    myfile.write('Page Link Is\n')
                    myfile.write(s)
                myfile.close()
                print("Done!")


            if choice==3:
                dow(j)

            if choice==4:
                choice = input("\nEnter The Any Key\n")
                #return(0)
    

            if choice==5:
                if j>1:
                    j=j-1
                    abc(j)

                else :
                    print("Wrong Input")

        def dow(j):
            res = req.urlopen(u+str(j)+v,context=context)
            data = res.read().decode("utf-8")
            match = re.finditer(r'https://pagalworld.info/files/\d+/((.)+?).html',
                   data)

            movielist = [] # link of all songs
    
            for i,value in enumerate(match):
                movielist.append(value.group(0).replace(" ","%20"))
    
            Download=int(input("\nEnter Song Number We Want Download :\n"))
            res = req.urlopen(movielist[Download-1],context=context)

            b=movielist[Download-1].replace("%20"," ")            
            c=b[0:-9]
            d=c[36:]
            print(d)
            folder = d
            if not os.path.exists(folder):
                os.mkdir(d)
            os.chdir(folder) 

            data = res.read().decode("utf-8")
            match = re.finditer(r'https://pagalworld.info/filedownload/\d+/\d+/((.)+?).html',data)
            songlist = []  # list of links
            songname = []  # song name - for file name of downloaded file.
            print("\n\t PAGE 1\n")
            for i,value in enumerate(match):
                songlist.append(value.group(0).replace(" ","%20"))
                songname.append(value.group(1))
                print(i+1,value.group(1)) # print song name

            print("\nDon't Choice Zip File\n")
            print("1. Go To Next Page")
            print("2. Current Page")

            c=int(input("\nEnter Above Choice :\n"))

            if c==1:
                print("\n\t PAGE 2\n")
                res = req.urlopen(movielist[Download-1].replace(".html","/position/2.html"),context=context)
                data = res.read().decode("utf-8")
                match = re.finditer(r'https://pagalworld.info/filedownload/\d+/\d+/((.)+?).html',data)

                songlist = []  # list of links
                songname = []  # song name - for file name of downloaded file.

                for i,value in enumerate(match):
                    songlist.append(value.group(0).replace(" ","%20"))
                    songname.append(value.group(1))
                    print(i+1,value.group(1)) # print song name

                choice = int(input("\nEnter Song Number We Want Download :\n"))
                res = req.urlopen(songlist[choice-1])
                data = res.read().decode("utf-8")
                match = re.search(r'downpwnew.com/upload_file/\d+/\d+/((.)+?).mp3',data)

                downloadlink = match.group(0).replace(" ","%20")
                
                with open("Song Details.txt", "a") as myfile:
                    myfile.write(d)
                    myfile.write("\n")
                    myfile.write(movielist[Download-1].replace(".html","/position/2.html"))
                    myfile.write('songname')
                    myfile.write("\n")
                    myfile.write(songlist[choice-1])
                    myfile.write('\n Download Url\n')
                    myfile.write(downloadlink)
                myfile.close()
                print("\nDownload started\n")

                res=req.urlretrieve("https://"+downloadlink,songname[choice-1]+".mp3")
                print("Done!")

            if c==2:
                choice = int(input("\nEnter Song Number We Want Download :\n"))
                res = req.urlopen(songlist[choice-1])
                data = res.read().decode("utf-8")
                match = re.search(r'downpwnew.com/upload_file/\d+/\d+/((.)+?).mp3',data)

                downloadlink = match.group(0).replace(" ","%20")
                print(downloadlink)
                print("\nDownload started\n")
                with open("Song Details.txt", "a") as myfile:
                    myfile.write(d)
                    myfile.write("\n")
                    myfile.write(movielist[Download-1].replace(".html","/position/2.html"))
                    myfile.write('songname')
                    myfile.write("\n")
                    myfile.write(songlist[choice-1])
                    myfile.write('\n Download Url\n')
                    myfile.write(downloadlink)
                myfile.close()
                res=req.urlretrieve("https://"+downloadlink,songname[choice-1]+".mp3")
                print(res)
                print("Done!")


       
#start


    
    if choice==2:
        print("1. Video Choice ")
        print("2. Url Choice")
        print("3. Terminated Application\n")

        choice=int(input("Enter Above Choice :\n"))
        print(" ")

        if 0<choice<4:
            if choice==1:
                os.system('Video.py')

            if choice==2:
                os.system('url.py')

            else:
                os.system('terminate.py')
           
else:
    print("Wrong Input")


abc(j)   

