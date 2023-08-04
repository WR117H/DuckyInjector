import os
from colorama import Fore
import random

# Generate 3 random numbers between a specified range
min_num = 1
max_num = 3

random_numbers = []
for _ in range(1):
    random_numbers.append(random.randint(min_num, max_num))

banner1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠿⠿⠷⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⢀⣀⡀⠙⣷⡀⠀⠀⠀    ___           __  
⠀⠀⠀⡀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠘⠿⠃⠀⢸⣿⣿⣿⣿  / _ \__ ______/ /____ __ 
⠀⣠⡿⠛⢷⣦⡀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟ / // / // / __/  '_/ // / 
⢰⡿⠁⠀⠀⠙⢿⣦⣤⣤⣼⣿⣄⠀⠀⠀⠀⠀⢴⡟⠛⠋⠁⠀/____/\_,_/\__/_/\_\\_, /_     
⣿⠇⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀ /  _/__    (_)__ /___/ /____  ____
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀ _/ // _ \  / / -_) __/ __/ _ \/ __/
⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀ ⠀/___/_//_/_/ /\__/\__/\__/\___/_/ 
⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀        |___/   
⠀⠹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠉⠙⠛⠿⠶⣶⣶⣶⣶⣶⠶⠿⠟⠛⠉⠀⠀

"""
banner2 = """
    ____             __         ____        _           __            
   / __ \__  _______/ /____  __/  _/___    (_)__  _____/ /_____  _____
  / / / / / / / ___/ //_/ / / // // __ \  / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /__/ ,< / /_/ // // / / / / /  __/ /__/ /_/ /_/ / /   {Fore.LIGHTYELLOW_EX} __(.)<{Fore.RESET}  
/_____/\__,_/\___/_/|_|\__, /___/_/ /_/_/ /\___/\___/\__/\____/_/    {Fore.LIGHTYELLOW_EX}\___){Fore.RESET} 
                      /____/         /___/                             
"""
banner3 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠉⠙⠲⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⠁⣀⣀⣀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⡀⠘⡆⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⠉⠉⠉⣹⡆⠀⠀⣿⣿⣿⣿⡇⠀⢀⣀⡿⠀⢹⠀⠀
⠀⢀⣀⣠⡬⠿⠿⠟⠓⠚⠛⠉⠉⠉⠙⢲⡈⠉⠉⠉⠉⠉⠉⠀⠀⠀⢸⡆⠀
⣞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠉⠓⠶⠶⣶⠶⠶⠶⠖⠒⠒⠒⠒⠒⢦⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠈⠓⠒⠶⠶⠶⠶⠶⡶⠶⠖⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀{Fore.RESET}Ducky{Fore.LIGHTYELLOW_EX}    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀  {Fore.RESET}Injector{Fore.LIGHTYELLOW_EX}    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀  {Fore.RESET}by @WR117H{Fore.LIGHTYELLOW_EX}    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def ASCII():
    os.system("clear||cls")
    if 1 in random_numbers:
       print(Fore.LIGHTYELLOW_EX+banner1+Fore.RESET)
    elif 2 in random_numbers:
       print(Fore.LIGHTMAGENTA_EX+banner2+Fore.RESET)
    elif 3 in random_numbers:
       print(Fore.LIGHTYELLOW_EX+banner3+Fore.RESET)

