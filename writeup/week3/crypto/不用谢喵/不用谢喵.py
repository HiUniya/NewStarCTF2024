from Crypto.Cipher import AES
from Crypto.Util.number import *
import os

KEY = b"fake_key_fake_ke"
FLAG = "flag{fake_flag_fake_flag}"  

def decrypt(c):
    AES_ECB = AES.new(KEY, AES.MODE_ECB)
    decrypted = AES_ECB.decrypt(long_to_bytes(c))

    return decrypted.hex()

def encrypt():
    iv = os.urandom(16)
    AES_CBC = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = AES_CBC.encrypt(FLAG.encode())
    print('iv:',iv.hex())

    return iv.hex() + encrypted.hex()

c=encrypt()
print('encrypt:',c)
print('decrypt:',decrypt(int(c,16)))

#encrypt: f2040fe3063a5b6c65f66e1d2bf47b4cddb206e4ddcf7524932d25e92d57d3468398730b59df851cbac6d65073f9e138
#什么是AES啊😭，求求你帮我解密吧，我什么都会做的！！！！！😭

'''
什么都会做？那就去学习一下AES吧……
我这次就先给你解一下好了，不用谢喵
decrypt: f9899749fec184d81afecd35da430bc394686e847d72141b3a955a4f6e920e7d91cb599d92ba2a6ba51860bb5b32f23b
这对吗？哦不对不对，哦对的对的。
'''