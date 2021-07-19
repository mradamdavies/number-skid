#!/usr/bin/env python
# -*- coding: utf-8 -*-
author__ = "Mr. Adam Davies"
copyright__ = "Copyreft 2021, mradamdavies"
license__ = "GPL"
version__ = "1.0.5"
maintainer__ = "mradamdavies"
email__ = "abeontech@gmail.com"

import os
import sys
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
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
hostname = "google.com"

global counter

def grab_serps(choice):

    counter = 0
    query_domains = ['amazon+site:nomorobo.com&tbs=qdr:'+choice+'&sa=X',
                     'amazon+site:lookup.robokiller.com&tbs=qdr:'+choice+'&sa=X',
                     'microsoft+site:nomorobo.com&tbs=qdr:'+choice+'&sa=X', 
                     'microsoft+site:lookup.robokiller.com&tbs=qdr:'+choice+'&sa=X'
                     ]

    # Loop SERPs
    for x in query_domains:

        dork = f"https://google.com/search?q={x}"
        resp = requests.get(dork, headers=headers)

        # Too many responses
        if resp.status_code == 429:
            print(bcolors.FAIL + "Too many queries!" + bcolors.ENDC)
            print("* Wait a moment \r\n* Or change IP.")
            time.sleep(5)
            exit

        # 404 / Page Not Found
        elif resp.status_code == 404:
            print(bcolors.FAIL + "Page not found!" + bcolors.ENDC)
            print("* Check internet connection \r\n* Check query_domains")
            time.sleep(5)
            exit
            
        # 200 / OK
        elif resp.status_code == 200:
            
            counter = counter + 1
            
            if counter == 1:
                print (bcolors.ORANGE + "\r\n[ Amazon Scammers ]" + bcolors.ENDC)
            if counter == 3:
                print (bcolors.ORANGE + "\r\n[ Microsoft Scammers ]" + bcolors.ENDC)      
            
            soup = BeautifulSoup(resp.content, "html.parser")
            results = []
            
            for g in soup.find_all('div', class_='g'):
                
                rc = g.find('div', class_='yuRUbf')
                anchor = rc.find('a')
                title = anchor.find('h3').text
                item = {"title": title}
                results.append(item)


                # Check for blanks
                try:
                    x = re.search("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", title). group(0)
                except:
                    x = "Blank result"
                print(x)
                # print(x + " |-----> " + title) #debug
                

                
        # Epic Fail!
        else:
            print(bcolors.ORANGE + "Fatal Error!" + bcolors.ENDC)
            print(" * Check your internet connection! \r\n * Check your can access robokiller.com")
    ###########// End SERP Loop

# Do Menu Stuff
def main():
    choice = "0"
    while choice =="0":

        print("1) Grab numbers: last HOUR")
        print("2) Grab numbers: last DAY")
        print("3) Grab numbers: last WEEK")
        print("4) Info")

        choice = input ("Enter option: ")

        if choice == "4": # Option 4 - help menu
            logo()
            print(bcolors.GREEN + "Submit your suggestions -> https://github.com/mradamdavies/number-skid" + bcolors.ENDC)
            second_menu()
            
        elif choice == "3": # Option 3 - past week
            logo()
            print("Grabbing phone numbers from the past week...")
            time.sleep(1)
            grab_serps("w")
            
        elif choice == "2": # Option 2 - past day
            logo()
            print("Grabbing phone numbers from the past day...")
            time.sleep(1)
            grab_serps("d")
            
        elif choice == "1" : # Option 1 - past hour
            logo()
            print("Grabbing phone numbers from the past hour...")
            time.sleep(1)
            grab_serps("h")
            
        elif choice == "x" : # Exit
            logo()
            print("Closing...")
            time.sleep(2)
            sys.exit()
                        
        # Fallback menu
        else:
            logo()
            print(bcolors.FAIL + "Please select a valid option." + bcolors.ENDC)
            main()
            exit

#  Clear Screen
def screen_clear():
   if os.name == 'posix': # for mac and linux
      _ = os.system('clear')
   else: # for windows
      _ = os.system('cls')

