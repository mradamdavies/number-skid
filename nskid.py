#!/usr/bin/env python
# -*- coding: utf-8 -*-
author__ = "Mr. Adam Davies"
copyright__ = "Copyleft 2021, mradamdavies"
license__ = "GPL"
version__ = "1.0.3"
maintainer__ = "mradamdavies"
email__ = "abeontech@gmail.com"
status__ = "Potato code - it's like spaghetti code, but worse!"

import os
import time
import requests
import re
from bs4 import BeautifulSoup

# Colours for menu stuff
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# General Vars
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
hostname = "google.com"
ping_google = os.system("ping -c 1 " + hostname)


# Quick and nasty online check. 429 header codes handled below.
def ping_check():
    
    if ping_google == 0:
      print("Google ping: Success \r")
      print("Generating numbers... \r\n")
      time.sleep(1)
      
    else:
      print("Google ping: Failed! \r\nExiting! \r\n")
      time.sleep(3)


# Grab SERPs. Loop that mashed potato. 
def grab_serps(choice):


    query_domains = ['amazon+site:nomorobo.com&tbs=qdr:{choice}&sa=X', 'amazon+site:robokiller.com&tbs=qdr:{choice}&sa=X', 'amazon+site:who-called.co.uk&tbs=qdr:{choice}&sa=X' ]

    # Loop SERPs
    for x in query_domains:
        dork = f"https://google.com/search?q={x}"
        resp = requests.get(dork, headers=headers)

        # Too many responses
        if resp.status_code == 429:
            message_sleep("Too many queries! \rPlease wait a moment or change IP (Windscribe) ;)", 5)

        # If 200 / OK
        elif resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            results = []
            for g in soup.find_all('div', class_='g'):
                
                rc = g.find('div', class_='yuRUbf')
                anchor = rc.find('a')
                title = anchor.find('h3').text
                item = {"title": title}
                results.append(item)

                # Output
                x = title
                trimmed = re.sub('[^(0-9{3}) (0-9){3}-]|( - )|( |)', '', x) # For the love of God, FIX ME. Due in next update!
                try:
                  print(trimmed)
                except:
                  print("No results. Try a longer time-frame!") 
                
        # Epic Fail!
        else:
            print("Fail Error Code: 9001")
    ###########// End SERP Loop

# Do Menu Stuff
def main():
    choice = "0"
    while choice =="0":
        
        if choice == 1:
            choice == "h"
        elif choice == 2:
            choice == "d"
        elif choice == 3:
            choice == "w"
            
        # print("Enter a number:")
        print("1) Grab numbers: last HOUR")
        print("2) Grab numbers: last DAY")
        print("3) Grab numbers: last WEEK")
        #print("4) Submenu")

        choice = input ("Enter option: ")

        # Option 4 - help menu
        if choice == "4":
            logo()
            print(bcolors.GREEN + "Halp! https://mradamadvies.com")
            second_menu()
            
        # Option 3 - past week
        elif choice == "3":
            logo()
            print(bcolors.GREEN + "Showing phone numbers from the past week..." + bcolors.ENDC)
            ping_check()
            time.sleep(1)
            grab_serps(choice)
            
        # Option 2 - past day
        elif choice == "2":
            logo()
            print(bcolors.GREEN + "Showing phone numbers from the past day..." + bcolors.ENDC)
            ping_check()
            time.sleep(1)
            grab_serps(choice)
            
        # Option 1 - past hour
        elif choice == "1" :
            logo()
            print(bcolors.GREEN + "Showing phone numbers from the past hour..." + bcolors.ENDC)
            ping_check()
            time.sleep(1)
            grab_serps(choice)
                        
        # Fallback menu
        else:
            logo()
            print(bcolors.FAIL + "Please select a valid option." + bcolors.ENDC)
            main()
            exit

#  Clear Screen
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

