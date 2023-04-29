#!/usr/bin/python3
'''list 10 commits (from the most recent to oldest) of the repository
rails by the user rails
'''

import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
