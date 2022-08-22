import os
import json

## JSON
def loadJson(filePath):
    newList = []
    try:
        loadFile = open(filePath, "r")
    except:
        return f"Error opening {filePath}"
    newList = json.load(loadFile)
    loadFile.close()
    # returns a list

    return newList

def saveJson(filePath: str, data: list):
    # Saves data to a file as a JSON object
    # Expects a list of dictionaries
    if os.path.exists(filePath):
        try:
            saveFile = open(filePath, "r")
            oldList = json.load(saveFile)
            saveFile.close()
        except: 
            return "Error opening existing file"    
    else:
        oldList = []
    try:
        saveFile = open(filePath, "w")
    except:
        return f"Could not write to {filePath}"
    newList = oldList
    for obj in data:
        newList.append(obj)
    json.dump(newList, saveFile)
    saveFile.close()
    return "JSON Saved"

## Strings
def saveStr(filePath: str, data: list):
    # Saves data to a file as a string on each line
    # Expects a list of strings
    if os.path.exists(filePath):
        try:
            saveFile = open(filePath, "a")
        except: 
            return f"Error opening {filePath}"
    else:
        try:
            saveFile = open(filePath, "w")
        except:
            return f"Could not create {filePath}"
    for obj in data:
        saveFile.write(obj+"\n")
    saveFile.close()
    return "Strings Saved"

def testStr():
    data = ["apple", "pear","Pumpkin", "caterpillar"]
    filePath = "test1.txt"
    return saveStr(filePath, data)
    return loadStr(filePath)

def main():
    print(testStr())
    #print(testJson())

if __name__ == "__main__":
    main()
