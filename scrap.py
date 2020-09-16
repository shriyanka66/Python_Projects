import requests
from bs4 import BeautifulSoup as bs
import pprint

response = requests.get('https://news.ycombinator.com/news')
bs1 = bs(response.text, 'html.parser')
links = bs1.select('.storylink')
stext = bs1.select('.subtext')


def hacker_list(links, stext):
    hl = []
    for i, item in enumerate(links):
        title = item.getText()
        reference = item.get('href', None)
        votes = stext[i].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hl.append({'title': title, 'link': reference, 'votes': points})
    return hl

pprint.pprint(hacker_list(links,stext))

