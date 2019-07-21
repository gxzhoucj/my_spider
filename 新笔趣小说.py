# -*- coding: utf-8 -*-
#开发人员：zhoucj

import requests
from lxml import etree
import re
import time

header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

def get_etree_html():
    """获取目录页内容"""
    url = "http://www.xinbqg.com" + num
    html = requests.get(url, headers=header).text
    etree_html = etree.HTML(html)
    return etree_html

def get_litle(etree_html):
    """获取书名"""
    title = etree_html.xpath('//div/h1')
    title = str(title[0].text)
    return title

def get_mulist(etree_html,i):
    """获取目录"""
    Mulist = etree_html.xpath('//dd/a')
    mulist = Mulist[i].text
    return mulist

def get_totle(etree_html):
    """获取总章数"""
    Mulist = etree_html.xpath('//dd/a')
    num=len(Mulist)
    return num

def get_NR(etree_html,i):
    """获取小说内容"""
    Nrlist = etree_html.xpath('//dd/a/@href')
    nrurl = "http://www.xinbqg.com" + Nrlist[i]
    html2 = requests.get(nrurl, headers=header).text
    pat=r'&nbsp;&nbsp;&nbsp;&nbsp;'
    pat2=r'<br /><br />'
    html2=re.sub(pat,'',html2)
    html2 = re.sub(pat2, '\n', html2)
    etree_html2 = etree.HTML(html2)
    Nrlist2 = etree_html2.xpath('//div[@id="content"]')
    NR=Nrlist2[0].text
    return NR

def lode(litle,etree_html,k):
    """下载小说"""
    for i in range(0,k):
        mulist = get_mulist(etree_html,i)
        print("正在下载:"+mulist)
        NR = get_NR(etree_html,i)
        with open('./小说/' + str(litle)+ '.txt', 'a+') as f:
            f.write(mulist)
            f.write('\n')
            f.write(NR)
            f.write('\n''\n')

def spider(num,k):
    """爬取小说"""
    etree_html = get_etree_html()
    litle=get_litle(etree_html)
    totle = int(get_totle(etree_html))

    if k != 0:
        k= k
    else:
        k=totle

    print("准备下载：" + litle + ",共" + str(k) + "章")
    time.sleep(2)
    lode(litle, etree_html, k)

if __name__ == '__main__':
    print("1、请到新笔趣阁查找喜欢的小说：http://www.xinbqg.com")
    num = str(input("2、输入小说编号（网址后面的数字,如/0/455/）："))
    k=int(input("3、请输入需要下载的章数，全部下载则输入0："))
    spider(num,k)

    print("___________________*_下载完成_*______________________")
    print("_*_保存在：/home/zhoucj/PycharmProjects/spider/小说_*_")
