#!/usr/bin/python3

#encoding:utf-8

import requests

s=requests.Session()

url="http://eci-2ze8z01szogk0yudg063.cloudeci1.ichunqiu.com/start"

r=s.get(url)

res=r.content

a=res.find(b'<p id=\"text\">')

b=res.find(b'</p>',a)

answer = res[a+13:b]

url2="http://eci-2ze8z01szogk0yudg063.cloudeci1.ichunqiu.com/submit"


r=s.post(url2,data={'user_input': answer})

print(r.content)