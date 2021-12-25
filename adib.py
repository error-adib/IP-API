import pyfiglet
import os
from requests import *

ip = get('https://api.ipify.org/').text
help = '''

 [1] ip    - GET UR IP ADDRESS
 [2] about - About this script
 [3] exit  - EXIT THE SCRIPT

'''

txt = pyfiglet.figlet_format("Error", font="graffiti")
print(txt)

print("\u001b[32;1m Programmed By Adnan Adib")

con = True
while con:
    user = input("error >> ")

    if user=='ip':
        print("Your Public IP is: ", ip)
    
    elif user=='about':
        print("No INFO TO SHOW")
    
    elif user=='help':
        print("\u001b[36;1m ",help)
    
    elif user=='exit':
        con = False

    elif user=='cmd':
        os.system("start cmd")

    else:
        print("wrong command")

