import os
try:
    import requests
    import pystyle
    from pystyle import Colors, Colorate, Add, Center, Box, Write
    import threading
    from threading import Thread
except:
    os.system("pip install requests")
    os.system("pip install requests")
    os.system("pip install threading")
    
# DEV BY ATSUYO 
    
import requests
import pystyle
from pystyle import *
import threading
from threading import Thread

print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Welcome to TikTok Share BOT"), 1))
print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Dev by Atsuyo\n"), 1))
videoid = Write.Input(Center.XCenter("Enter your VideoID ==> "), Colors.red_to_white, interval=0.0100)
while True:
    response = requests.get(f"https://noelp-backend.xyz/shares?id={str(videoid)}")
    if response.status_code == 200:
        print(response.text)
        
    elif response.status_code == 429:
        print("You are ratelimit...")
