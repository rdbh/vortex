
import os
import json

clear = lambda: os.system('cls')

def load(filename):
    # print("loading data")
    # returns a dictionary
    load_file = open(filename, "r")
    results = json.load(load_file)
    load_file.close()
    
    # returns a list
    return results

def save(filename, data):
    # print("Saving data")
    # print(data)
    # saves a dictionary as JSON
    if os.path.exists(filename):
        save_file = open(filename, "r")
        old_list = json.load(save_file)
        save_file.close()
    else:
        old_list = []
        save_file = open(filename, "w")
    new_list = old_list
    #append dat with oldlist
    new_list.append(data)
    json.dump(new_list, save_file)
    save_file.close()
    
    # Remove duplicate results to prvent duplicate alerts.

"""res = []
    for i in results_1:
        if i not in res:
        res.append(i)
        
        else:
            save_file.close"""


def main():
    data =  {"Result_1"}
    save("./Results_1.json", data )
    print(load("./Results_1.json")) 

if __name__ == "__main__":
    clear()
    main()