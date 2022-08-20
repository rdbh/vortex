# Ruben

import os
import json
import websitemanager as websites
import keywordmanager as kwm
import resultsmanager_2_Vince as rsm
#import searcher

clear = lambda: os.system('cls')

def caseObj(): #Building the case dictionary/json object
    record = {"name":[], "keywords":[], "results":[], "user":[], "sites":[]}
    modify_key = "name"
    record[modify_key] = record.get(modify_key,0) + 1
    record["keywords"] = kwm.load()
    record["results"] = rsm.load()
    record["user"] = userdict()
    record["sites"] = websites.list()

    '''def obj_save(caseObj.json, record):
    print("Saving data")
    # saves a dictionary as JSON
    if os.path.exists(caseObj.json):
        save_file = open(caseObj.json, "r")
        old_list = json.load(save_file)
        save_file.close()
    else:
        old_list = []
    save_file = open(caseObj.json, "w")
    new_list = old_list
    new_list.append(record)
    json.dump(new_list, save_file)
    save_file.close()'''
 
def getCase(casename):
    # Find case filename
    filename = "case1.json"
    caseObj = {
        "name":"case1",
        "keywords":"./vortex.json",
        "results":"./Results_1.json",
        "user":"Al Merino",
        "websites":"./Project Vortex/Osint_WebsiteList.txt" 
    }
    return caseObj


def userdict():
    userdict = {"FName":[], "LName":[], "Email":[]}
    get_fname = input("Type the first name of the user needing an alert: ")
    get_lname = input("Type the last name of the user needing an alert: ")
    get_email = input("Type the email address of the user needing an alert: ")

    userdict["FName"] = get_fname
    userdict["LName"] = get_lname
    userdict["Email"] = get_email

    with open('users_config.txt', 'w') as convert_file:
        convert_file.write(json.dumps(userdict))
    

def keywordmgr(keyword):
    #key_name = input("What keywords are you looking for? ")
    if (caseObj.key("keywords") == keyword):
        print("Here is a list of records associated with that keyword: ") + caseObj.get("keywords")

def getWebsites(site):
    #site_name = input("What website are you looking for? ")
    if (caseObj.key("sites") == site):
        print("Here are a list of websites and associated cases that have used that website: ") + caseObj.get("sites")
    
def results(case):
    result_name = input("What case are you looking for? ")
    if (caseObj.key("name") == result_name):
        print("Here are a list of results associated with that case: ") + caseObj.get("results")

def user_searches():
    user_name = input("What user are you looking for? ")
    if (caseObj.key("user") == user_name):
        print("Here are the records associated with that user: ") + caseObj.get("user")
    pass

    '''def manager():
    pass
    # Alerts created
    '''#Use Alert format as defined in the alert.py file'''
    # Alerts sent
    '''#Send Alert if keyword is discovered'''
    '''-----------------------------------------------------
    Now I'm thinking maybe i just handle the alerts as a whole here, sending the alerts to the respective users and storing alerts sent'''

    # Searches conducted
    '''#Validate that the searches being conducted have not already been done
        #compare the keyword(keywordmanager) to website '''

def main():
    #manager()
    pass

if __name__ == "__main__":
    clear()
    main()