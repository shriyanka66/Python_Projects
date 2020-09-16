import requests
from bs4 import BeautifulSoup as bs
import pprint


def sort_hnlist(hlist):
    return sorted(hlist, key = lambda k : k['votes'], reverse=True)


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
    return sort_hnlist(hl)


for i in range(2,17):
    response = requests.get(f'https://news.ycombinator.com/news?p={i}')
    bs1 = bs(response.text, 'html.parser')
    links = bs1.select('.storylink')
    stext = bs1.select('.subtext')
    pprint.pprint(print(f'Following articles are found on page: {i}', hacker_list(links, stext)))








