from colorama import Fore
import sys
from module.functoin import Digispark, Arduino, Arduino_Prank_Talker, Digispark_Prank_Talker , check, help, clear, is_command_valid, runCMD
from module.banner import ASCII
from time import sleep
import signal
modules=['execution/download_exec','prank/computer_talking','prank/rick_roll','prank/change_background']
platforms=['arduino','digispark','hak5','esp32-s2']
is_on_module = 0
is_on_banner = 0
module_type=[]
module_name=[]
text=[]
def disable_ctrl_c():
    def handler(signum, frame):
        if is_on_banner > 0:
          
           print('\nAborting...')
           sleep(1)
           exit()
        else:
           print("TRL+C is disabled, use 'exit' to quit")


        if is_on_module == 0:
           print(Fore.LIGHTBLUE_EX+"\033[4mdi1\033[0m"+Fore.RESET+" > ", end="")

        else:
           print("\033[4mdi1\033[0m "+module_type[0]+"("+Fore.LIGHTBLUE_EX+module_name[0]+Fore.RESET+")"+" > ", end="")
        sys.stdout.flush()  # Flush the output buffer to ensure immediate input prompt

    signal.signal(signal.SIGINT, handler)
# Python script to create a Digispark or Arduino script to download an executable file with PowerShell
plat=[]
url=[]
path=[]
def main():
    global platforms    
    global plat
    global url
    global text
    global path
    global is_on_module
    global module_name
    while True:
      
       platform = input(Fore.LIGHTBLUE_EX+"\033[4mdi1\033[0m"+Fore.RESET+" > ").lower()

       if platform.startswith("set"):
          if platform[4:12] == "platform":
             if platform[13:21] == "arduino":
                if len(plat) == 0:
                   plat.append("arduino")
                else:
                    del plat[0] 
                    plat.append("arduino")
             elif platform[13:23] == "digispark":
                if len(plat) == 0:
                    plat.append("digispark")  
                else:
                    del plat[0] 
                    plat.append("digispark")                
             else:
                print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the platform "+"["+Fore.LIGHTYELLOW_EX+f"{platform[4:]}"+Fore.RESET+"]"+" was not found or failed to import.")
          else:
             print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the there is no such thing as "+"["+Fore.LIGHTYELLOW_EX+f"{platform[4:]}"+Fore.RESET+"]"+" to set")
       elif platform.startswith("help"):
          help("console")
       elif platform.startswith("clear"):
          clear()
       elif platform.startswith("exit"):
          exit(0)
       elif platform.startswith("show"):

          if platform[5:14] == "platforms":
             for i in range(0, len(platforms), 5):
                print(" ".join(platforms[i:i+5]))
   
  
          elif platform[5:13] == "platform":
             if len(plat) == 0:
                print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"Haven't selected any platforms")
             else:
                print(plat[0])
   
   
          elif platform[5:12] == "modules":
             for i in range(0, len(modules), 5):
                print(" ".join(modules[i:i+5]))
          else:
            print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"there is no such a thing as "+"["+Fore.LIGHTYELLOW_EX+f"{platform[5:]}"+Fore.RESET+"]"+" to show.")
       elif platform.startswith("banner"):
          ASCII(0)
       elif platform.startswith("use"):
          if len(plat) == 0:
            print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"set the platform")  
          else:
            if platform[4:13]=="execution":
                if len(module_type) > 0:
                   del module_type[0]
                 
                   module_type.append(platform[4:13])
                else:
                   module_type.append(platform[4:13])
                plat=plat
                if platform[13:27] == "/download_exec":
                    is_on_module+=1
                    if len(module_name) == 0:
                        module_name.append(platform[13+1:27])
                    else:
                        del module_name[0]
                        module_name.append(platform[13+1:27])
                    if len(plat) != None:                        
                        while True:

                            platform = input("\033[4mdi1\033[0m "+module_type[0]+"("+Fore.LIGHTBLUE_EX+module_name[0]+Fore.RESET+")"+" > ")
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
                                    if plat[0] == "digispark":
                                        platform="digispark"

                                        check(f"Generating the script for {platform} ")
                                        script = Digispark(url, file_path,DEFAULT_DELAY, MAIN_DELAY)
                                        sleep(1)
                                        file_name = "digispark.ino"
                                        with open(file_name, "w") as f:
                                            f.write(script)        

                                        check(f"Generated the script for {platform} in {file_name}")
                                    elif plat[0] == "arduino":
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
                                is_on_module-=1
                                break                 
                            elif platform.startswith("exit"):
                                exit(0)                                                              

                    else:
                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"please select a platform such as arduino and digispark ")
            elif platform[4:9]=="prank":
                if len(module_type) > 0:
                   del module_type[0]

                   module_type.append(platform[4:9])
                else:
                   module_type.append(platform[4:9])
                plat=plat
                if platform[9:16] == "/talker":
                    is_on_module+=1
                    if len(module_name) == 0:
                        module_name.append(platform[9+1:16])
                    else:
                        del module_name[0]
                        module_name.append(platform[9+1:16])
                    if len(plat) != None:
                        while True:

                            platform = input("\033[4mdi1\033[0m "+module_type[0]+"("+Fore.LIGHTBLUE_EX+module_name[0]+Fore.RESET+")"+" > ")
                            if platform.startswith("set"):

                                if platform[4:8] == "text":
                                    if len(path) == 0:
                                        text.append(platform[9:])
                                    else:
                                        del text[0] 
                                        text.append(platform[9:])
                            elif platform.startswith("show"):
                                if platform[5:13] == "platform":
                                    print(str(plat))
                                elif platform[5:9]=="text":
                                    if len(text) == 0:
                                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"Haven't entred any text")
                                    else:
                                        print(text[0])
                            elif platform.startswith("run"):
                                if len(text) > 0:
                                    # Convert the user input to an integer (milliseconds should be a whole number)
                                    MAIN_DELAY = 2500
                                    DEFAULT_DELAY = 750
                                    text=text[0] 
                                    if plat[0] == "digispark":
                                        platform="digispark"

                                        check(f"Generating the script for {platform} ")
                                        script = Digispark_Prank_Talker(text, DEFAULT_DELAY, MAIN_DELAY)
                                        sleep(1)
                                        file_name = "digispark.ino"
                                        with open(file_name, "w") as f:
                                            f.write(script)        

                                        check(f"Generated the script for {platform} in {file_name}")
                                    elif plat[0] == "arduino":
                                        platform="arduino"
                                        check(f"Generating the script for {platform} ")
                                        script = Arduino_Prank_Talker(text, DEFAULT_DELAY, MAIN_DELAY)
                                        sleep(1)
                                        file_name = "arduino.ino"
                                        with open(file_name, "w") as f:
                                            f.write(script) 
                                        check(f"Generated the script for {platform} in {file_name}")
                                elif platform.startswith("exit"):
                                    exit(0)
                                else:
                                    print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"set the text")    
                            elif platform.startswith("back"):
                                is_on_module-=1
                                break
                            elif platform.startswith("exit"):
                                exit(0)

                    else:
                        print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"please select a platform such as arduino and digispark ")
                else:
                   print(1)
            else:

                print(Fore.LIGHTRED_EX+"[-] "+Fore.RESET+"the module "+"["+Fore.LIGHTYELLOW_EX+f"{platform[11:]}"+Fore.RESET+"]"+" was not found or failed to import.")
       
       else:
          if is_command_valid(platform):

             print(Fore.LIGHTBLUE_EX+"[*] "+Fore.RESET+"exec: \n")
             runCMD(platform)

          else:
             print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" di1: command not found: "+platform)

if __name__ == "__main__":
    # Start the input thread
    disable_ctrl_c()
    try:
        is_on_banner+=1
        ASCII(1)
        is_on_banner-=1
        main()
    except KeyboardInterrupt:
        pass
