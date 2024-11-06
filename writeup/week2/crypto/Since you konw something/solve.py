from pwn import xor
#The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths
from Crypto.Util.number import bytes_to_long,long_to_bytes

c=218950457292639210021937048771508243745941011391746420225459726647571

cc = long_to_bytes(c)

for i in range(32,127):
	for j in range(32,127):
		key = chr(i)+chr(j)
		print(xor(cc,key))
