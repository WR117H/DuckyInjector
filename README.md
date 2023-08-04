# DuckyInjector


![Uploading Screenshot 2023-08-04 180224.png…]()
                                                                      
A tool for creating scripts for arduino and digispark for HID attacks automatically 
# Setup
First install DuckyInjector using git
```
git clone https://github.com/WR117H/DuckyInjector.git
```
Then head to the folder
```
cd DuckyInjector
```
Install the requirements using pip
```
pip install -r requirements.txt
```
## How to interact with it?

Well DuckyInjector's a console based proggram and for interacting you don't have to use arguments
and you'll learn how to work with it later with commands I'd mention later

## Commands

| Command | Description |
| --- | --- |
| `set` | to set platform, url, path ... |
| `use` | to use modules |
| `show` | to see objects that you set before |
| `help` | I think this is so clear |
| `run` | to run the module after selecting it 
and after setting its options |

## Modules
1: [download_exec]() <it's a module that you can download and execute .exe files with it>

## Examples
How to set platform?
```
di1 > set digispark
```
or
```
di1 > set arduino
```
How to use a module?
```
di1 > use module/download_exec
```
You gotta notice that you should select the platform first and then select the module.

And you can get help using to find out what you should do in a module
```
di1 > help
```
