from Crypto.Cipher import AES
from Crypto.Util.number import *
import os


Ctext1 = "f2040fe3063a5b6c65f66e1d2bf47b4c"

Dtext2 = "94686e847d72141b3a955a4f6e920e7d"

Ptext2 = int(Ctext1,16)^int(Dtext2,16)

print(long_to_bytes(Ptext2))

"""
b'flag{HOw_c4REfu1'
"""
Ctext2 = "ddb206e4ddcf7524932d25e92d57d346"
Dtext3 = "91cb599d92ba2a6ba51860bb5b32f23b"

Ptext3 = int(Ctext2,16)^int(Dtext3,16)

print(long_to_bytes(Ptext3))

"""
b'Ly_yOu_O65ERve!}'
"""

# flag{HOw_c4REfu1Ly_yOu_O65ERve!}