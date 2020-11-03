import cv2 as cv


image = cv.imread("test-images/pumpkin.jpg")

# Invert the pixels
# for i in image:
#     for j in range(len(i)):
#         i[j] = ~i[j]

cv.imshow("Pumpkin", image)
cv.waitKey(0)
