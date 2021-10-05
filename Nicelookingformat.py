import itertools
import threading
import time
import sys
done=False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def start_animation():
    global done
    t=threading.Thread(target=animate)
    done=False
    t.start()

def end_animation():
    global done
    time.sleep(10)
    done=True
    

def printLine(str,len):
    p=""
    for i in range(len):
        p=p+str
    print()
    print(p)
    print()

