import requests
from bs4 import BeautifulSoup

# with the first page to visit
urls = ["https://www.scrapingcourse.com/ecommerce/"]

# get the page to visit from the list
current_url = urls.pop()

# crawling logic
response = requests.get(current_url)
soup = BeautifulSoup(response.content, "html.parser")

link_elements = soup.select("a[href]")

for link_element in link_elements:
    url = link_element["href"]
    if "https://www.scrapingcourse.com/ecommerce/" in url:
        urls.append(url + "\n")

# initialize the output file
with open('urls.txt', 'w') as file:
    # populating the text file
    for url in urls:
        file.write(url)

print("URLs extracted successfully!!!!!\n")
