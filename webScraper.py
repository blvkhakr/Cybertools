import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract specific information from the page
    # For example, let's extract and print all the links on the page
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
