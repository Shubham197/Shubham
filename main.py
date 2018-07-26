print("1. Download The Song")
print("2. Download The Video")
print("3. Enter The URL And Download Video")
print("4. Terminate Application\n")

choice = int(input("Enter Your Choice :\n"))
print(" ")
if choice==1:
    os.system('mp3.py')
    
if choice==2:
    os.system('video.py')

if choice==3:
    os.system('url.py')

if choice==4:
    os.system('terminate.py')
