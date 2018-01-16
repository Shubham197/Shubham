import os

os.system('cls')
print('ARE YOU SURE ?....\n')
def a():
    v=int(input('yes(1) or no(0)\n'))
    if v<2:
        if v==1:
            return(0)
        if v==0:
            os.system('123.py')
    else:
        print('fail input\n',sep="\n")
        a()

a()
        

    

