#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:59:42 2020

@author: mgao
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'

r = requests.get(url, timeout = 30)

print(r.status_code)

print(r.text)

print(r.encoding)

r.encoding = 'utf-8'

print(r.text)

url = '这里输入你的想要爬取的url'

def GetHTML(url, timeout = 30):
    try:
        r = requests.get(url, timeout = timeout)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')
        return ''
    
url = 'https://www.baidu.com'
soup = BeautifulSoup(GetHTML(url), 'html.parser')

print(soup.prettify())

print(soup.a)

for a in soup.find_all('a'):
    print(a)
    
print(a.get('href'))

print(a['href'])

a = soup.find('a')

print(a.parent)

print(a.parents)

for i in a.parents:
    print(i)

# 首先先随便获取一个标签
a = soup.find('a')
# 获取该标签的第一个父节点
a.parent
# 获取该标签的全部父节点
a.parents # 生成一个迭代器
# 获取该标签的直接子节点
a.children # 生成一个迭代器
# 获取该标签的全部子孙节点
a.descendants # 生成一个迭代器
# 获取该标签的平行节点
a.next_sibling
# 获取该标签的全部平行节点
a.next_siblings # 生成一个迭代器








