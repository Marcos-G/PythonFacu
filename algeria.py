from scipy.special import binom,comb
from math import ceil
from decimal import *
import sys
def probMujerGanarEnOAntesDe(n):
    if(n<1000):
        pm=0
    else:
        pm=Decimal(comb(n,1000,exact=True))*(Decimal(0.5)**n)
    return pm
def probHombreGanarTurno(n,t):
    tg=ceil(1000/(2**(t-1)))
    ph=comb(n-1,tg-1,exact=True)*((Decimal(0.5)**t)**tg)*(1-Decimal(0.5)**t)**(n-tg)
    return ph
h=11
m=1
p=0
for n in range(1,200000):
    p+=(Decimal(0.5)**11)*((1-Decimal(0.5)**11)**(n-1))*(1-(comb(n,1000,exact=True)*(Decimal(0.5)**n)))
    print(p)
