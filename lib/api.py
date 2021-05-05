import requests
from .house import House

URL = 'https://anapioficeandfire.com/api/houses'

def fetch_houses():
    ''' Call to API of Ice and Fire '''
    req = requests.get(URL)
    for data in req.json():
        House(data)
    return data