# Intro
def logo():
    screen_clear()
    print(bcolors.GREEN + "░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░▒▒▒░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░░█▒░▒█▓▒░░░░░░░▒▓█▓░░░░▒▒▒░░░░░░░▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░▒░░░▒█▓░▓▒░▓▓▓▒▒███▓▒░░▒▓▒░▒▓▒░░░▒▒░░░░░░▒▒▒░░░▒▒▒░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░▓▒░░██▓░██▒░▒████▓▓▒░▒▒░▓█▒░░▒▓▓░░░░░░░░▒▒▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░▓██▒░▒░░█▒░░▒▓█▒░░░▒░▓█▓░░▓██▓░░░░░░█▓░░░░░░█▓░▓████▓▒░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░▓█░░░░▒██▒░▒▓██░░░░▓██░░███░░▒▒▒▒▓█░░░░░▓░░░▓▒░░░░░▒▒▒░░░▒█░░▓▓░░░ \r\n░░░░░░░░░░░░░░▒█▒▒██████▓░░░░░░░█▓░▒███▒░░░▒█████▓▓▓██▓░░▒░▓█▓▒░░░░░▒░░█▒▒█▒█░░ \r\n░░░░░░░░░░░░░░░░██████████░░░░░░░░▓███▓░░░░░░▒▒▓▓▓▓▓▒░▒░▓▒░▒░░░░░░░▒█░░▓██▓▒█▓░ \r\n░░░░░░░░░░░░░░░░░█████▓▒██░░░░░░░░░███▒▓████▓▒░▒▓▓▓▓▓▓▒██░██▓▒░░░░░▒██████░░▓█▒ \r\n░░░░░░░░░░░░░░░██████▒░░█▓░░░░░░░░░░▒███████████▓▒░░█▓█▓░░░▓███▓▒░░▓█░░▓██░░▒██ \r\n░░░░░░░░░░░░░░░░████▒░░░█▓░░░░░░░░░░░░░░▓█████████▒▒░░░░░░░░▒█████▒██░░▒█▓░░░▓▒ \r\n░░░░░░░░░░░░░░▓█████░░░░█▒░░░░░░░░░░░░░░░███▓░░░░▒▒▒░░░░░░░░░▒████▓█▓░▓░██░░░░░ \r\n░░░░░░░░░░░░▒░░█████░░░░▓▒░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓██▓▓░▒░░░░░░░░ \r\n░▒██░░░░▒░░░▓░░▒████░░░░▒▒░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███░░░▓░█░░░░░░░░ \r\n░▓██░░░░█▒░░▓▓▓█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▓░▒░▓▒▒█▓░░░░░░ \r\n░██▓░░░▓█░░░▒████████░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░▒█▓░░▓▒▓░░░░░░░░░░ \r\n░██▓░░░██░░░░████████▒░░░░░░░▒▒▒▒▒▒▒░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▓░░░▒▓░▓░░░░░░░░░ \r\n▒██▓▒▒▒█▓░░░▓█▒▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒██▒░░░░░░░ \r\n▒██▓▓▓██░░░░█▓░░█▒░▓▓▒▒░░░░▒██▓▓▒░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░▓▒▓▒▒░░░░░ \r\n▓█▓░░░██░░░▓█▓▒░▒░░░█░░░░░░▓██████▓▓▓░░▒▒░░░░█▓░████████▓▓▒░░░░░░░░░░░░░░░░░░░░ \r\n██▒░░▒█▓░░░█▓▓▓██▓░░▒▓▒░░░▓███▓░▒▓▒░▒▓██▒░░░▓██▓▒▓▓▒▒███▓▒░░░░░▒█░░▒░░░░░░░░░░░ \r\n██░░░▓█▒░░▓█░░░░▓█░░░░▓░░░░▓▓████████████▓▒░██████████▓░░░░░░░███░░░▒▒▒▒░░░░░░░ \r\n░▒░░░██░░░██░░░░░█▒░░░▒░░░░░░░░▒▒▒▒███▓▓▓░░░▒█▒▓████▓▒░░░░░░░░██▓░░░░░░░░░░░░░░ \r\n░░░░░▒▒░░▒█▓░░░░░▒▓░░░░░░░░░░░░░░▒▒▒░░░▒░░░░░░▒░░░░░░░░░░░░▒░░▓░░░░░░▓▒░░░░░░░░ \r\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒░▓░░░░░▒▒█░░░░░░░░ \r\n░░░░░░░░░▓▓░░░░██▒░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▒▒▒░░▓░░▒░░▓▒▒█░░░░░░░ \r\n░░░░░░░░░▓█░░░░██▓░▒█░░█░░░░░░░░░░░░░▓█░░░░░░░░░░░░░▒▓█▓▓▓░░▒█░░░█░░▓▓░█▒░░░░░░ \r\n░░░░░░░░░▓█░░░░▓█▓▒█▒▒▓██▒░░░░░░▒░░░░░░▒▒░░▒▒█▓░░░░░░░░█▓░░▓▒█▒░░█▓░█▒░▓█░░░░░░ \r\n░░░░░░░░░▒█▓▓████▓██░░░░▓█▓░░░░█▒░░░░░░░░░░░░░░░░▒█████▒░░▓░░█▓▓▓██░░░░░░░░░░░░ \r\n░░░░░░░░░▒█▓░░░▓███░░░░░░██▓▒░░██▒▒▒▒▒▒▒▒▒▒▒▒▓████▓▓░░░░▓▒░░░▓█▒▒▒█░░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░▒██▒░░░░░░▒█▒▒█▒░░▒▒▒▓███████████▒░░░░░▒▒░░░░░▓█▒░░█▒░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░░█▓░░░░░░░░░░░░▒█▒░░░░░▒▓▓███▓▒░░░░░░▒▒░░░░░░░▒█▒░░░▓░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░░▓░░░░░░░░░░░░░░░▒▓▒░░░░░░░░░░░░░░░▒▒░░░░░░░░░░█▒░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░░░░░░░▓▒░░░░░░░░░░░▒▒░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░" + bcolors.ENDC)
    print(bcolors.ORANGE + "                        [ Number Skid ]-[ by mradamdavies ] \r\n                             The scammer number grabber!" + bcolors.ENDC)

# Help Menu
def second_menu():
    print("This is the help menu")

# Do stuff
logo()
main()
