##
# Bryce Jackson - 2022
#	
#	A software to detect color highlighting using python libraries cv2, pytesseract, and numpy
#	Input an image with highlighted text (red or green, for now) and it will label the text that is hihglighted. 
#
# Usage: In a unix terminal, enter the command 'python3 run.py'. Windows will open showing the original higlighted image, the color masked images, and the sharpened color masked images.
#
##

import csv
import cv2
import pytesseract
import numpy as np


# load an image file *note an enlarged font size leads to better text recognition
img = cv2.imread("text-hl.png")

# create lower and upper color limits

#red color
lower_val_red = (0, 0, 245)
upper_val_red = (200,200, 255)

#green color
lower_val_green = (0,245,0)
upper_val_green = (225,255,225)

#blue color
lower_val_blue = (225,0,0)
upper_val_blue = (255, 225, 225)


# Threshold the image to get only green colors
mask = cv2.inRange(img, lower_val_green, upper_val_green)

# Threshold the image to get only red colors
mask2= cv2.inRange(img, lower_val_red, upper_val_red)

# Threshold the image to get only red colors
mask3= cv2.inRange(img, lower_val_blue, upper_val_blue)


# apply mask to original image
res = cv2.bitwise_and(img,img, mask= mask)
res2 = cv2.bitwise_and(img,img, mask= mask2)
res3 = cv2.bitwise_and(img, img, mask = mask3) 

#sharpen to try to get better detection using a kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
                   
# the sharpened green image object
image_sharp = cv2.filter2D(src=res, ddepth=-1, kernel=kernel)

# the sharpened red image object
image_sharp1 = cv2.filter2D(src=res2, ddepth=-1, kernel=kernel)

# the sharpened blue image object
image_sharp2 = cv2.filter2D(src=res3, ddepth=-1, kernel=kernel)


#show images
#cv2.imshow("Original", img) #original
#cv2.imshow("Green Mask", res) #green
#cv2.imshow("Red mask", res2) #red
#cv2.imshow("Blue Mask", res3) #blue

#show sharpened images
#cv2.imshow("Sharpened Green", image_sharp) #sharp
#cv2.imshow("Sharpened Red", image_sharp1) #sharp
#cv2.imshow("Sharpened Blue", image_sharp2) #sharp

# see how well text recognition works with green image
data1 = pytesseract.image_to_string(res, lang='eng', config='--psm 6')
print("green masked: " + data1)

# see how well text recognition works with red image
data2 = pytesseract.image_to_string(res2, lang='eng', config='--psm 6')
print("red masked: " + data2)

# see how well text recognition works with red image
data3 = pytesseract.image_to_string(res3, lang='eng', config='--psm 6')
print("blue masked: " + data3)


# see how well text recognition works with sharp image
data3 = pytesseract.image_to_string(image_sharp, lang='eng', config='--psm 6')
print("green sharpened: " + data1)
csv1 = data3[:-1]

# see how well text recognition works with sharp image
data3 = pytesseract.image_to_string(image_sharp1, lang='eng', config='--psm 6')
print("red sharpened: " + data2)
csv2 = data3[:-1]

# see how well text recognition works with sharp image
data3 = pytesseract.image_to_string(image_sharp2, lang='eng', config='--psm 6')
print("blue sharpened: " + data3)
csv3 = data3[:-1]

cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/green1.png", res)
cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/red1.png", res2)
cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/blue1.png", res3)
cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/green_sharp1.png", image_sharp)
cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/red_sharp1.png", image_sharp1)
cv2.imwrite("/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/blue_sharp1.png", image_sharp2)



cv2.waitKey(0)
cv2.destroyAllWindows()

with open('/mnt/c/Users/bryce/Desktop/Documents/Highlight Recognition/out.csv','w') as f:
        writer = csv.writer(f, delimiter =' ',quotechar =' ',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(csv1)
        writer.writerow(csv2)
        writer.writerow(csv3)

