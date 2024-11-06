from pwn import xor
#The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths
from Crypto.Util.number import bytes_to_long

key = ?? #extremely short
FLAG = 'flag{????????}'
c = bytes_to_long(xor(FLAG,key))

print("c={}".format(c))

'''
c=218950457292639210021937048771508243745941011391746420225459726647571
'''

