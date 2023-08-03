import cv2
import sys
import re
from pyzbar.pyzbar import decode

image = cv2.imread("img2.png")


detectedBarcodes = decode(image)
#print(detectedBarcodes)
#print(type(detectedBarcodes))
#print(len(detectedBarcodes))


for barcode in detectedBarcodes:
   
    bar = str(barcode.data)

    bar = bar.replace('b','')
    bar = bar.replace("'",'')
    
    bar = int(bar)
    print(type(bar))


    
""" 



if image is None:
    print("Image not found")
else:
    print("Image found")


h,w = image.shape[:2]
print(h,w)


#Resizing Image
image = cv2.resize(image,(800,800))

h,w = image.shape[:2]
print(h,w)

cv2.imshow("Resized Image",image)
cv2.waitKey(1)

"""
