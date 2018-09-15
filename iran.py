import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.png',0)
img2 = img.copy()
template = img[0:40,0:40]
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
'''
inp = misc.imread('test.jpg')
pokenumbers={}
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
'''
