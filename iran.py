from scipy import misc
import numpy as np

inp = misc.imread('test.jpg')
pokenumbers={}
print(inp[400*2:400*2+400,400*7:400*7+400]-inp[0:400,0:400])
resultado=""
resultador=""
print(len(inp))
for i in range(23):
    for j in range(24):
        if(str(inp[400*i:400*i+400,400*j:400*j+400]) in pokenumbers):
            resultado+=str(pokenumbers[str(inp[400*i:400*i+400,400*j:400*j+400])])
            resultador+=str(pokenumbers[str(inp[400*i:400*i+400,400*j:400*j+400])])[::-1]
        else:
            img = Image.fromarray(inp[400*i:400*i+400,400*j:400*j+400], 'RGB')
            img.show()
            n=input()
            print(i*24+j,"/",23*24)
            pokenumbers[str(inp[400*i:400*i+400,400*j:400*j+400])]=n
print(resutado)
print()
print(resultador)
