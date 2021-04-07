"""
    python script to return html text from a webpage
"""

import requests
from bs4 import BeautifulSoup
url = "https://www.theguardian.com/technology/2019/nov/12/history-as-a-giant-data-set-how-analysing-the-past-could-help-save-the-future"

result = requests.get(url)
html_page = result.content
soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ""

blacklist = [
    '[document',
    'noscript',
    'html',
    'meta', 
    'head',
    'input',
    'script',
    'style'
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print(output)