# -*- coding: utf-8 -*-
#开发人员：zhoucj


from urllib import request
from urllib import parse
import re

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

word=input("请输入：")

formdata={
	"i":word,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"15503049709404",
	"sign":"3da914b136a37f75501f7f31b11e75fb",
	"ts":"1550304970940",
	"bv":"ab57a166e6a56368c9f95952de6192b5",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTIME",
	"typoResult":"false"
}

data=parse.urlencode(formdata).encode(encoding='utf-8')

req=request.Request(url,data=data,headers=header)

resp=request.urlopen(req).read().decode()
prt=r'"tgt":"(.*?)"}]]}'
result=re.findall(prt,resp)

print("结果是:"+result[0])

