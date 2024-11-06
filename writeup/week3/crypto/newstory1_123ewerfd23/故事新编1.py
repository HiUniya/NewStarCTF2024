from hashlib import md5
zen1  = '''
BEAUTIFUL IS BETTER THAN UGLY.
EXPLICIT IS BETTER THAN IMPLICIT.
SIMPLE IS BETTER THAN COMPLEX.
COMPLEX IS BETTER THAN COMPLICATED.
FLAT IS BETTER THAN NESTED.
SPARSE IS BETTER THAN DENSE.
FLAGA IS VEGENERE
READABILITY COUNTS.
SPECIAL CASES AREN'T SPECIAL ENOUGH TO BREAK THE RULES.
ALTHOUGH PRACTICALITY BEATS PURITY.
ERRORS SHOULD NEVER PASS SILENTLY.
UNLESS EXPLICITLY SILENCED.

'''
key1 = 'subtitution'
def enc1(plaintext, key):
    def shift_char(c, k):
        return chr(((ord(c) - ord('A') + (ord(k) - ord('A'))) % 26) + ord('A'))

    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            ciphertext.append(shift_char(char, key[key_index % len(key)]))
            key_index += 1
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)
print('enc = \'\'\'' + enc1(zen1, key1)+'\'\'\'')
flag = b'flag{'+md5(zen1.encode()).hexdigest().encode()+b'}'
print(flag)
#----------------------------------------------
enc = '''
TYBNBBZNT WF TYUMMK NAIB HYFZ.
XFIFBKWG AM CXBMYK BVNF CNITBWBB.
GVEJMX QL VXBHRJ NITV VIFXZRP.
WPFXEYQ QG OWNUXZ MBTV QBEJMBKTNXL.
TYSN JL JXNMMF GZUO GMLNXL.
GCSLTX QL VXBHRJ NITV WYGAS.
SDUHT QL PXOSAWLF
KMTXTJWYANZ VWNHMA.
GCWWJTT VULMG NJYO'M AIYVQOY WHPNOA NH JFRSE UAM KOEMG.
NDNIHCZB IZOPLCDTTBNR JSNLM QNZBNR.
MFEGLT LPHOEL BRNYS IILM LQZRFNMR.
CGFXAG RPJMBKBNEG GVDYOVMW.
'''