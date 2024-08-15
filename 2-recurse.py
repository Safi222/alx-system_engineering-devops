#!/usr/bin/python3
"""A script to Print the title of the top 10 hot posts for a subreddit"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Print the title of the top 10 hot posts"""
    headers = {'User-Agent': 'Chrome/124.0.0.0 Safari/537.36'}
    if after is not None:
        url = f'https://www.reddit.com/r/{subreddit}/top.json?after={after}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/top.json'
    r = requests.get(url, headers=headers)
    if (r.status_code == 200):
        top_posts = r.json()['data']['children']
        hot_list += [(post['data']['title']) for post in top_posts]
        next_page = r.json()['data']['after']
        if next_page is None:
            return hot_list
        return recurse(subreddit, hot_list, after=next_page)
    else:
        return None
