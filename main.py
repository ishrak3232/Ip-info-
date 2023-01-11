import colorama
import requests, json
import os
from colorama import Fore, Style, Back
import time
import ipinfo
from ipinfo import *
import geopy
from geopy.geocoders import Nominatim

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
ip_address = input("  >>  ")
handler = ipinfo.getHandler('a10aa7cbd78ac9')
details = handler.getDetails(ip_address)
geolocator = Nominatim(user_agent="unknown.ip")
url = str(geolocator.reverse(details.loc))
colorama.init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}latitude: "+details.latitude)
print(f"{Fore.LIGHTRED_EX}longitude: "+details.longitude)
print(f"{Fore.LIGHTRED_EX}country: "+details.country_name)
print(f"{Fore.LIGHTRED_EX}city: "+details.city)
print(f"{Fore.LIGHTRED_EX}region: "+details.region)
print(f"{Fore.LIGHTRED_EX}postal: "+details.postal)
print(f"{Fore.LIGHTRED_EX}timezone: "+details.timezone)
print(f"{Fore.LIGHTRED_EX}org: "+details.org)
print(f"{Fore.LIGHTRED_EX} address: "+url)
last = input("press enter to exit....")
if last == "":
    os.system('exit')
