# Amy

import os

clear = lambda: os.system('cls')

import requests

def scrape(keywords, sitelist):
    # Test Data
    keywords = ["ramen","udon","saimin"]
    sitelist = ["books.toscrape.com", "bing.com", "duckduckgo.com", "www.websleuths.com"]
    
    # Get data from websites
    found = False
    for site in sitelist:
        url = "https://" + site
        #Make searcher look like user
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

        html_page = requests.get(url, headers=headers)

        for word in keywords:
            if word in html_page.text:
                print(f"Keyword {word} found at {url}")
                found = True

    # Return True or False if keywords are found
    return found

def search(keywords, sitelist):
    # Test Data
    keywords = ["ramen","udon","saimin"]
    sitelist = ["google.com", "bing.com", "duckduckgo.com", "www.websleuths.com"]
    
    # Get data from websites
    for site in sitelist:
        url = "https://" + site
        #Make searcher look like user
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

        for word in keywords:
            url = url + "/search/q=" + word
            html_page = requests.get(url, headers=headers)
            print(html_page.text)

        
        #Google search
            #try:
            #from googlesearch import search
            #except ImportError:
            #print("No module named 'google' found")
 
            # to search
            #query = "Kiely Rodni"
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
    
    # download HTML

    # Translate data to JSON 

    # Pass data to datamanager

def main():
    keywords = []
    sites = []
    search(keywords, sites)

if __name__ == "__main__":
    clear()
    main()