# Intro
def logo():
    screen_clear()
    print(bcolors.GREEN + "░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░▒▒▒░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░░█▒░▒█▓▒░░░░░░░▒▓█▓░░░░▒▒▒░░░░░░░▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░▒░░░▒█▓░▓▒░▓▓▓▒▒███▓▒░░▒▓▒░▒▓▒░░░▒▒░░░░░░▒▒▒░░░▒▒▒░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░▓▒░░██▓░██▒░▒████▓▓▒░▒▒░▓█▒░░▒▓▓░░░░░░░░▒▒▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░▓██▒░▒░░█▒░░▒▓█▒░░░▒░▓█▓░░▓██▓░░░░░░█▓░░░░░░█▓░▓████▓▒░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░▓█░░░░▒██▒░▒▓██░░░░▓██░░███░░▒▒▒▒▓█░░░░░▓░░░▓▒░░░░░▒▒▒░░░▒█░░▓▓░░░ \r\n░░░░░░░░░░░░░░▒█▒▒██████▓░░░░░░░█▓░▒███▒░░░▒█████▓▓▓██▓░░▒░▓█▓▒░░░░░▒░░█▒▒█▒█░░ \r\n░░░░░░░░░░░░░░░░██████████░░░░░░░░▓███▓░░░░░░▒▒▓▓▓▓▓▒░▒░▓▒░▒░░░░░░░▒█░░▓██▓▒█▓░ \r\n░░░░░░░░░░░░░░░░░█████▓▒██░░░░░░░░░███▒▓████▓▒░▒▓▓▓▓▓▓▒██░██▓▒░░░░░▒██████░░▓█▒ \r\n░░░░░░░░░░░░░░░██████▒░░█▓░░░░░░░░░░▒███████████▓▒░░█▓█▓░░░▓███▓▒░░▓█░░▓██░░▒██ \r\n░░░░░░░░░░░░░░░░████▒░░░█▓░░░░░░░░░░░░░░▓█████████▒▒░░░░░░░░▒█████▒██░░▒█▓░░░▓▒ \r\n░░░░░░░░░░░░░░▓█████░░░░█▒░░░░░░░░░░░░░░░███▓░░░░▒▒▒░░░░░░░░░▒████▓█▓░▓░██░░░░░ \r\n░░░░░░░░░░░░▒░░█████░░░░▓▒░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓██▓▓░▒░░░░░░░░ \r\n░▒██░░░░▒░░░▓░░▒████░░░░▒▒░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███░░░▓░█░░░░░░░░ \r\n░▓██░░░░█▒░░▓▓▓█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▓░▒░▓▒▒█▓░░░░░░ \r\n░██▓░░░▓█░░░▒████████░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░▒█▓░░▓▒▓░░░░░░░░░░ \r\n░██▓░░░██░░░░████████▒░░░░░░░▒▒▒▒▒▒▒░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▓░░░▒▓░▓░░░░░░░░░ \r\n▒██▓▒▒▒█▓░░░▓█▒▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒██▒░░░░░░░ \r\n▒██▓▓▓██░░░░█▓░░█▒░▓▓▒▒░░░░▒██▓▓▒░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░▓▒▓▒▒░░░░░ \r\n▓█▓░░░██░░░▓█▓▒░▒░░░█░░░░░░▓██████▓▓▓░░▒▒░░░░█▓░████████▓▓▒░░░░░░░░░░░░░░░░░░░░ \r\n██▒░░▒█▓░░░█▓▓▓██▓░░▒▓▒░░░▓███▓░▒▓▒░▒▓██▒░░░▓██▓▒▓▓▒▒███▓▒░░░░░▒█░░▒░░░░░░░░░░░ \r\n██░░░▓█▒░░▓█░░░░▓█░░░░▓░░░░▓▓████████████▓▒░██████████▓░░░░░░░███░░░▒▒▒▒░░░░░░░ \r\n░▒░░░██░░░██░░░░░█▒░░░▒░░░░░░░░▒▒▒▒███▓▓▓░░░▒█▒▓████▓▒░░░░░░░░██▓░░░░░░░░░░░░░░ \r\n░░░░░▒▒░░▒█▓░░░░░▒▓░░░░░░░░░░░░░░▒▒▒░░░▒░░░░░░▒░░░░░░░░░░░░▒░░▓░░░░░░▓▒░░░░░░░░ \r\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒░▓░░░░░▒▒█░░░░░░░░ \r\n░░░░░░░░░▓▓░░░░██▒░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▒▒▒░░▓░░▒░░▓▒▒█░░░░░░░ \r\n░░░░░░░░░▓█░░░░██▓░▒█░░█░░░░░░░░░░░░░▓█░░░░░░░░░░░░░▒▓█▓▓▓░░▒█░░░█░░▓▓░█▒░░░░░░ \r\n░░░░░░░░░▓█░░░░▓█▓▒█▒▒▓██▒░░░░░░▒░░░░░░▒▒░░▒▒█▓░░░░░░░░█▓░░▓▒█▒░░█▓░█▒░▓█░░░░░░ \r\n░░░░░░░░░▒█▓▓████▓██░░░░▓█▓░░░░█▒░░░░░░░░░░░░░░░░▒█████▒░░▓░░█▓▓▓██░░░░░░░░░░░░ \r\n░░░░░░░░░▒█▓░░░▓███░░░░░░██▓▒░░██▒▒▒▒▒▒▒▒▒▒▒▒▓████▓▓░░░░▓▒░░░▓█▒▒▒█░░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░▒██▒░░░░░░▒█▒▒█▒░░▒▒▒▓███████████▒░░░░░▒▒░░░░░▓█▒░░█▒░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░░█▓░░░░░░░░░░░░▒█▒░░░░░▒▓▓███▓▒░░░░░░▒▒░░░░░░░▒█▒░░░▓░░░░░░░░░░░ \r\n░░░░░░░░░░█▓░░░░▓░░░░░░░░░░░░░░░▒▓▒░░░░░░░░░░░░░░░▒▒░░░░░░░░░░█▒░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░░░░░░░▓▒░░░░░░░░░░░▒▒░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░ \r\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░" + bcolors.ENDC)
    print(bcolors.ORANGE + "                        [ Number Skid ]-[ by mradamdavies ] \r\n                             The scammer number grabber!" + bcolors.ENDC)

# Help Menu
def second_menu():
    print("This will scrape a few Google SERPs for scammers phone numbers.")
    print(bcolors.BOLD + "Start with numbers from the past day!" + bcolors.ENDC + " (Option 2)")
    print("Numbers provided by Nomorobo and Robokiller, thanks guys. \r\nPlease check you're talking to a real scammer! \r\n")
    main()

# Do stuff
logo()
main()
