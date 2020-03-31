import requests
from bs4 import BeautifulSoup
from api_key import api_key

def get_name(NSID):
    response = requests.get(
        'https://api.flickr.com/services/rest/',
        params={
            'method': 'flickr.people.getInfo',
            'api_key': api_key,
            'user_id': NSID
        }
    )
    xml = response.text
    soup = BeautifulSoup(xml, 'html.parser')
    return (soup.find('username').text, soup.find('profileurl').text)

with open('attribs.txt') as attribs:
    with open('attribs-names.txt', 'w') as out:
        for line in attribs:
            name, url = get_name(line[:-1])
            print(url)
            out.write('%s (%s)\n' % (name, url))
