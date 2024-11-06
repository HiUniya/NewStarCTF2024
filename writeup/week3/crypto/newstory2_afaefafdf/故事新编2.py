from hashlib import md5
zen2 = '''
IN THE FACE OF AMBIGUITY, REFUSE THE TEMPTATION TO GUESS.
THERE SHOULD BE ONE-- AND PREFERABLY ONLY ONE --OBVIOUS WAY TO DO IT.
ALTHOUGH THAT WAY MAY NOT BE OBVIOUS AT FIRST UNLESS YOU'RE DUTCH.
NOW IS BETTER THAN NEVER.
ALTHOUGH NEVER IS OFTEN BETTER THAN RIGHT NOW.
IF THE IMPLEMENTATION IS HARD TO EXPLAIN, IT'S A BAD IDEA.
IF THE IMPLEMENTATION IS EASY TO EXPLAIN, IT MAY BE A GOOD IDEA.

'''
key2 = 'supersubtitution'
dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def generate_key(message, key):
    for i in range(len(message)):
        if message[i].isalpha() == False:
            pass
        else:
            key += message[i]
    return key
def enc2(message, key):
    message = message.upper()
    key = key.upper()
    key_new = generate_key(message, key)
    cipher_text = ''
    i = 0
    for letter in message:
        if letter.isalpha():
            x = (dict1[letter]+dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]
        else:
            cipher_text += letter
    return cipher_text
print('enc = \'\'\'' + enc2(zen2, key2)+'\'\'\'')
flag = b'flag{'+md5(zen2.encode()).hexdigest().encode()+b'}'
print(flag)
#----------------------------------------------
enc = '''
AH ILV XUDX WY UFJWTCVMF, VJFWWS YHQ UMSJBTRZSS NG KNLWL.
XTTKE LPCHER HY SFW-- TUH GVWMSLLEMC CAPY BQT --FFAMFUT HYM GZ BC VX.
OMOPCOYD TFTH ZOG FAJ GVH VK VUCIHQS YF FGEGM VRZFNA MIM'RX ICKUA.
HBH MK TCHNVV WBTP URJAZ.
SMXAHYXA UEIRV DW FFEXU PYZARV OLRV JWLAX APA.
BY XYX PMCCMSLGGOPQTG PW PMGO XA IKILTQB, VB'K H BRG BRIX.
XQ TPR QFHLFMHVWETQTG PW MMHJ XA IKILTQB, VB EEY TC T USLS TDMN.
'''