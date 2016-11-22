#-*-coding:utf8-*-

import requests
import json

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}

jscontent = requests.get('http://coral.qq.com/article/1165021596/comment?commentid=0&reqnum=50',\
                         headers=head).content
jsDict = json.loads(jscontent)
jsData = jsDict['data']
comments = jsData['commentid']
for each in comments:
    print each['content']