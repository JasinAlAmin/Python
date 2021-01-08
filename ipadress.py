import datetime, socket, platform, getpass,sys, sqlite3 ,csv, argparse ,json,sys,time, TimeToSend , os


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)
print("")