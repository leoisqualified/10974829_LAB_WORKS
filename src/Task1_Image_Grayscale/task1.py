import cv2

# Load the original image
image = cv2.imread("photo.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show both images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Save grayscale image
cv2.imwrite("photo_gray.jpg", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
