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
        if(inp[40*i:40*i+40,40*j:40*j+40].tobytes() in pokenumbers):
            resultado+=str(pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tobytes()])
            resultador+=str(pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tobytes()])[::-1]
        else:
            img = Image.fromarray(inp[40*i:40*i+40,40*j:40*j+40], 'RGB')
            img.show()
            n=input()
            print()
            pokenumbers[inp[40*i:40*i+40,40*j:40*j+40].tobytes()]=n
print(resutado)
print()
print(resultador)
