import config
import os, json, uuid

import filehandler as fh
import websitemanager as wsm
import keywordmanager as kwm
import resultsmanager_2_Vince as rsm
#import searcher


def clear(): return os.system('cls')
CASE_PATH = config.SAVE_DIR + "/" + config.CASE_FILE

current_case = {
    "id":"0",
    "name":"select case",
    "description":"",
    "keywords":"./",
    "results":"./",
    "user":"",
    "websites":"./" 
}

def caseObj():  # Building the case dictionary/json object
    record = {"name": [], "keywords": [],
              "results": [], "user": [], "sites": []}
    modify_key = "name"
    record[modify_key] = record.get(modify_key, 0) + 1
    record["keywords"] = kwm.load()
    record["results"] = rsm.load()
    record["user"] = userdict()
    record["sites"] = wsm.list()

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

# Cases

def create_case(new_case: dict):
    global current_case
    if isinstance(new_case, dict):
        new_case["id"] = str(uuid.uuid4())
        file_path = CASE_PATH
        fh.saveJson(file_path, [new_case])
        current_case = new_case
    else:
        new_case = {
            "name": "Choose case"
        }
    return new_case

def get_case_id(case_id: str):
    # Find case filename
    file_path = CASE_PATH
    cases = fh.loadJson(file_path)
    for case in cases:
        if case["id"] == case_id:
            return case
    return {"name": "Case not found"}

def get_case_name(case_name: str):
    # Find case filename
    file_path = CASE_PATH
    cases = fh.loadJson(file_path)
    for case in cases:
        if case["name"] == case_name:
            return case
    return {"name": "Case not found"}

def get_cases(filename: str = CASE_PATH):
    cases = fh.loadJson(filename)
    return cases

def get_case_names(filename: str = CASE_PATH):
    caseList = []
    cases = fh.loadJson(filename)
    for case in cases:
        caseList.append(case["name"])
    return caseList

def update_case(update_case):
    case_list = get_cases()
    for test_case in case_list:
        if update_case["id"] == test_case["id"]:
            case_list.remove(test_case)
            case_list.append(update_case)


def delete_case(old_case: dict):
    case_list = get_cases()
    for case in case_list:
        if old_case["id"] == case["id"]:
            case_list.remove(case)
    return fh.saveJson(CASE_PATH, case_list, "o")


# Keywords


# Results


def results(case):
    result_name = input("What case are you looking for? ")
    if (caseObj.key("name") == result_name):
        print("Here are a list of results associated with that case: ") + \
            caseObj.get("results")

# Websites


def getWebsites(file_path: str = current_case["websites"]):
    #site_name = input("What website are you looking for? ")
    if (caseObj.key("sites") == site):
        print("Here are a list of websites and associated cases that have used that website: ") + \
            caseObj.get("sites")

# Users
def userdict():
    userdict = {"FName": [], "LName": [], "Email": []}
    get_fname = input("Type the first name of the user needing an alert: ")
    get_lname = input("Type the last name of the user needing an alert: ")
    get_email = input("Type the email address of the user needing an alert: ")

    userdict["FName"] = get_fname
    userdict["LName"] = get_lname
    userdict["Email"] = get_email

    with open('users_config.txt', 'w') as convert_file:
        convert_file.write(json.dumps(userdict))

def user_searches():
    user_name = input("What user are you looking for? ")
    if (caseObj.key("user") == user_name):
        print("Here are the records associated with that user: ") + \
            caseObj.get("user")
    pass

    '''def manager():
    pass
    # Alerts created
    '''  # Use Alert format as defined in the alert.py file'''
    # Alerts sent
    '''#Send Alert if keyword is discovered'''
    '''-----------------------------------------------------
    Now I'm thinking maybe i just handle the alerts as a whole here, sending the alerts to the respective users and storing alerts sent'''

    # Searches conducted
    '''#Validate that the searches being conducted have not already been done
        #compare the keyword(keywordmanager) to website '''


def main():
    pass

if __name__ == "__main__":
    clear()
    main()
