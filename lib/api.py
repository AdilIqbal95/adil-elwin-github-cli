import requests
from .repo import Repository

def fetch_repos(username):
    ''' Call to Github API '''
    URL = f'https://api.github.com/users/{username}/repos'
    req = requests.get(URL)
    for data in req.json():
        Repository(data)
    return data