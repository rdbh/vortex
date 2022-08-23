# Rick

import os

#import alert
import config
import datamanager as dm
import menu
#import searcher


def clear(): return os.system('cls')


# global variables
work_dir = os.getcwd()
case = {
    "name": "Choose case"
}


def add_keyword():
    keyword = input("New keyword to add: ")
    description = input("Keyword description: ")
    language = input("Keyword language: ")
    translation = input("Translation: ")
    #case = input("Enter case: ")

    # lookup case in datamanger
    filename = case["keywords"]

    newkeyword = {
        "keyword": keyword,
        "description": description,
        "language": language,
        "translation": translation
    }
    dm.saveKeyword(newkeyword)


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
    press = input("Press eneter to continue")


def discover():
    keywords = []
    sites = []

    if searcher.scrape(keywords, sites):
        print("Keywords found in site list")

    # Data presentation

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
    main_menu = menu.Menu(title=config.BANNER)
    alert_menu = menu.Menu(title="Alerts")
    case_menu = menu.Menu(title="Cases")
    keyword_menu = menu.Menu(title="Keywords")
    search_menu = menu.Menu(title="Searches")
    website_menu = menu.Menu(title="Websites")
    main_menu.set_options([
        ("Case Menu", case_menu.open),
        {"Keyword Menu", keyword_menu.open}
        ("Exit", main.close)
    ])
    alert_menu.set_options([
        ("Return to main menu", alert_menu.close)
    ])
    case_menu.set_options([
        ("Return to main menu", case_menu.close)
    ])
    keyword_menu.set_options([
        ("Return to main menu", keyword_menu.close)
    ])
    search_menu.set_options([
        ("Return to main menu", search_menu.close)
    ])
    website_menu.set_options([
        ("Return to main menu", website_menu.close)
    ])
    main_menu.open()


def main():
    #websites.check("./Project Vortex/Osint_WebsiteList.txt")
    #mywebsites = websites.list("./Project Vortex/Osint_WebsiteList.txt")
    #sitelist = datamanager.getWebsites("case1")
    #result = searcher.scrape(["apples","oranges"], sitelist)
    runtime()


if __name__ == "__main__":
    clear()
    main()
