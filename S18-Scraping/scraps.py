import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest')
# res2 = requests.get('https://news.ycombinator.com/newest?next=34772114&n=31')
soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup)
# print(soup.find_all('div'))
# print(soup.find_all('a'))

# find the first a
# print(soup.find('a'))


# print(soup.find(id='score_20514755'))

# css selector
# print(soup.select('div'))
# print(soup.select('.score'))

links = soup.select('.titleline')
subtext = soup.select('.subtext')
# links2 = soup2.select('.titleline')
# subtext2 = soup2.select('.subtext')

# mega_link = links + links2
# mega_subtext = subtext + subtext2
# id from html become an attribute
# print(votes[0].get('id'))


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['point'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for ind, item in enumerate(links):
        title = links[ind].getText()
        href = links[ind].get('href')
        print(href)
        vote = subtext[ind].select('.score')
        if len(vote):
            if (point := vote[0].getText()) == '1 point':
                point = int(point.replace(' point', ''))
            else:
                point = int(point.replace(' points', ''))

            if point > 5:
                hn.append(
                    {
                        'title': title,
                        'href': href,
                        'point': point,
                    }
                )

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
