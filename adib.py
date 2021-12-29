from requests import *
import socket

ip = get('https://api.ipify.org/').text
uname = socket.gethostname()
maddr = socket.gethostbyname(uname)

INFO = '''
 
                         ______   
  ____________    _____|\     \  
 /            \  /     / |     | 
|\___/\  \\___/||      |/     /| 
 \|____\  \___|/|      |\____/ | 
       |  |     |\     \    | /  
  __  /   / __  | \     \___|/   
 /  \/   /_/  | |  \     \       
|____________/|  \  \_____\      
|           | /   \ |     |      
|___________|/     \|_____| 
 
 
'''

print("\u001b[32;1m ", INFO)

print("\u001b[36;1m Your Uname : ", uname)
print("\u001b[36;1m Your public IP is : ", ip)
print("\u001b[36;1m Your PC's address : ", maddr)

