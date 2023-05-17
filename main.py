#Developed by Kirollos Gerges
#Q2
#python program to read an image and find the corners using Harris corner detection.
import cv2
import numpy as np

# read input image
input = cv2.imread('lamborgini.jpg')

# convert the input image into grayscale colored space
Image_processing = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

# modify the data type setting to 32-bit floating point
Image_processing = np.float32(Image_processing)

# apply the cv2.cornerHarris method to detect the corners with adjusting input parameters
destination = cv2.cornerHarris(Image_processing, 2, 5, 0.07)

# Results are marked through the dilated corners
destination = cv2.dilate(destination, None)

# Reverting back to the original image, with optimal threshold value 50
input[destination > 0.01 * destination.max()] = [0, 128, 255]

# The output image with corners detection
cv2.imshow('lamborgini Image with corners using Harris corner detection', input)

# De_allocate memory,reset it
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()