import cv2
import numpy as np

img = cv2.imread("test.png")
ret,gray = cv2.threshold(img,127,256,cv2.THRESH_BINARY)

cv2.imshow("original image",img)
cv2.imshow("binary image",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
image_data=np.asarray(gray)
w=len(image_data)
h=len(image_data[0])
for i in range(w):
	for j in range(h):
		if((image_data[i,j,0]==0)and(image_data[i,j,1]==0)and (image_data[i,j,2]==0)):
			print 0,
		elif((image_data[i,j,0]==255)and(image_data[i,j,1]==255)and (image_data[i,j,2]==255)):
			print 1,

