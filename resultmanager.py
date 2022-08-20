# Vince

from ast import Import
import os
import readline

# assuming result_1 and result_2 are our result outputs

clear = lambda: os.system('cls')

def menu():
    

    pass
    # Compare search results

    list_1=open(filename_1, "r")
    list_2=open(filename_2, "r")
   
  
"""#                         SITE_LIST= "./Samples/websites.txt"readline    import:SITE_LIST as sl"""

    # Compare lists
    results_final = list_1 + list_2  

    """or lists_1.extend(list_2)"""

    print('Merged List:')
    print("results_final")


    """#              Makes changes as needed             list.append(),list.extend(), list(insert)"""


    res= []
    
    
    #save file
    save_file_name = "results_final.csv"
    try:
        save_file = open(save_file_name, "w")
        save_file.close()
    except:
        print("Error creating save file")
        exit()


    

def main():
    menu()

if __name__ == "__main__":
    clear()
    main()