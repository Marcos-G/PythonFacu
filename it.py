gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=1
for i in range(234612846789231):
  arr=list(inp)
  outp=""
  once=True
  for a in range(len(arr)):
    outp+=gram[arr[a]]
    if(once and outp==inp):
        outp=""
        once=False
  inp=outp
  c+=outp.count('alpaca')
  print(i/234612846789231.0)
  print(c)
print(c)
"""110101010110000100001111011001001000001001101111
234612846789231
123 ¡No encontrado! 43.4 hello ¡No encontrado! Hello Universe! World! New ¡No encontrado! ¡No encontrado! 34 9.845 ¡No encontrado! ¡No encontrado! 4$ 6$ ¡No encontrado! ¡No encontrado! ¡No encontrado!
"""
