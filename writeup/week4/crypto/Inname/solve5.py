from Crypto.Util.number import *
from gmpy2 import *
import random
p = 11256874906034337229658272553494271626180719204801621165552253304119314454014247481847595578004383239651599038196432752043642616511808644606155091511313329
q = 12563439896413287507369191021540890661182794010085857062984791988214078294298809633469029528754549607502031091193150571585844351836163514784874848514208151

N = p*q

e = 65537

c = 104575090683421063990494118954150936075812576661759942057772865980855195301985579098801745928083817885393369435101522784385677092942324668770336932487623099755265641877712097977929937088259347596039326198580193524065645826424819334664869152049049342316256537440449958526473368110002271943046726966122355888321


fi = (p-1)*(q-1)

d = inverse(e,fi)

m = pow(c,d,N)

print(long_to_bytes(m))