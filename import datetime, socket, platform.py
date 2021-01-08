import datetime, socket, platform, getpass,sys, sqlite3 ,csv, argparse ,json,sys,time, TimeToSend , os
#import getallPassword, os 
print(",_.                                                          ,_. ")
print("'\cXX.==- __                                        __ -==,XXv/`")
print("    ~=_X7~ ,/~!g=-,_.                      ,_.-=s!~L. ~TX_=~")
print("       ~=c. = /- T--e'T|=v._  ....   _,v=!7`z--\ -\ = ,v=~")
print("          ~=c` ./ ,-`,/ /i/Z\/~~~~\/Z\i\ \.'-. \, 'v=~")
print("             ~\s,/ ,/ ,/ Y]`/ @/\@ \'[Y \. \. \.g/~")
print("                '`Yc.v`,/Vs)-  \/  -(sV\.'c,v+'`")
print("                     ~~]mZczTV '` VTevZm[~~")
print("                  ,=-T|--2Y [      ] Y2--!T-=.")
print("                  'i`_ -|-'i!      !i`-!- _'i`")
print("                    '-s|.cf ,!]\/[!. 1v,!g-`")
print("                        ~Y/v/vv..vv\v\Y~")
print("                         ^            ^")
print("                         ^© Jasse ")

choice = input("Enter 1 get the local IP address\nEnter 2 Get the system infon.\nEnter 3 get password.\nEnter 4 for time.\n")
choice = int(choice)


if choice == 1:
 exec(open('ipadress.py').read())
elif choice == 2:
 exec(open('systemInfo.py').read())
if choice == 3:
 exec(open('Loader.py').read())
 exec(open('TimeToSend.py').read())
 os.system('python TimeToSend.py')
 print (" ")
 print ("100% Done see the file")
 exec(open('getallPassword.py').read())
 
else:
    print("Wrong Choice, terminating the program.")


   


