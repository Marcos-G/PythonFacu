from scipy import misc
import numpy as np

inp = misc.imread('test.png')
pokenumbers={}
calculado=[]
resultador=""
print(len(inp))
res=[['' for i in range(24)] for j in range(24)]
for i in range(23):
    for j in range(24):
        if( (i,j) not in calculados):
            img = Image.fromarray(inp[40*i:40*i+40,40*j:40*j+40], 'RGB')
            img.show()
            n=input()
            res[i][j]=n
            calculados.append((i,j))
            for a in range(23):
                for b in range(24):
                    if( (a,b) not in calculados and (inp[40*a:40*a+40,40*b:40*b+40]-inp[40*i:40*i+40,40*j:40*j+40]).sum()<=3000):
                        res[i][j]=n
                        calculados.append((i,j))
            print(str(sol))
