from scipy.special import binom
from math import ceil
def probMujerGanarAntesDe(n):
    if(n<1000):
        pm=0
    else:
        pm=binom(n,1000)*(pow(0.5,n))
def probHombreGanarTurno(n,t):
    tg=ceil(1000/(2**(t-1)))
    print(tg)
h=11
m=1
p=0
n=1
print(probHombreGanarTurno(1,h))
