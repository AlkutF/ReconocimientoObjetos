import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

img = Image.open("./assets/Lápices_de_colores_01.jpg")
print('Image')
print(img)
img.show()

img = Image.open("./assets/Lápices_de_colores_01.jpg")
img_mat = np.array(img)
plt.imshow(img_mat)
plt.show()

'''img = cv2.imread("./assets/Lápices_de_colores_01.jpg")
img_mat = img.copy()
cv2.imshow("Image", img_mat)
cv2.waitKey(0)
cv2.destroyAllWindows()'''