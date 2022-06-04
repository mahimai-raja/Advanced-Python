import cv2

image = cv2.imread(' # Image path ')

gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray

blur = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blur

sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# Save the sketch image 
cv2.imwrite('Sketch_image.png', sketch)
cv2.imshow('Sketch Image', sketch)