import os
import json
import filehandler as fh

clear = lambda: os.system('cls')

def delete(filename: str, data: str):
    # deletes all instances of a keyword
    oldList = fh.loadJson(filename)
    newList = oldList
       
    # Remove the word from the list
    for testkey in oldList:
        print(testkey)
        print(data)
        if data == testkey["keyword"]:
            print(f"{data} found")
            newList.remove(testkey)
            
        else:
            print(f"{data} not found")

    # Save the modified data
    print(newList)
    return fh.saveJson(filename, newList, "o")

def load(filename: str):
    print("loading data")
    # returns a dictionary
    load_file = open(filename, "r")
    keywords = json.load(load_file)
    load_file.close()
    # returns a list
    return keywords

def save(filename: str, data: list):
    if isinstance(data, dict):
        data = [data]
    return fh.saveJson(filename, data)

def test(data):
    testFile = "./test/key_test1.json"
    #return save(testFile, data)
    return delete(testFile, data)

def main():
    word = {
        "keyword":"train bomb",
        "language":"english",
        "description":"Rail attack",
        "translation":"",
        "type":"entity"
    }
    words = [{
        "keyword":"SVIED",
        "language":"english",
        "description":"enemy self kill",
        "translation":"",
        "type":"activity"
    },
    {
        "keyword":"car_attack",
        "description":"ground attacks",
        "language":"english",
        "translation":"",
        "type":"activity"
    }]
    #print(test(words))
    print(test("SVIED"))

    print("-" * 10)

if __name__ == "__main__":
    clear()
    main()