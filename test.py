import requests
from bs4 import BeautifulSoup

def get_all_hrefs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    hrefs = []

    for element in soup.find_all(src=True):
        href = element.get('src')
        if href:
            hrefs.append(href)

    return hrefs

# Example usage
url = 'https://www.ucsfdentalcenter.org/'
# all_hrefs = get_all_hrefs(url)
response = requests.get(url)

# print(all_hrefs)
# print(len(all_hrefs))

file_path = '111.html'

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(response.text)