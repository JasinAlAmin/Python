import datetime,time, sys
toolbar_width = 40

def loadingbar():
 sys.stdout.write("%s\n" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("#")
    sys.stdout.flush()