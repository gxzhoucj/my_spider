# -*- coding: utf-8 -*-
#开发人员：zhoucj

import requests
import re

header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

def get_html(i):
    """输入页数，返回html"""
    i = i*10
    url="https://maoyan.com/board/4?offset="+str(i)
    html=requests.get(url,headers=header).text
    return html

def parse_html(html):
    pattern = re.compile('<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">上映时间：(.*?)</p> .*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>',re.S)
    item = re.findall(pattern,html)
    for item in item:
        yield {
            '名字': item[0],
            '演员': item[1].strip()[3:],
            '上映': item[2],
            '评分': item[3] + item[4]
        }

if  __name__ == '__main__':
    k=int(input("下载的页数："))
    for i in range(0,k):
        print("第"+str(i+1)+"页：")
        html=get_html(i)
        for k in parse_html(html):
            for key,value in k.items():
                print(key,value)
            print("——————————————————————————————————————————")