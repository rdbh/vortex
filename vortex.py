# Rick

import os

#import alert
import config
import datamanager as dm
import keywordmanager
#import resultmanager
#import searcher
import websitemanager as websites

clear = lambda: os.system('cls')

# global variables
work_dir = os.getcwd()
case = {
    "name":"Choose case"
}

## Keyword search

    # Search keywords on a certain websites

    # List of keywords
    # Get keywords from a file
        ## or
    # Get keywords from keyboard
        ## or
    # Get keywords from website (OSINT list?)

        # Create variations of keywords

        # synonyms
        # other languages
        # l33sp3@k
        # name spelling

    # List websites
    # Get list from file
        ## or
    # Get the list from a search engine
        ## or
    # Get the list from other search results
        ## or
    # Get the list from start.me

## Alert system

    # Alert on changes to searches
    # Configurable search alerts (priority?)

    # Alert distribution via console
        ## or
    # Alert distribution via messaging
        ## or
    # Alert distribution via web/social media

def add_keyword():
    keyword = input("New keyword to add: ")
    language = input("Keyword language: ")
    translation = input("Translation: ")
    #case = input("Enter case: ")

    # lookup case in datamanger
    filename = case["keywords"]

    newkeyword = {
        "keyword":keyword,
        "language":language,
        "translation":translation
    }
    keywordmanager.save(filename, newkeyword)

def case_info():
    global case
    name = input("Case name: ")
    case = dm.getCase(name)
    print(case)
    nothing = input("Press enter to continue")

def change_dir():
    work_dir = input("Enter new working directory: ")
    if work_dir == "":
        work_dir = "./"

    if os.path.isdir(work_dir):
        os.chdir(work_dir)
    else:
        try:
            os.mkdir(work_dir)
        except: 
            print("Cannot create working directory")
        os.chdir(work_dir)
    return os.getcwd()

def check_web():
    filename = "./Project Vortex/Osint_WebsiteList.txt"
    websites.check(filename)
    press=input("Press eneter to continue")

def discover():
    keywords = []
    sites = []
    
    if searcher.scrape(keywords, sites):
        print("Keywords found in site list")
    
    ## Data presentation

    # Sort by DTG

    # Sort by topic

    # Sort by search engine
def menu():
    # menu options
    print(config.BANNER)
    print("Enter [A] to add a keyword")
    print("Enter [C] to check a web addresses")
    print("Enter [D] to change the working directory")
    print("Enter [G] to get case data")
    print("Enter [S] to add a website")
    print("Enter [W] to add a keyword")
    print()
    caseName = case["name"]
    print(f"Current case is:\n\t{caseName}")
    print(f"Current working directory is:\n\t{work_dir}")

    # get user input
    choice = input("\nEnter X to quit: ")
    print("\n\n")

    if choice.upper() == 'X':
        print("Exiting")
        quit()
    elif choice.upper() == 'A':
        add_keyword()
    elif choice.upper() == 'C':
        check_web()
    elif choice.upper() == 'G':
        case_info()
    # Change Settings
    elif choice.upper() == 'S':
        change_settings()
    # Change Settings
    elif choice.upper() == 'W':
        change_dir()
    # handle non-options
    else:
        print("Please select a valid option")

def runtime():
    while True:
        menu()        

def main():
    #websites.check("./Project Vortex/Osint_WebsiteList.txt")
    #mywebsites = websites.list("./Project Vortex/Osint_WebsiteList.txt")
    #sitelist = datamanager.getWebsites("case1")
    #result = searcher.scrape(["apples","oranges"], sitelist)
    runtime()

if __name__ == "__main__":
    clear()
    main()