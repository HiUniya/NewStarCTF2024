# -*- coding:utf-8 -*-

n = 141425071303405369267688583480971314815032581405819618511016190023245950842423565456025578726768996255928405749476366742320062773129810617755239412667111588691998380868379955660483185372558973059599254495581547016729479937763213364591413126146102483671385285672028642742654014426993054793378204517214486744679

z = 400042032831098007958224589201074030167511216235146696966889080122265111949126155016295896501799032251334875101500882585261911204171467951139573150807043239564581043145433814155757093989016940205116328236031283789686099217459678429270939065783626769903068201144816933538226628329294355184200590029028565011348654002192085571172863125467318356642528249715812871925525776008917314884490518613080652875623759460663908309369135829140204137773254011408135516737187092812588388209697036416805176286184831779945910125467423823737934475944632379524991238593952097013985394648562259886597816452815669024660257170465154297959999722533255899489096196292778430386116108069053440749172609798098777046509743030019115282253351905670418760503352277616008654327326851761671410084489662135479597061419403235762755010286075975241013273964842915146756571330207605591193457296347769260777032489271278979332616929093357929916558230665466587125254822846466292980360420737307459205352964255972268278992730637939153686420457279334894980200862788513296786385507282999530973028293157179873999483225505784146175328159014143540959190522315340971608002638786511995717564457749873410017343184395040614025573440462522210939180555090227730875845671821586191943346000

a1 = 1919*1919*810*810
a2 = -(1919*1919+810*810)*n-(114*114+514*514)*1919*1919*810*810
a3 = n*n+(114*114+514*514)*(1919*1919+810*810)*n+114*114*514*514*1919*1919*810*810-z
a4 = -(114*114+514*514)*n*n-114*114*514*514*(1919*1919+810*810)*n
a5 = 114*114*514*514*n*n



coefficients = [a1, a2, a3, a4, a5]  # 例如 x^4 - 2x^2 + 1 = 0

