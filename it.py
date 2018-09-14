gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
for i in range(5):
  arr=list(inp)
  outp=""
  for a in range(len(arr)):
    outp+=gram[arr[a]]
  inp=outp
  print(outp)
  print(outp.count('alpaca'))
print(outp.count('alpaca'))
"""110101010110000100001111011001001000001001101111
234612846789231
123 ¡No encontrado! 43.4 hello ¡No encontrado! Hello Universe! World! New ¡No encontrado! ¡No encontrado! 34 9.845 ¡No encontrado! ¡No encontrado! 4$ 6$ ¡No encontrado! ¡No encontrado! ¡No encontrado!
"""
