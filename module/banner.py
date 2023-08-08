import sys
import time
import os
from colorama import Fore
import random
GREEN=Fore.LIGHTGREEN_EX
RESET=Fore.RESET
YELLOW=Fore.LIGHTYELLOW_EX
# Generate 3 random numbers between a specified range
min_num = 1
max_num = 3

random_numbers = []
for _ in range(1):
    random_numbers.append(random.randint(min_num, max_num))




def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "starting the duckyinject console..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 10):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")

banner1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠿⠿⠷⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⢀⣀⡀⠙⣷⡀⠀⠀⠀   ___           __  
⠀⠀⠀⡀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠘⠿⠃⠀⢸⣿⣿⣿⣿  / _ \__ ______/ /____ __
⠀⣠⡿⠛⢷⣦⡀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟ / // / // / __/  '_/ // /   
⢰⡿⠁⠀⠀⠙⢿⣦⣤⣤⣼⣿⣄⠀⠀⠀⠀⠀⢴⡟⠛⠋⠁⠀/____/\_,_/\__/_/\_\\\\_, /_        
⣿⠇⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀  /  _/__    (_)__ /___/ /____  ____
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀ _/ // _ \  / / -_) __/ __/ _ \/ __/
⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀ ⠀/___/_//_/_/ /\__/\__/\__/\___/_/ 
⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀        |___/            
⠀⠹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠉⠙⠛⠿⠶⣶⣶⣶⣶⣶⠶⠿⠟⠛⠉⠀⠀

"""
banner2 = f"""
    ____             __         ____        _           __            
   / __ \__  _______/ /____  __/  _/___    (_)__  _____/ /_____  _____
  / / / / / / / ___/ //_/ / / // // __ \  / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /__/ ,< / /_/ // // / / / / /  __/ /__/ /_/ /_/ / /   
/_____/\__,_/\___/_/|_|\__, /___/_/ /_/_/ /\___/\___/\__/\____/_/   
                      /____/         /___/                             
"""
banner3 = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠉⠙⠲⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⠁⣀⣀⣀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⡀⠘⡆⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⠉⠉⠉⣹⡆⠀⠀⣿⣿⣿⣿⡇⠀⢀⣀⡿⠀⢹⠀⠀
⠀⢀⣀⣠⡬⠿⠿⠟⠓⠚⠛⠉⠉⠉⠙⢲⡈⠉⠉⠉⠉⠉⠉⠀⠀⠀⢸⡆⠀
⣞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠉⠓⠶⠶⣶⠶⠶⠶⠖⠒⠒⠒⠒⠒⢦⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠈⠓⠒⠶⠶⠶⠶⠶⡶⠶⠖⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀  {RESET}Ducky{YELLOW}    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀  {Fore.RESET}Injector{Fore.LIGHTYELLOW_EX}    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def ASCII(x):

    min_num = 1
    max_num = 3
    
    random_numbers = []
    for _ in range(1):
       random_numbers.append(random.randint(min_num, max_num))
    
    if x == 1:
    
       load_animation()   

    else:
       pass
    if 1 in random_numbers:
       print(Fore.LIGHTYELLOW_EX+banner1+Fore.RESET)
    elif 2 in random_numbers:
       print(Fore.LIGHTYELLOW_EX+banner2+Fore.RESET)
    elif 3 in random_numbers:
       print(Fore.LIGHTYELLOW_EX+banner3+Fore.RESET)
    print("by: "+Fore.LIGHTBLUE_EX+"@WR117H"+Fore.RESET+" | version: "+Fore.LIGHTMAGENTA_EX+"1.0"+Fore.LIGHTGREEN_EX+" main"+Fore.RESET)
    print(Fore.LIGHTYELLOW_EX+"Documentation:"+Fore.RESET+"  https://github.com/WR117H/DuckyInjector")
