# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 0023 下午 3:47
# @Author  : dingqin

import requests

def http_request(urls,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization':token}
    if method=='get':
        result=requests.get(url=urls,json=data,headers=header)
    else:
        result=requests.post(url=urls,json=data,headers=header)
    return result.json()








