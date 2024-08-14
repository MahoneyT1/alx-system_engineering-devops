#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given
subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for
    a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent':'1-top_ten.py'}


    response = requests.get(url=url,
                            headers=headers,
                            allow_redirects=False)

    try:
        data = response.json()
        if response.status_code == 200:
            for post in data.get('data').get('children'):
                print(post.get('data').get('title'))
    except Exception as e:
        print(None)
