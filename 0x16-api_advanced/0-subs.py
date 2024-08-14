#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns
the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent':'0-subs.py/1.0'}

    try:
        response = requests.get(url=url,
                                headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            response = response.json()
            return response['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
