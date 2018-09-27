from scipy.special import binom,comb
from math import ceil
from decimal import *
import sys
def probMujerNOGanarEnOAntesDe(n):
    if(n<1000):
        pm=1
    else:
        pm=comb(n,n-1000,exact=True)*(Decimal(0.5)**n)
    return pm
def probHombreGanarTurno(n,t):
    tg=ceil(1000/(2**(t-1)))
    ph=comb(n-1,tg-1,exact=True)*((Decimal(0.5)**t)**tg)*(1-Decimal(0.5)**t)**(n-tg)
    return ph
h=11
m=1
p=0
setcontext(Context(prec=60, rounding=ROUND_HALF_DOWN))
for n in range(1,3000):
    p+=(Decimal(0.5)**11)*((1-Decimal(0.5)**11)**(n-1))*probMujerNOGanarEnOAntesDe(n)
    a=Decimal(comb(n,1000,exact=True)*(Decimal(0.5)**n))
    b=Decimal(Decimal(1.0)-Decimal(a))
    c=Decimal(Decimal(1.0)-Decimal(b))
    print(n,p)
