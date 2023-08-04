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

![192 168 1 1_ (1)](https://github.com/spaceeeeboy/Wifi-Ducky/assets/97615989/95a227b3-1617-4f7d-a187-3d3b88518d56)

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
And you can get help using to find out what you should do in a module
```
di1 > help
```
