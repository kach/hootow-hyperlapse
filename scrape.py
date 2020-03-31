import requests
from bs4 import BeautifulSoup
import shutil

import sys
from api_key import api_key

response = requests.get(
    'https://api.flickr.com/services/rest/',
    params={
        'method': 'flickr.photos.search',
        'api_key': api_key,
        'text': 'stanford hoover tower',
        'sort': 'relevance',
        'page': sys.argv[1],
        'license': '1,2,4,5,7,8,9,10'
    }
)
xml = response.text
soup = BeautifulSoup(xml, 'html.parser')

with open('attribs.txt', 'a') as attribs:
    for photo in soup.find_all('photo'):
        url = 'https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}_z.jpg'.format(**{
            'farm_id': photo['farm'],
            'server_id': photo['server'],
            'id': photo['id'],
            'secret': photo['secret']
        })
        attribs.write(photo['owner'] + '\n')
        print(url)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('imgs/' + url.split('/')[-1], 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