import math
import cmath
import numpy as np
 
 
def cal_quartic_ik(args_list):
    a, b, c, d, e = args_list
 
    D = 3*pow(b,2) - 8*a*c
    E = -pow(b, 3) + 4*a*b*c - 8*pow(a, 2)*d
    F = 3*pow(b, 4) + 16*pow(a, 2)*pow(c, 2) - 16*a*pow(b, 2)*c + 16*pow(a, 2)*b*d - 64*pow(a, 3)*e
 
    A = D**2 - 3*F
    B = D*F - 9*pow(E, 2)
    C = F**2 - 3*D*pow(E, 2)
 
    delta = B**2 - 4*A*C  # 总判别式
 
    if (D == 0) & (E == 0) & (F == 0):
        """ 四重实根"""
        x = -b/(4*a)
        return 1, [x]
    if (A == 0) & (B == 0) & (C == 0) & (D*E*F != 0):
        """ 两个实根，其中一个三重实根"""
        x1 = (-b*D + 9*E)/(4*a*D)
        x234 = (-b * D - 3 * E) / (4 * a * D)
        return 2, [x1, x234]
    if (E == 0) & (F == 0) & (D != 0):
        """ 一对二重根"""
        if D>0:  # 根为实数
            x13 = (-b + math.sqrt(D))/(4*a)
            x24 = (-b - math.sqrt(D)) / (4 * a)
            return 2, [x13, x24]
 
        if D<0:  # 根为虚数
            # x13 = (-b + cmath.sqrt(D))/(4*a)
            # x24 = (-b - cmath.sqrt(D)) / (4 * a)
            return 0, 0
    if (A*B*C != 0) & (delta == 0):
        """ 一对二重实根 """
        x3 = (-b - np.sign(A*B*E)*math.sqrt( D - B/A))/(4*a)
        x4 = (-b - np.sign(A*B*E)*math.sqrt( D - B/A))/(4*a)
        if A*B>0 :  # 其余两根为不等实根
            x1 = (-b + np.sign(A*B*E)*math.sqrt( D - B/A) + math.sqrt( 2*B/A) )/(4*a)
            x2 = (-b + np.sign(A * B * E) * math.sqrt(D - B / A) - math.sqrt(2 * B / A)) / (4 * a)
            return 4, [x1, x2, x3, x4]
        if A*B < 0:  # 其余两根为共轭虚根
            # x1 = (-b + np.sign(A * B * E) * math.sqrt(D - B / A) + cmath.sqrt(2 * B / A)) / (4 * a)
            # x2 = (-b + np.sign(A * B * E) * math.sqrt(D - B / A) - cmath.sqrt(2 * B / A)) / (4 * a)
            return 2,  [x3, x4]
    if delta > 0:
        """" 两个不等实根和一对共轭虚根"""
        z1 = A*D + 3*(( -B + math.sqrt(delta))/2.0)
        z2 = A * D + 3 * ((-B - math.sqrt(delta)) / 2.0)
 
        # print """ z1 =  """, z1
        # print """ z2 =  """, z2
        # print """ abs(z1) =  """, abs(z1)
        # print """ abs(z2) =  """, abs(z2)
 
        z = D**2 - D*(np.sign(z1)*pow(abs(z1), 1.0/3.0) + np.sign(z2)*pow(abs(z2), 1.0/3.0)) + \
            (np.sign(z1)*pow(abs(z1), 1.0/3.0) + np.sign(z2)*pow(abs(z2), 1.0/3.0))**2 - 3*A
 
        x1 = (-b + np.sign(E)*math.sqrt((D + np.sign(z1)*pow(abs(z1), 1.0/3.0) + np.sign(z2)*pow(abs(z2), 1.0/3.0))/3.0)
              + math.sqrt((2*D - np.sign(z1)*pow(abs(z1), 1.0/3.0) - np.sign(z2)*pow(abs(z2), 1.0/3.0)
                 + 2*math.sqrt(z))/3.0))/(4*a)
        x2 = (-b + np.sign(E)*math.sqrt((D + np.sign(z1)*pow(abs(z1), 1.0/3.0) + np.sign(z2)*pow(abs(z2), 1.0/3.0))/3.0)
              - math.sqrt((2*D - np.sign(z1)*pow(abs(z1), 1.0/3.0) - np.sign(z2)*pow(abs(z2), 1.0/3.0)
                 + 2*math.sqrt(z))/3.0))/(4*a)
 
        # 虚根忽略
        return 2, [x1, x2]
    if delta < 0:
        if E == 0:
            if (D>0) & (F>0) :
                """ 四个不等实根 """
                x1 = (-b + math.sqrt(D + 2*math.sqrt(F))) / (4 * a)
                x2 = (-b - math.sqrt(D + 2 * math.sqrt(F))) / (4 * a)
                x3 = (-b + math.sqrt(D - 2 * math.sqrt(F))) / (4 * a)
                x4 = (-b - math.sqrt(D - 2 * math.sqrt(F))) / (4 * a)
                return 4, [x1, x2, x3, x4]
            else:
                """ 两对不等共轭虚根 """
                # 虚根忽略
                print " 两对不等共轭虚根 "
                return 0, 0
        else:
            if (D > 0) & (F > 0):
                """ 四个不等实根 """
                theta = math.acos((3*B-2*A*D)/(2*A*math.sqrt(A)))
                y1 = (D - 2*math.sqrt(A)*math.cos(theta/3.0))/3.0
                y2 = (D + math.sqrt(A)*(math.cos(theta/3.0) + math.sqrt(3)*math.sin(theta/3.0)))/3.0
                y3 = (D + math.sqrt(A) * (math.cos(theta / 3.0) - math.sqrt(3) * math.sin(theta / 3.0))) / 3.0
 
                x1 = (-b + np.sign(E) * math.sqrt(y1) + ( math.sqrt(y2) + math.sqrt(y3)))/(4*a)
                x2 = (-b + np.sign(E) * math.sqrt(y1) - (math.sqrt(y2) + math.sqrt(y3))) / (4 * a)
                x3 = (-b - np.sign(E) * math.sqrt(y1) + (math.sqrt(y2) - math.sqrt(y3))) / (4 * a)
                x4 = (-b - np.sign(E) * math.sqrt(y1) - (math.sqrt(y2) - math.sqrt(y3))) / (4 * a)
 
                return 4, [x1, x2, x3, x4]
            else:
                """ 两对不等共轭虚根 """
                # 虚根忽略
                print " 两对不等共轭虚根 "
                return 0, 0

cal_quartic_ik(coefficients)