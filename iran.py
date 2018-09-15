from scipy import misc
from PIL import Image
import numpy as np


inp = misc.imread('test.png')
pokenumbers={}
resultado=""
resultador=""
print(len(inp))
for i in range(23):
    for j in range(24):
        if(inp[40*i:40*i+40,40*j:40*j+40].tostr() in pokenumbers):
            resultado+=str(pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tostr()])
            resultador+=str(pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tostr()])[::-1]
        else:
            img = Image.fromarray(inp[40*i:40*i+40,40*j:40*j+40], 'RGB')
            img.show()
            n=input()
            print(i*24+j,"/",23*24)
            pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tostr()]=n
print(resutado)
print()
print(resultador)
