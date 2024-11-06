import gmpy2
beta=0.37
delta=0.01
n=round((1-2*beta-2*delta)/((1-beta)^2-2*delta-beta),6)
e= 3668637434348843171145584606519031375027610199908169273169275927238735031431533260375377791001464799116453803408104076615710166171199990283470548282669948353598733020244755959461974603778630346457439345913209321194112256348302765254052193562603687450740346132207444615610078198488883539133291840346099727880587092122957231085658576850601488737629051252914095889313671875244094452330062619943781809984690384476868543570724769198985172300665613239047649089399919032152539462701309393130614829962670866062380816370571057536421400102100259975636785825540933280194583888638501981649650640939392658268133881679239293596283
N= 9748523098652101859947730585916490335896800943242955095820326993765071194474558998322598145898741779502734772138283011560029368500998354183150180904846368209977332058847768859238711047784703104535311583123388923571789764758869419482184613566672922481672444028753365755071127320541645016370072493604532087980626825687519083734367691341907014061379844209864141989961751681235215504772582878202048494707090104738899927036896915997556102574747166491969027546256022019959716418675672979328622656831990050058120299353807110233202113906317969377201045402271911946244076903611612303290556012512559696538977841061277173754331
c= 5374936627659221745209010619827617207565185520404653329184605916859755641352457088986635357806048863755173540232471505333583684733535121482637476692432365062808450583470788320547816186936317927449796090525477205337038591439577855884910604383190932340306435201976465543731935147881754136301375206828970248293731391543905441514528959500307972606931927112031018356411970001312995489429650903529877904694901310020882390008248466887950986326522740278880600110217817950511478637493101027659292006016454642135508207492151610829525082829566392116546434101694921106423469015683277992978077101831969525458693031031468092418427
n=int(n+1)
#print(n)
m=int(n*(1-beta))
X=int(pow(N,delta))
Y=int(pow(N,delta+beta))
Z.<x,y>=ZZ[]
L=Matrix(ZZ,n,n)
f=e*x-y
for i in range(n):
    g=list(N^max(0,m-i)*x^(n-1-i)*f^i)
    for j in range(len(g)):
        L[i,j]=g[j][0]*X^(n-1-j)*Y^j
L=L.LLL()[0]
coeff=[]
for i in range(n):
    coeff.append((L[i]//(X^(n-1-i)*Y^i),'x'+'**'+str(n-1-i)+'*y'+'**'+str(i)))
s=''
for i in range(len(coeff)):
    s+=str(coeff[i][0])+'*'+coeff[i][1]+'+'
f=eval(s[:-1])
factored_f = f.factor()
first_polynomial = factored_f[0][0]
first_coefficient = first_polynomial.coefficients()[0]
k = first_coefficient + 1
dp = first_polynomial.coefficients()[1]
p=(e*dp-1)//k+1
q=N//p
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,N)
print(bytes.fromhex(hex(m)[2:]))