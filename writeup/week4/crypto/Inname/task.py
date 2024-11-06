from Crypto.Util.number import *
from gmpy2 import *
import random

def pad(msg, nbits):
    pad_length = nbits - len(msg) * 8 - 8
    assert pad_length >= 0
    pad = random.getrandbits(pad_length).to_bytes((pad_length + 7) // 8, "big")
    padded_msg = pad[:len(pad)//2] + b"\x00" + msg + pad[len(pad)//2:]

    return padded_msg

def All_in_my_name(p, q):
    #开启三技能<俱以我之名>后，维娜立即在周围八格可部署地面召唤“黄金盟誓(Golden_Oath)”;对RSA造成真实伤害。
    Golden_Oath = (p-114)*(p-514)*(p+114)*(p+514)*(q-1919)*(q-810)*(q+1919)*(q+810)
    x = bytes_to_long(pad(gift, random.randint(bytes_to_long(gift).bit_length(), 512)))
    y = inverse(x, Golden_Oath)
    return y

flag = b'flag{?????}'
gift = b'?????'
assert gift[:3] == b'end'

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
c = pow(bytes_to_long(flag), e,n)

print(f'n = {n}')
print(f'c = {c}')
print(f'All_in_my_name = {All_in_my_name(p, q)}')

'''
n = 141425071303405369267688583480971314815032581405819618511016190023245950842423565456025578726768996255928405749476366742320062773129810617755239412667111588691998380868379955660483185372558973059599254495581547016729479937763213364591413126146102483671385285672028642742654014426993054793378204517214486744679
c = 104575090683421063990494118954150936075812576661759942057772865980855195301985579098801745928083817885393369435101522784385677092942324668770336932487623099755265641877712097977929937088259347596039326198580193524065645826424819334664869152049049342316256537440449958526473368110002271943046726966122355888321
All_in_my_name = 217574365691698773158073738993996550494156171844278669077189161825491226238745356969468902038533922854535578070710976002278064001201980326028443347187697136216041235312192490502479015081704814370278142850634739391445817028960623318683701439854891399013393469200033510113406165952272497324443526299141544564964545937461632903355647411273477731555390580525472533399606416576667193890128726061970653201509841276177937053500663438053151477018183074107182442711656306515049473061426018576304621373895497210927151796054531814746265988174146635716820986208719319296233956243559891444122410388128465897348458862921336261068868678669349968117097659195490792407141240846445006330031546721426459458395606505793093432806236790060342049066284307119546018491926250151057087562126580602631912562103705681810139118673506298916800665912859765635644796622382867334481599049728329203920912683317422430015635091565073203588723830512169316991557606976424732212785533550238950903858852917097354055547392337744369560947616517041907362337902584102983344969307971888314998036201926257375424706901999793914432814775462333942995267009264203787170147555384279151485485660683109778282239772043598128219664150933315760352868905799949049880756509591090387073778041
'''