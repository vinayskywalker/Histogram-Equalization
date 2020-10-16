import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL
import cv2


img=cv2.imread("data/img5.jpg",0)
img_1=Image.open("data/img5.jpg")
# print(img.shape)






def freq(img):
    mp=[0]*256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            mp[int(img[i][j])]=mp[int(img[i][j])]+1
    return mp




def cdf(pdf):
    cdf=[0]*256
    sum=0
    for i in range(len(cdf)):
        sum=sum+pdf[i]
        cdf[i]=round(sum*255)
    
    return cdf



def pdf(hist):
    pb=[0]*256
    for i in range(len(pb)):
        pb[i]=hist[i]/(img.shape[0]*img.shape[1])
    
    return pb


def create_img(cdf):
    nw_img=np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            nw_img[i][j]=int(cdf[img[i][j]])
    
    return nw_img



frequency=freq(img)
pdf=pdf(frequency)
cdf=cdf(pdf)

# plt.bar(range(256),frequency)
# plt.savefig("old_freq.png")
# plt.bar(range(256),cdf)
# plt.show()

nw_img=create_img(cdf)
nw_freq=freq(nw_img)

nw_img=Image.fromarray(np.uint8(nw_img),'L')
nw_img.show(title="New Image")
img_1.show(title="Old image")


plt.bar(range(256),nw_freq)
plt.savefig("new_freq.png")






