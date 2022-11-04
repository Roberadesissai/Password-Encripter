import os
import sys
import key
import time
import json
import getpass
from stringcolor import *


def read_file():
    
    def progressbar(it, prefix="", size=60, out=sys.stdout): 
        count = len(it)
        def show(j):
            x = int(size*j/count)
            print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                    end='/r', file=out, flush=True)
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        print("/n", flush=True, file=out)
    file_name=input("File name: ")
    pattern1=file_name.split('.')
    for root, dirs, files in os.walk(r'C:/'):
        for name in files:
            if name == file_name: 
                result=(os.path.abspath(os.path.join(root,name))) 
                check=name         
    try:
        pattern=check.split('.')
        if pattern1[1]==pattern[1]:
            try:
                if 'txt' in pattern:
                    with open(result) as f:
                        pwdd = f.read()
                    pwd=key.Key(pwdd)
                    pwd.lock()

                elif 'json' in pattern:

                    with open(result) as f:
                        pwdd=json.load(f)
                    pwd=key.Key(pwdd)
                    pwd.unlock()

            except: 
                print(cs('The file is empity', "#ff0000"))
        
    except:
        print(cs('Unknown file type', "#ff0000"))
        print(cs('Input most be .json or .txt file', "#ff0000"))





read_file()  







