#!/usr/bin/python3
"""A script to Print the title of the top 10 hot posts for a subreddit"""

import json
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Print the title of the top 10 hot posts"""
    headers = {'User-Agent': 'Chrome/124.0.0.0 Safari/537.36'}
    if after is not None:
        url = f'https://www.reddit.com/r/{subreddit}/top.json?after={after}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/top.json'
    r = requests.get(url, headers=headers, allow_redirects=False)
    if (r.status_code != 200):
        return
    top_posts = r.json()['data']['children']
    hot_list += [(post['data']['title']) for post in top_posts]
    next_page = r.json()['data']['after']
    if next_page is None:
        res = search_count(hot_list, word_list)
        if res == {}:
            return
        [print(f"{k}: {v}") for k, v in res.items()]
    else:
        count_words(subreddit, word_list, hot_list, after=next_page)


def search_count(hot_list, word_list):
    """Count the occurrence of a word in the hot_list"""
    res = {}
    for word in word_list:
        l_word = word.lower()
        count = res.get(l_word, 0)
        for post in hot_list:
            count += post.lower().split().count(l_word)
        if count:
            res[l_word] = count
        res = dict(sorted(res.items(), key=lambda x: (-x[1], x[0])))
    return res
