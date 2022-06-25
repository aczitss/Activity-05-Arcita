import cv2 as cv
import numpy as py

#image loading..
img = cv.inread("john.jpg")

#check image rgb or grayscale image
if(len(img.shape)<2):
    print("\nImage Type: Grayscale Image")
    exit()
elif len(img.shape)==3:
    print("\nImage Type: Colored Image")

#dimension and size image
maxheight =  1920
maxwidth = 1080
minheight = 480
minwidth = 360
size = 1500000

#SET IMAGE DIMENSION
print("\nImage Dimension limit : max = 1920 x 1080 and min = 480 x 360")
imgheight = img.shape[0]
imgwidth = img.shapre[1]
print("Current loaded image dimension:", imgheight, "x",imgwidth)
if((imgheight < maxheight and imgheight > minheight) and (imgwidth < maxwidth and imgwidth > minwidth)):
    print("Current loaded image is within the boundaries!")
else:
    print("Current loaded image is not in the boundaries!")

#SET IMAGE TOTAL PIXEL COUNT
print("\nSet size:", size)
imgsize = img.size
print("Current loaded image size:",imgsize)
if(imgsize < size):
    print("Current loaded image has lower pixel count than the set image size!")
else:
    print("\nCurrent loaded image has higher pixel count than the set image size!")

#SHOW THE IMAGE DATA TYPE
print("\nCurrent loaded image datatype:", img.dtype)

#PIXEL VALUE
print("\nAccess a pixel value using item method")
a,b,c = input("Enter row, column and channel: ").split() 
row1,col1,chan1 = [int(a), int(b), int (c)]
res = img.item(row1,col1,chan1)
print("Result: ".res)

print("\n Modify a pixel value using Itemset method")
q,w = input("Enter column and row: ").split()
blue = int(input("Enter changes in blue channel: "))
green = int(input("Enter changes in green channel: "))
red = int(input("Enter changes in red channel: "))
print("Result: ")
row2, col2 = [int(q), int(w)]
img.item(row2,col2,0)
img.item(row2,col2,1)
img.item(row2,col2,2)
res1 = img[row2,col2]
print("Before:", res1)
img.itemset((row2,col2,0), blue)
img.itemset((row2,col2,0), green)
img.itemset((row2,col2,0), red)
res2 = img[row2,col2]
print("After: ", res2,"\n")

