import colorama
import argparse
import requests, json
import sys
from sys import argv
import os
from colorama import Fore, Style, Back
import time






#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
colorama.init(autoreset=True)
print('')
print(f"{Fore.BLUE}             ╱╱╱╱╱╱╭╮")
print(f"{Fore.CYAN}            ╱╱╱╱╱╱┃┃")
print(f"{Fore.GREEN}            ╭╮╭┳━╮┃┃╭┳━╮╭━━┳╮╭╮╭┳━╮      ")
print(f"{Fore.LIGHTBLUE_EX}            ┃┃┃┃╭╮┫╰╯┫╭╮┫╭╮┃╰╯╰╯┃╭╮╮     ")
print(f"{Fore.LIGHTCYAN_EX}            ┃╰╯┃┃┃┃╭╮┫┃┃┃╰╯┣╮╭╮╭┫┃┃┃╭╮     ")
print(f"{Fore.LIGHTGREEN_EX}            ╰━━┻╯╰┻╯╰┻╯╰┻━━╯╰╯╰╯╰╯╰╯╰╯     ")
print(f"{Fore.LIGHTWHITE_EX}                       ╭━━┳━━━╮      ")
print(f"{Fore.LIGHTGREEN_EX}                       ╰┫┣┫╭━╮┃      ")
print(f"{Fore.LIGHTCYAN_EX}                       ╱┃┃┃╰━╯┃")
print(f"{Fore.LIGHTBLUE_EX}                       ╱┃┃┃╭━━╯     ")
print(f"{Fore.LIGHTWHITE_EX}                      ╭┫┣┫┃")
print(f'{Fore.WHITE}                      ╰━━┻╯')

txt = f"{Fore.LIGHTCYAN_EX} put the ip "
for letter in txt:
    colorama.init(autoreset=True) 
    print(letter, end="", flush=True)
    time.sleep(0.1)
ip = input("  >>")

api = "http://ip-api.com/json/"

try: 
        os.system("cls")
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        print ("[Victim]:", data['query'])
        print ("[ISP]:", data['isp'])
        print ("[Organisation]:", data['org'])
        print ("[City]:", data['city'])
        print ("[Region]:", data['region'])
        print ("[Longitude]:", data['lon'])
        print ("[Latitude]:", data['lat'])
        print ("[Time zone]:", data['timezone'])
        print ("[Zip code]:", data['zip'])


except KeyboardInterrupt:
        print ('Terminating, Bye')
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (" check your internet connection!")
        



