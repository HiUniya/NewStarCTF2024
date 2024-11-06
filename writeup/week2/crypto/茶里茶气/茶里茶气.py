from Crypto.Util.number import *

flag = "flag{*****}"
assert len( flag ) == 25

a = ""
for i in flag:
    a += hex(ord(i))[2:]
l = int(a,16).bit_length()
print("l  =" , l )

v0 = int(a,16)>>(l//2)
v1 = int(a,16)-(v0<<(l//2))
p = getPrime(l//2+10)

v2 = 0
derta = 462861781278454071588539315363
v3 = 489552116384728571199414424951
v4 = 469728069391226765421086670817
v5 = 564098252372959621721124077407
v6 = 335640247620454039831329381071
assert v1 < p and v0 < p and derta < p and v3 < p and v4 < p and v5 < p and v6 < p 

for i in range(32):
    v1 += (v0+v2) ^ ( 8*v0 + v3 ) ^ ( (v0>>7) + v4 ) ; v1 %= p
    v0 += (v1+v2) ^ ( 8*v1 + v5 ) ^ ( (v1>>7) + v6 ) ; v0 %= p
    v2 += derta ; v2 %= p

print( "p  =" , p  )
print( "v0 =" , v0 )
print( "v1 =" , v1 )

"""
l  = 199
p  = 446302455051275584229157195942211
v0 = 190997821330413928409069858571234
v1 = 137340509740671759939138452113480
"""