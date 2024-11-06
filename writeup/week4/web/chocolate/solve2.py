# a = b'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>\xe8\x83\x8c\xe6\x99\xaf\xe5\x9b\xbe\xe7\x89\x87\xe7\xa4\xba\xe4\xbe\x8b</title>\r\n</head>\r\n<body style="background-image: url(\'choco.gif\'); background-size: cover;">\r\n\xe6\x88\x96\xe8\xae\xb8\xe5\x8f\xaf\xe4\xbb\xa5\xe9\x97\xae\xe9\x97\xae\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x9c\x80\xe4\xb8\xb0\xe5\xaf\x8c\xe7\x9a\x84 Mr.0ldStar, \xe4\xbb\x96\xe5\x9c\xa80ldStar.php'

# str(a,encoding="utf-8")

# print(str(a,encoding="utf-8"))

# <!DOCTYPE html>
# <html>
# <head>
#     <title>背景图片示例</title>
# </head>
# <body style="background-image: url('choco.gif'); background-size: cover;">
# 或许可以问问经验最丰富的 Mr.0ldStar, 他在0ldStar.php

# http://eci-2zegzaz5l01s0yi0n228.cloudeci1.ichunqiu.com/0ldStar.php?num=1337\0000

# 什么?想做巧克力? // 可可液块 (g): 1337033 // gur arkg yriry vf : pbpbnOhggre_fgne.cuc, try to decode this 牢师傅如此说到

# gur arkg yriry vf : pbpbnOhggre_fgne.cuc,

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

encrypted_text = "gur arkg yriry vf : pbpbnOhggre_fgne.cuc"
decrypted_text = rot13(encrypted_text)
print(decrypted_text)

# the next level is : cocoaButter_star.php