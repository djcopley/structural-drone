import cv2 as cv


# Read in the image
img = cv.imread("test-images/pumpkin.jpg")

# Draw red rectangle
cv.rectangle(img, (160, 60), (800, 700), (0, 255, 0), 3)

cv.imshow("Pumpkin", img)
cv.waitKey(0)
cv.destroyAllWindows()
