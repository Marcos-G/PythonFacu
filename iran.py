'''from scipy import misc
import numpy as np
from PIL import Image


inp = misc.imread('test.png')
pokenumbers={}
calculado=[]
resultador=""
print(len(inp))
res=[['' for i in range(24)] for j in range(24)]
for i in range(23):
    for j in range(24):
        if( (i,j) not in calculado):
            img = Image.fromarray(inp[40*i:40*i+40,40*j:40*j+40], 'RGB')
            img.show()
            n=input()
            res[i][j]=n
            calculado.append((i,j))
            for a in range(23):
                for b in range(24):
                    if( (a,b) not in calculado and (inp[40*a:40*a+40,40*b:40*b+40]-inp[40*i:40*i+40,40*j:40*j+40]).sum()<=3000):
                        res[a][b]=n
                        calculado.append((a,b))
            print(str(res))'''
array=[['092', '095', '082', '085', '082', '095', '026', '017', '028', '016', '027', '022', '017', '024', '069', '095', '010', '011', '025', '082', '071', '095', '082', '085'], ['082', '117', '117', '022', '025', '095', '032', '032', '017', '030', '018', '026', '032', '032', '095', '066', '066', '095', '093', '032', '032', '018', '030', '022'], ['017', '032', '032', '093', '069', '117', '118', '092', '095', '060', '016', '018', '015', '010', '011', '022', '017', '024', '095', '016', '010', '013', '095', '018'], ['030', '024', '022', '028', '095', '017', '010', '018', '029', '026', '013', '081', '081', '081', '117', '118', '092', '095', '054', '095', '008', '016', '017', '027'], ['026', '013', '095', '008', '023', '006', '095', '022', '011', '095', '022', '012', '095', '011', '030', '020', '022', '017', '024', '095', '012', '016', '095', '019'], ['016', '017', '024', '094', '117', '117', '118', '018', '030', '007', '032', '019', '022', '018', '022', '011', '095', '066', '095', '078', '007', '076', '075', '074'], ['073', '072', '071', '070', '071', '072', '073', '074', '075', '076', '007', '079', '117', '117', '118', '092', '095', '013', '030', '017', '024', '026', '095', '022'], ['012', '095', '024', '022', '009', '022', '017', '024', '095', '018', '026', '095', '018', '026', '018', '016', '013', '006', '095', '026', '013', '013', '016', '013'], ['095', '022', '017', '095', '015', '006', '011', '023', '016', '017', '007', '083', '095', '008', '026', '088', '027', '095', '029', '026', '011', '011', '026', '013'], ['095', '010', '012', '026', '095', '030', '095', '024', '026', '017', '026', '013', '030', '011', '016', '013', '117', '118', '028', '016', '010', '017', '011', '095'], ['066', '095', '079', '117', '118', '025', '016', '013', '095', '022', '095', '022', '017', '095', '007', '013', '030', '017', '024', '026', '087', '018', '030', '007'], ['032', '019', '022', '018', '022', '011', '086', '069', '117', '118', '118', '028', '016', '010', '017', '011', '095', '84', '066', '095', '078', '117', '117', '118'], ['019', '022', '017', '026', '030', '013', '032', '012', '010', '018', '095', '066', '095', '079', '117', '118', '025', '016', '013', '095', '021', '095', '022', '017'], ['095', '007', '013', '030', '017', '024', '026', '087', '018', '030', '007', '032', '019', '022', '018', '022', '011', '086', '069', '117', '118', '118', '019', '022'], ['017', '026', '030', '013', '032', '012', '010', '018', '095', '84', '066', '095', '021', '117', '117', '118', '012', '014', '010', '030', '013', '026', '027', '032'], ['012', '010', '018', '095', '066', '095', '079', '117', '118', '025', '016', '013', '095', '020', '095', '022', '017', '095', '007', '013', '030', '017', '024', '026'], ['087', '018', '030', '007', '032', '019', '022', '018', '022', '011', '095', '080', '095', '074', '086', '069', '117', '118', '118', '012', '014', '010', '030', '013'], ['026', '027', '032', '012', '010', '018', '095', '84', '066', '095', '020', '095', '085', '095', '020', '117', '117', '118', '028', '010', '029', '022', '028', '032'], ['012', '010', '018', '095', '066', '095', '079', '117', '118', '025', '016', '013', '095', '019', '095', '022', '017', '095', '007', '013', '030', '017', '024', '026'], ['087', '018', '030', '007', '032', '019', '022', '018', '022', '011', '095', '080', '095', '007', '079', '086', '069', '117', '118', '118', '028', '010', '029', '022'], ['028', '032', '012', '010', '018', '095', '84', '066', '095', '019', '095', '085', '095', '019', '095', '085', '095', '019', '117', '117', '118', '015', '013', '022'], ['017', '011', '087', '019', '022', '017', '026', '030', '013', '032', '012', '010', '018', '095', '84', '095', '012', '014', '010', '030', '013', '026', '027', '032'], ['012', '010', '018', '095', '84', '095', '028', '010', '029', '022', '028', '032', '012', '010', '018', '086', '117']]
res=""
resi=""
for i in range(len(res)):
    for j in range(len(res[i])):
        res+=chr(int(array[i][j]))
        resi+=chr(int(array[i][j][::-1]))
print(res)
print(resi)
