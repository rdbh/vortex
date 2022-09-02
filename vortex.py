# Rick

import os

#import alert
import config
import datamanager as dm
import menu
#import searcher

# Screen Clearance
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


def runtime():
    main_menu = menu.Menu(title=config.BANNER)
    alert_menu = menu.Menu(title="Alerts")
    case_menu = menu.Menu(title="Cases")
    config_menu = menu.Menu(title="Configuration")
    keyword_menu = menu.Menu(title="Keywords")
    search_menu = menu.Menu(title="Searches")
    website_menu = menu.Menu(title="Websites")
    main_menu.set_options([
        ("Alert Menu", alert_menu.open),
        ("Case Menu", case_menu.open),
        ("Configuration Menu", config_menu.open),
        ("Keyword Menu", keyword_menu.open),
        ("Search Menu", search_menu.open),
        ("Website Menu", website_menu.open),
        ("Exit", main_menu.close)
    ])
    alert_menu.set_options([
        ("Return to main menu", alert_menu.close)
    ])
    case_menu.set_options([
        ("Return to main menu", case_menu.close)
    ])
    config_menu.set_options([
        ("Return to main menu", config_menu.close)
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
