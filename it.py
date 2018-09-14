gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
s=True
for i in range(10):
    c*=2
    if(s):
        c+=1
    else:
        c-=1
    s=not s
    print(c)
print(c)
"""110101010110000100001111011001001000001001101111
234612846789231
123 ¡No encontrado! 43.4 hello ¡No encontrado! Hello Universe! World! New ¡No encontrado! ¡No encontrado! 34 9.845 ¡No encontrado! ¡No encontrado! 4$ 6$ ¡No encontrado! ¡No encontrado! ¡No encontrado!
"""
