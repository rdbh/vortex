# Joe

from fileinput import filename
import keyword
import os
import json
clear = lambda: os.system('cls')

# create a save file

def load(filename):
    print("loading data")
    # returns a dictionary
    load_file = open(filename, "r")
    keywords = json.load(load_file)
    load_file.close()
    # returns a list
    return keywords

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
    json.dump(new_list, save_file)
    save_file.close()
 
# write keywords to file
def main():
    vortex = {
        "keyword":"train bomb",
        "language":"english",
        "description":"Rail attack",
        "type":"entity"
    }
    vortex_2 = {
        "keyword":"SVIED",
        "language":"english",
        "description":"enemy self kill",
        "type":"activity"
    }
    vortex_3 = {
        "keyword":"car_attack",
        "language":"english",
        "description":"ground attacks",
        "type":"activity"
    }
  # read keywords from file

  # Saved keywords add to list in txt file for case
  # create new txt file (json) for each keyword list per case
    #save("./vortex.json", vortex)
    #print(load("./vortex.json"))
    #save("./vortex_2.json", vortex_2)
    #print(load("./vortex_2.json"))
    #save("./vortex_3.json", vortex_3)
    #print(load("./vortex_3.json"))
    #delete("./vortex.json","'keyword:plane'")
    data = {"keyword":"attack"}
    delete("./vortex_3.json", data)
    #delete("./vortex_3.json","'keyword':'explosions'")
    print("-" * 10)

# delete keywords from txt file (json) for each keyword list per case
def delete(filename, data):
    # saves a dictionary as JSON
    print("Delete function test")
    if os.path.exists(filename):
        save_file = open(filename, "r")
        old_list = json.load(save_file)
        save_file.close()
    else:
        print(f"Could not find file {filename}")
        return
    
    # Remove the word from the list
    for testkey in old_list:
        print(testkey)
        print(data)
        if data["keyword"] == testkey["keyword"]:
            old_list.remove(testkey)
        else:
            print(f"{data} not found")
    # Save the modified data
    save_file = open(filename, "w")
    json.dump(old_list, save_file)
    save_file.close()
    

if __name__ == "__main__":
    clear()
    main()


# use a file name variable that correlates with each case - used Vortex.json as file name

    # Get new keywords - Identify where to get new keywords from by topic.  Create a new file per new case.
        # count keywords per website (?) website manager?

        # list keywords count by website (?) website manager?
    # Sort keywords
    #Inside of each json case file sort by ...
    
        # sort by frequency
        # sort by date
        # sort by name 
