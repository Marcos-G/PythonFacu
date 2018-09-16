from scipy import misc
import numpy as np

inp = misc.imread('test.png')
pokenumbers={}
print((inp[40*2:40*2+40,40*7:40*7+40]-inp[0:40,0:40]).sum())
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
