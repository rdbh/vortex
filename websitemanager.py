# TJ
#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


########################################
# WebsiteManager.PY              TJ
#Get, Save, Sort Website
    # List websites
    # Get list from file MAYBE THIS ONE: (https://start.me/p/gy0NXp/open-source-intelligence-osint)
        ## or
    # Get the list from a search engine
        ## or
    # Get the list from other search results
        ## or
    # Get the list from start.me
#####################################################################
import os
import requests

HTTP_TIMEOUT = 10
Web_List= "./Project Vortex/Osint_WebsiteList.txt"

clear = lambda: os.system('cls')

def check(loadname):
    # Variable Scope
    status_list = []

# Save results as CSV
    save_file_name = "WebSites_VORTEX.csv"
    try:
        save_file = open(save_file_name, "w")
        save_file.close()
    except:
        print("Error creating save file request")
        exit()

# Open source load name
    """sites_file_name = loadname
    try:
        sites_file = open(sites_file_name, "r")
    except:
        print(f"Could not open loadname{sites_file_name}")"""


# #Open source file
    sites_file_name = Web_List
    try:
        sites_file = open(sites_file_name, "r")
    except:
        print(f"Could not open file {sites_file_name}")
        exit()
    else:

#Read content on file
        addresses = sites_file.readlines()

#Iterate though the list
    for address in addresses:
        address = address.strip()

#Get websites status
        newurl = "https://" + address
        status = ""
        try:
            response = requests.get(newurl, timeout=HTTP_TIMEOUT)
            status = str(response.status_code)
        except:
            status = "Website Connection Failed"
        finally:
            print(f"Website: {address}, Status: {status}")
            status_code = address + "," + status
            status_list.append(status_code)
    print(status_list)

# Iterate through the status list and save to the ouput file
    for element in status_list:
        try:
            save_file = open(save_file_name, 'a')
        except:
            print("Can not open save file")
        try:
            save_file.write(element + '\n')
        except:
            print("Failed to write to save file")
        try:
            save_file.close()
        except:
            print("Failed to close file")

def list(filename):
    #filename = Web_List
    sitelist = []
#open a file
    site_file = open(filename, "r")
    for line in site_file.readlines():
# Read each line
        sitelist.append(line.strip())
    return sitelist

def save(filename, data):
    print("Saving data")
    print(data)
# saves a dictionary as JSON
    if os.path.exists(filename):
        save_file = open(filename, "r")
        old_list = save_file.readlines()
        save_file.close()
    else:
        old_list = []
    save_file = open(filename, "w")
    new_list = old_list
    new_list.append(data)
    (new_list, save_file)
    save_file.close()

def save(filename, data):
    print("Saving data")
    print(data)
    # saves a dictionary as JSON
    if os.path.exists(filename):
        save_file = open(filename, "r")
        old_list = json.load(save_file)
        save_file.close()
    else:
        old_list = []
    save_file = open(filename, "w")
    new_list = old_list
    new_list.append(data)
    print(new_list)
    save_file.close()

def main():
    print("Welcome to Vortex FAMILIA!")
    #check()
    websites = list(Web_List)
    for site in websites:
        print(site)

if __name__ == "__main__":
    main()

