#!/usr/bin/python3
'''
Recurse function find the words inside the title
'''
import re
import requests


def print_result(obj):
    if not obj:
        return obj
    for elem in sorted(obj.items()):
        print('{}: {}'.format(elem[0], elem[1]))
    return obj


def count_words(subreddit, word_list, after=None, obj={}):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)\
                  AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    #print(after)
    #print(obj)
    if after is None:
        request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=100'
                               .format(subreddit), headers=headers)
        if request.status_code != 200:
            return None
        data = request.json().get('data')
        childrens = data.get('children')
        if not childrens:
            return None
        if not word_list:
            return None

        for c in childrens:
            for word in word_list:
                count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word),
                            c.get('data').get('title'), re.IGNORECASE))
                if count > 0:
                    obj[word] = count
        if data.get('after') is None:
            print_result(obj)

        count_words(subreddit, word_list, data.get('after'), obj)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
        request = requests.get(url.format(subreddit, after), headers=headers)
        data = request.json().get('data')
        childrens = data.get('children')

        for c in childrens:
            for word in word_list:
                count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word),
                            c.get('data').get('title'), re.IGNORECASE))
                if count > 0:
                    if word in obj:
                        obj[word] += count
                    else:
                        obj[word] = count

        if data.get('after') is None:
            print_result(obj)
        else:
            count_words(subreddit, word_list, data.get('after'), obj)
    #return obj
