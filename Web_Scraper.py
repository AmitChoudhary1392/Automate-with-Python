# import libraries
import requests
from bs4 import BeautifulSoup

#url of website to query
url="http://quotes.toscrape.com/"

#GET query to get the response
response= requests.get(url)
#print(response.text)           #see output of the GET request

#parse the HTML object using beautifulsoup and lxml
soup=BeautifulSoup(response.text,'lxml')

#print(soup)        #prints the HTML code for the web page

'''Inspect the HTML tags to find the relevant information to scrape.'''

quotes= soup.find_all('span', class_="text")        #lists all the elements for span with text class to get all quotes
authors= soup.find_all('small', class_='author')    # lists all authors for the quotes
tags= soup.find_all('div', class_="tags")           # lists all tags for the quote

for i in range(0, len(quotes)):
    print("Quote: " + quotes[i].text)           #.text removes the HTML tags and displays only the body of the tag
    print("Author: " + authors[i].text)
    print("Tags: ")

    quote_tags=tags[i].find_all('a', class_='tag')      #find all tags for a particular quote.
    for quote_tag in quote_tags:
        print(quote_tag.text)




