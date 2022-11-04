
import sys
import time
import json
import string
import colorterminal
from stringcolor import *
from datetime import date


class Key:

    def __init__(self, pwd):
        self.pwd = pwd
        
    def pattern(self):
        sc = ['@', '#', '$', '/', '(', ')']
        di = {}
        pattern = string.ascii_uppercase
        i = 1
        for letter in pattern:
            di[letter] = i
            i += 1
        for k, v in di.items():
            di[k] = v*len(pattern)
            if len(str(v*len(pattern))) < 3:
                x = str(v*len(pattern))+"26"
                x = int(x)//26
                di[k] = x
        for num in range(10):
            di[str(num)] = i*len(pattern)//2
            i += 2
        for spical_chr in sc:
            di[spical_chr] = i*len(pattern)//2
            i += 3

        return di

    def lock(self):
        passw=[]
        todays_date = date.today()
        def progressbar(it, prefix="", size=60, out=sys.stdout): 
            count = len(it)
            def show(j):
                x = int(size*j/count)
                print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                        end='\r', file=out, flush=True)
            show(0)
            for i, item in enumerate(it):
                yield item
                show(i+1)
            print("\n", flush=True, file=out)


        try:
            for letter in self.pwd:
                encripted = self.pattern()[letter.upper()]
                passw.append(str(encripted))
                result=''.join(passw)
            if len(self.pwd) >= 8 and self.pwd[0]==self.pwd[0].title():
                for i in progressbar(range(15), "Encripting: ", 50):
                    time.sleep(0.5) 
                print('The Password get Encripted successfully')
            
                with open('C:/Program Files/Password/password.json', 'a', encoding='utf-8') as f:
                    json.dump(result,f)

            else:
                for i in progressbar(range(15), "Encripting: ", 50):
                    time.sleep(0.3) 
                time.sleep(0.2) 
                print(cs("Error ocure while Encripting!!!", "#ff0000"))
                print(("Check if your password have the requirment characters and must be uppercase the first letter", "#ff0000"))

        except: 

            print(cs("Error Encripting!!!", "#ff0000"))
            print(cs("The pasword already locked try another one", "#ff0000"))
    
    def unlock(self):
        pattern=[]
        def progressbar(it, prefix="", size=60, out=sys.stdout): 
            count = len(it)
            def show(j):
                x = int(size*j/count)
                print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                        end='\r', file=out, flush=True)
            show(0)
            for i, item in enumerate(it):
                yield item
                show(i+1)
            print("\n", flush=True, file=out)

        pwd=self.pwd
        #pattern = ([pwd[i:i+3] for i in range(0, len(pwd), 3)])
        for i in range(0, len(pwd),3):
            pattern.append(pwd[i:i+3])
        result=[]

        for num in pattern:
            num=int(num)
            result.append(list(self.pattern().keys())[list(self.pattern().values()).index(num)])
        for i in progressbar(range(15), "Cracking password: ", 50):
            time.sleep(0.5)
        time.sleep(0.7) 
        passwd=(''.join(result))
        print("Password: ",(cs(passwd,"#ff0000")))
            
      
