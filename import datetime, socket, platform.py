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
global loadingbar 
toolbar_width = 40
choice = input("Enter 1 get the local IP address\nEnter 2 Get the system infon.\nEnter 3 get password.\nEnter 4 for time.\n")
choice = int(choice)
meny = input("Eneter 1 get all the password.\nEnter 2 for encryptor the files ")
meny = int(meny)

def loadingbar():
 sys.stdout.write("%s\n" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("#")
    sys.stdout.flush()

if choice == 1:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)

elif choice == 2:
 print("="*40, "System Information", "="*40)
 uname = platform.uname()
 print(f"System: {uname.system}")
 print(f"Node Name: {uname.node}")
 print(f"Release: {uname.release}")
 print(f"Version: {uname.version}")
 print(f"Machine: {uname.machine}")
 print(f"Processor: {uname.processor}")  

elif choice == 3:
 if meny == 1:
  loadingbar()
  #pwsfile()
  exec(open('TimeToSend.py').read())
  os.system('python TimeToSend.py')
  print (" ")
  print ("100% Done see the file")
  os.system('python getallPassword.py')
 elif  meny == 2:
  print ("hello world")
 elif  meny == 3:
  print ("hello world")
 elif  meny == 4:
  print ("hello world")
 else:
        print("Wrong Choice, terminating the program.")
else:
    print("Wrong Choice, terminating the program.")


   


