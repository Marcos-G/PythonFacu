from scipy.special import binom,comb
from math import ceil
from decimal import *
import sys
setcontext(Context(prec=200, rounding=ROUND_HALF_DOWN))
def probMujerNOGanarEnOAntesDe(n):
    if(n<1000):
        return Decimal(1)
    pm=Decimal(0)
    for g in range(999):
        pm+=comb(n,g,exact=True)*(Decimal(0.5)**n)
    return pm
def probMujerGanarEnOAntesDe(n):
    if(n<1000):
        pm=1
    else:
        pm=comb(n,1000,exact=True)*(Decimal(0.5)**n)
    return pm
def probHombreGanarTurno(n,t):
    tg=ceil(1000/(2**(t-1)))
    ph=comb(n-1,tg-1,exact=True)*((Decimal(0.5)**t)**tg)*(1-Decimal(0.5)**t)**(n-tg)
    return ph
h=11
m=1
p=0
for n in range(1,3000):
    p+=probMujerNOGanarEnOAntesDe(n)*probHombreGanarTurno(n,h)
    print(n,p)
//11 0.62284446409585702730212154240537669444306908241802142203139433171908425610434484099912314526851746147572123049944448854360118216033593990870246568813807433020496054111696809687750267481957470444876691
