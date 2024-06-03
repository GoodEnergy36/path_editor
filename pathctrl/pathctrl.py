#!/usr/bin/env python3


import subprocess
import os
import re

env = os.environ.copy()
env["PYTHON_EXECUTED"] = "true"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True


def finalise(my_list, deleted_list):
    deleted = 0
    for i in deleted_list:
        del my_list[i - deleted]
        deleted += 1
    ret = ':'.join(my_list)
    with open("path.txt", "w") as f:
        f.write(ret.strip())
    f.close()


def main():
    my_list = os.environ.get('PATH').strip().split(':')
    deleted_list = []
    OOR_ERROR, NDR_ERROR, INV_ERROR = 0, 0, 0
    while 1:
        list_len = len(my_list)
        spacing = len(str(list_len-1))
        clear_screen()
        print(  
            "This is the $PATH editing app" +
            "\n\n'>>' represents paths that you want to keep" +
            "\n'##' represents paths that you want to remove" +
            "\n\nSelect the number of the path you'd to alter\n"
            )
        for item in enumerate(my_list):
            if item[0] in deleted_list:
                signif = "##"
            else:
                signif = ">>"
            print(f"{signif} {item[0]:<{spacing}} {item[1]}")
        
        print(
            "\nOther functions include:" +
            "\n'd _directory' - add _directory to path" +
            "\n'f' - finalise results" +
            "\n'a' - abort\n"
            )

        if OOR_ERROR:
            print("ERROR: The last number you entered was out of range\n")
            OOR_ERROR = 0
        
        if NDR_ERROR:
            print("ERROR: The last directory you entered was invalid\n")
            NDR_ERROR = 0
        
        if INV_ERROR:
            print("ERROR: The last command you entered was invalid\n")
            INV_ERROR = 0

        inp = input("Please enter something: ")

        if is_int(inp):
            val = int(inp)
            if val < 0 or val >= list_len:
                OOR_ERROR = 1
                continue
            if val in deleted_list:
                deleted_list.remove(val)
            else:
                deleted_list.append(val)
        elif inp == 'a':
            exit(1)
        elif inp == 'f':
            finalise(my_list, deleted_list)
            return
        elif inp[0] == 'd':
            print("hi")
            dir_name = inp[2:]
            print(dir_name)
            if os.path.isdir(dir_name) and re.match(r"^(/[^/]+)+/?$", dir_name):
                my_list.append(dir_name)
            else:
                NDR_ERROR = 1
        else:
            INV_ERROR = 1


if __name__ == '__main__':
    main()
    subprocess.run("pathctrl.sh", env=env)