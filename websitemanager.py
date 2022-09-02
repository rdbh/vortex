import filehandler as fh
import os
import requests


########################################
# WebsiteManager.PY              TJ
# Get, Save, Sort Website
# List websites
# Get list from file MAYBE THIS ONE: (https://start.me/p/gy0NXp/open-source-intelligence-osint)
# or
# Get the list from a search engine
# or
# Get the list from other search results
# or
# Get the list from start.me
#####################################################################


HTTP_TIMEOUT = 10
WEB_LIST = "./data/Osint_WebsiteList.txt"


def clear(): return os.system('cls')


def check(loadname):
    # Variable Scope
    status_list = []

# Save results as CSV
    save_file_name = "WebSites_VORTEX.csv"
    try:
        save_file = open(save_file_name, "w")
        save_file.close()
    except:
        print("Error creating save file")
        return

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
        return
    else:

        # Read content on file
        addresses = sites_file.readlines()

    # Iterate though the list
    for address in addresses:
        address = address.strip()

        # Get websites status
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
# open a file
    site_file = open(filename, "r")
    for line in site_file.readlines():
        # Read each line
        sitelist.append(line.strip())
    return sitelist

def save(keyword):
    fh.save


def main():
    clear()
    print("Welcome to Vortex FAMILIA!")
    # check()
    websites = list(WEB_LIST)
    for site in websites:
        print(site)


if __name__ == "__main__":
    main()
