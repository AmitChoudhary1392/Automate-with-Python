# import libraries
import requests
from bs4 import BeautifulSoup

'''*************************** SINGLE PAGE WEB SCRAPER *****************************************'''
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



'''*************************** MULTI-PAGE WEB SCRAPER *****************************************'''
#url of website to query
url2= "https://scrapingclub.com/exercise/list_basic/?page=1"

def web_scraper(url):
    #GET query to get the response
    response_multi= requests.get(url)
    #print(response.text)           #see output of the GET request

    #parse the HTML object using beautifulsoup and lxml
    soup_multi=BeautifulSoup(response_multi.text,'lxml')

    #inspect the HTML tags to identify what to scrape
    items= soup_multi.find_all('div', class_="col-lg-4 col-md-6 mb-4")

    count=1
    #grab the title and price tag from the items
    for i in items:
        item_name= i.find('h4', class_="card-title").text
        item_price= i.find("h5").text

        print('%s) Price: %s, Item Name: %s' % (count, item_price, item_name))
        counter+=1

web_scraper(url2)
# inspect the html page for page navigation
pages= soup_multi.find('ul', class_="pagination")
#store the individaul page links in a list
urls=[]
links= pages.find_all('a', class_='page-link')

for link in links:
    page_num= int(link.text) if link.text.isdigit() else None           # page number contains integer and strings. selecting the string will duplicate the result as it will take to the same page.\n have to put a conditional to select only the integer page number
    
    if page_num !=None:
        x= link.get('href')
        urls.append(x)
        new_url= url2+ x        #build a new Url for each page

    web_scraper(new_url)        #use the function to display results on each page

    print("*"*9 +" Next Page" + "*"*9)