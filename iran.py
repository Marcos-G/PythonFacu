from scipy import misc
from PIL import Image
import numpy as np


inp = misc.imread('test.jpg')
pokenumbers={}
resultado=""
resultador=""
print(len(inp))
for i in range(23):
    for j in range(24):
        if(str(inp[40*i:40*i+40,40*j:40*j+40]) in pokenumbers):
            resultado+=str(pokenumbers[str(inp[40*i:40*i+40,40*j:40*j+40])])
            resultador+=str(pokenumbers[str(inp[40*i:40*i+40,40*j:40*j+40])])[::-1]
        else:
            img = Image.fromarray(inp[40*i:40*i+40,40*j:40*j+40], 'RGB')
            img.show()
            n=input()
            print(i*24+j,"/",23*24)
            pokenumbers[str(inp[40*i:40*i+40,40*j:40*j+40])]=n
print(resutado)
print()
print(resultador)
