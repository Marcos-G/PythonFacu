gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
inp="a"
for i in range(234612846789231):
  arr=list(inp)
  outp=""
  for a in range(len(arr)):
    outp+=gram[arr[a]]
  inp=outp
  print(i/234612846789231.0)
print(outp.count('alpaca'))
