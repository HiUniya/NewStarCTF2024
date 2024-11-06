from Crypto.Util.number import *

flag = b'flag{*********}'
m = bytes_to_long(flag)


def get_prime(bits):
    while True:
        p = getPrime(bits)
        x = (1 << bits) - 1 ^ p
        for i in range(-10, 11):
            if isPrime(x + i):
                return p, x + i, i


p, q, i = get_prime(512)
n = p * q
e = 65537
c = pow(m, e, n)

print("c =", c)
print("n =", n)
print("i =", i)
'''
c = 14859652090105683079145454585893160422247900801288656111826569181159038438427898859238993694117308678150258749913747829849091269373672489350727536945889312021893859587868138786640133976196803958879602927438349289325983895357127086714561807181967380062187404628829595784290171905916316214021661729616120643997
n = 18104347461003907895610914021247683508445228187648940019610703551961828343286923443588324205257353157349226965840638901792059481287140055747874675375786201782262247550663098932351593199099796736521757473187142907551498526346132033381442243277945568526912391580431142769526917165011590824127172120180838162091
i = -3
'''