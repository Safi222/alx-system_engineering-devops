#!/usr/bin/python3
"""A script to Print the title of the top 10 hot posts for a subreddit"""

import requests


def top_ten(subreddit):
    """Print the top 10 hot posts's tiltle"""
    headers = {'User-Agent': 'Chrome/124.0.0.0 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    r = requests.get(url, headers=headers, allow_redirects=False)
    if (r.status_code == 200):
        hot_list = r.json()['data']['children']
        [print(post['data']['title']) for post in hot_list]
    else:
        print(None)
