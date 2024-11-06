# cocoaLiquor=123&cocoaButter=123&darkCocoaPowder=123&powderedSugar=111

import requests

# 要发送POST请求的网址
url = 'http://eci-2zegzaz5l01s0yi0n228.cloudeci1.ichunqiu.com/cocoaButter_star.php'

# POST请求的头部信息
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

params = {
	'cat': "M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2",
	'dog': "M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2"
}

data = {
	'moew': '0e215962017',
	'wof' : '60066549'
}


response = requests.post(url,headers=headers, params=params, json=data)

cc = response.content

print(str(cc,encoding="utf-8"))