import cv2

# Load the image
img = cv2.imread('assets/background.png')

# Print the original dimensions of the image
print("Original Dimensions : ", img.shape)

# Resize the image
resized_img = cv2.resize(img, (1000,800))
cv2.imwrite('assets/background_updated.png', resized_img)

# Print the new dimensions of the image
print("Resized Dimensions : ", resized_img.shape)

# Display the original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
