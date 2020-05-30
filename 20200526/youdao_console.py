#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:30:54 2020

@author: mgao
"""

import requests
import json
import hashlib
import time
import random

class YouDao():
    def __init__(self, key):
        self.key = key
        self.request_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.post_form = { 
                            'i': 'no', 
                            'from': 'AUTO',
                            'to': 'AUTO',
                            'smartresult': 'dict',
                            'client': 'fanyideskweb',
                            'salt': '15904017366884',
                            'sign': '9726a97600b1cf499141436ea5801e10',
                            'ts': '1590401736688',
                            'bv': '0d5cd29aaa049711c3bd27dc3e8530b2',
                            'doctype': 'json',
                            'version': '2.1',
                            'keyfrom': 'fanyi.web',
                            'action': 'FY_BY_REALTlME'
                        }
        self.headers = {
                        "Cookie": "OUTFOX_SEARCH_USER_ID=1721894360@59.111.179.141; _ntes_nnid=28c86721ce2c2392d0b4bc1c066195c2,1562810189644; OUTFOX_SEARCH_USER_ID_NCOO=1717529083.05212; P_INFO=qducst_xmt@163.com|1572920094|0|other|00&99|shd&1572744638&mail163#shd&null#10#0#0|&0|mail163|qducst_xmt@163.com; JSESSIONID=aaadMecWfzOYVgeMhs8dx; ___rl__test__cookies=1584780646068",
                        "Referer": "http://fanyi.youdao.com/",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                        }

        
    def create_md5(self):
        '''
        生成加密的随机数
        '''
        d = self.key
        m = hashlib.md5()
        u = "fanyideskweb"  #判断是网页还是客户端
        # 由于网页是用的js的时间戳(毫秒)跟python(秒)的时间戳不在一个级别，所以需要*1000
        ts = str(time.time() * 1000)
        f = str(time.time() * 1000) + str(random.randint(1,10))
        c = "Nw(nmmbP%A-r6U3EUn]Aj"
        #根据md5的方式：md5(u + d + f + c)，拼接字符串生成sign参数。
        m.update((u + d + f + c).encode('utf-8'))   #生成加密串
        self.post_form['salt'] = f
        self.post_form['sign'] = m.hexdigest()
        self.post_form['ts'] = ts
        self.post_form['i'] = d
    
    def translate(self):
        self.create_md5()
        response = requests.post(self.request_url, data=self.post_form, headers=self.headers)
        trans_json = response.text
        trans_dict = json.loads(trans_json)
        result = trans_dict['translateResult'][0][0]['tgt']
        print(result)
    
if __name__ == "__main__":
    content = input("请输入:  ")
    youdao = YouDao(content)
    youdao.translate()
        
        

        
        
        







