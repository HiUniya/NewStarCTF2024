#求解离散对数问题

import math
def egcd(a,b):
    r0,r1,s0,s1=1,0,0,1
    n=b
    while(b):
        q,a,b=a//b,b,a%b
        r0,r1=r1,r0-q*r1
        s0,s1=s1,s0-q*s1
    return r0%n             #拓展欧几里得返回的三个值是，a是a和b的最大公因数，r0和s0分别是ax+by=c中的一组解x和y，【此时只是选择返回一个r0，因为得到的是ax+by=gcd(a,b)中的x即可，有的时候x或者y可能为负数，在求解正数的逆元的时候负数要对n再次求模运算
    
#求解离散对数就是，X=G^a mod P,其中给出X,G,P的值，要求解的是 a的值，此处采用的是Baby step giant step的方法

def bsgs(x,g,p):                  #求解x=g^a mod p中的a，其中g是生成元
    m=math.ceil(math.sqrt(p-1))   #m的值是 p-1开平方后向上取整
    bstep={pow(g,j,p):j for j in range(m)}              #每一次 j 的增加表示 “baby-step”，一次乘上g，字典S中存了所有的g^j(j<m)以及其对应的j
    gstep=egcd(pow(g,m),p)           #算出了gstep的值，也就是g^-m的值
    for i in range(m):
        if x in bstep:
            return i*m+bstep[x]
        x=x*gstep%p
        
print(bsgs(37,3,101))