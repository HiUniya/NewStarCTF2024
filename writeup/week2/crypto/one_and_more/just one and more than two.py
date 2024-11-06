from Crypto.Util.number import *

flag = b'flag{?????}'
m1 = bytes_to_long(flag[:len(flag)//2])
m2 = bytes_to_long(flag[len(flag)//2:])
e = 65537
p, q, r= (getPrime(512) for _ in range(3))
N=p*q*r
c1 = pow(m1, e, p)
c2 = pow(m2, e, N)

print(f'p={p}\nq={q}\nr={r}\nc1={c1}\nc2={c2}')

'''
p=11867061353246233251584761575576071264056514705066766922825303434965272105673287382545586304271607224747442087588050625742380204503331976589883604074235133
q=11873178589368883675890917699819207736397010385081364225879431054112944129299850257938753554259645705535337054802699202512825107090843889676443867510412393
r=12897499208983423232868869100223973634537663127759671894357936868650239679942565058234189535395732577137079689110541612150759420022709417457551292448732371
c1=8705739659634329013157482960027934795454950884941966136315983526808527784650002967954059125075894300750418062742140200130188545338806355927273170470295451
c2=1004454248332792626131205259568148422136121342421144637194771487691844257449866491626726822289975189661332527496380578001514976911349965774838476334431923162269315555654716024616432373992288127966016197043606785386738961886826177232627159894038652924267065612922880048963182518107479487219900530746076603182269336917003411508524223257315597473638623530380492690984112891827897831400759409394315311767776323920195436460284244090970865474530727893555217020636612445
'''

