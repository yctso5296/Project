# -*- coding: utf-8 -*-

# clone repository of YOLOv5
git clone https://github.com/ultralytics/yolov5.git

# change to directory of yolov5
cd yolov5

# install the necessary libraries
pip install -r requirements.txt

# import python plot library and set plot window size
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = 21, 18

# retrieve original image from google drive (cloud) and save as "image1.jpg" in current directory
import requests
url = "https://drive.google.com/uc?id=1lvse1tfnih2rGflF-N2ZhVjegvaxLxC0&export=download"
r = requests.get(url)
with open('image1.jpg', 'wb') as f:
   f.write(r.content)

# read "image1.jpg" and plot
image1 = plt.imread('image1.jpg')
plt.subplot(121)
plt.imshow(image1)
plt.axis('off')
plt.title('Source Image')
plt.show()

# apply yolov5s model on "image1.jpg"
python detect.py --source image1.jpg --weights yolov5s.pt --project infer_yolov5s

# apply yolov5x model on "image1.jpg"
python detect.py --source image1.jpg --weights yolov5x.pt --project infer_yolov5x

# show object recognition results on "image1.jpg" for both yolov5s and yolov5x models
image1a = plt.imread('/content/yolov5/infer_yolov5s/exp/image1.jpg')
image1b = plt.imread('/content/yolov5/infer_yolov5x/exp/image1.jpg')

plt.subplot(121)
plt.imshow(image1a)
plt.axis('off')
plt.title('YOLOV5s predictions')

plt.subplot(122)
plt.imshow(image1b)
plt.axis('off')
plt.title('YOLOV5x predictions')

plt.show()

# encrypt image using XOR algorithm
# import numpy, cv2 and requests libraries
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import requests

# retrieve original image from Google Drive (cloud)
url = "https://drive.google.com/uc?id=1lvse1tfnih2rGflF-N2ZhVjegvaxLxC0&export=download"

# save retrieved image as "image1.jpg" in current directory
r = requests.get(url)
with open('image1.jpg', 'wb') as f:
   f.write(r.content)

# read shape of original image with cv2 library and generate encryption key
# source code credit to ProgrammerSought (2022)
img1 = cv2.imread("image1.jpg")
width, height, deep = img1.shape
imgKeyX = np.random.randint(0, 256, size=[width, height, deep], dtype=np.uint8)
cv2.imwrite("imgKeyX.jpg",imgKeyX)

# encrypt original image with key generated
imgEncryptX = cv2.bitwise_xor(img1, imgKeyX)
cv2.imwrite("imgEncryptX.jpg",imgEncryptX)

# save imgKeyX and imgEncryptX obtained to Google Drive (cloud) manually to get file id to facilitate remote file retrieval

# retrieve encryption key from Google Drive (cloud)
import requests
urlkey = "https://drive.google.com/uc?id=16G1JL5aTp_E4Q5cH6D7_7r_ALGPX-yRl&export=download"
rkey = requests.get(urlkey)

# save retrieved key as "imgKeyXOR.jpg" in current directory
with open('imgKeyXOR.jpg', 'wb') as fkey:
   fkey.write(rkey.content)

# retrieve encrypted image from Google Drive (cloud)
urlencrypt = "https://drive.google.com/uc?id=1swT0yRcOkvIC-7cBjBXjtJQqvPMvzAlW&export=download"
rencrypt = requests.get(urlencrypt)

# save retrieved encrypted image as "imgEncryptXOR.jpg" in current directory
with open('imgEncryptXOR.jpg', 'wb') as fencrypt:
   fencrypt.write(rencrypt.content)

# display retrieved encryption key and encrypted image 
imagekey = plt.imread('imgKeyXOR.jpg')
imageencrypt = plt.imread('imgEncryptXOR.jpg')

plt.subplot(121)
plt.imshow(imagekey)
plt.axis('off')
plt.title('Encryption Key')

plt.subplot(122)
plt.imshow(imageencrypt)
plt.axis('off')
plt.title('Encrypted Image')

plt.show()

# decrypt encrypted image
import cv2
from google.colab.patches import cv2_imshow
imagekey = cv2.imread('imgKeyXOR.jpg')
imageencrypt = cv2.imread('imgEncryptXOR.jpg')
imagedecrypt = cv2.bitwise_xor(imageencrypt, imagekey)
cv2_imshow(imagedecrypt)
cv2.imwrite("imgDecryptXOR.jpg",imagedecrypt)

# significant loss in resolution in decrypted image which are not suitable for performing object recognition.

# Encryption with DES
# source code credit to Chowdhury (2022)

# install pycrypto library
pip install pycrypto

# import the necessary libraries
from Crypto.Cipher import DES
from secrets import token_bytes
from PIL import Image
from google.colab.patches import cv2_imshow
import cv2

#Taken three key from token bytes
key1=token_bytes(16)
key2=token_bytes(16)
key3=token_bytes(16)

#Encryption function using triple key
def encrypt(image):
  cipher1=DES.new(key1[0:8],DES.MODE_CBC,key1[8:16])
  ciphertext1=cipher1.encrypt(image)
  cipher2=DES.new(key2[0:8],DES.MODE_CBC,key2[8:16])
  ciphertext2=cipher2.decrypt(ciphertext1)
  cipher3=DES.new(key3[0:8],DES.MODE_CBC,key3[8:16])
  ciphertext3=cipher3.encrypt(ciphertext2)
  return ciphertext3

# import numpy and cv2 libraries
import numpy as np
from google.colab.patches import cv2_imshow

# retrieve original image from Google Drive (cloud)
import requests
url = "https://drive.google.com/uc?id=1lvse1tfnih2rGflF-N2ZhVjegvaxLxC0&export=download"

# save retrieved image as "image1.jpg" in current directory
r = requests.get(url)
with open('image1.jpg', 'wb') as f:
   f.write(r.content)
  
# show retrieved image  
img1 = cv2.imread("image1.jpg")
cv2_imshow(img1)

# Main function for process the image and call the encryption function
with open("image1.jpg", 'rb') as imagefile:
  image=imagefile.read()
while len(image)%8!=0:
  image+=b" "
ciphertext=encrypt(image)

#save encrypted image to file "imgEncryptDES.enc"
with open('imgEncryptDES.enc', 'wb') as f:
    f.write(ciphertext)

# save "imgEncryptDES.enc" obtained to Google Drive (cloud) manually to get file id to facilitate remote file retrieval

# Decryption function
# Encryption and Descryption key is same
def decrypt(ciphertext):
  cipher1=DES.new(key3[0:8],DES.MODE_CBC,key3[8:16])
  plaintext1=cipher1.decrypt(ciphertext)
  cipher2=DES.new(key2[0:8],DES.MODE_CBC,key2[8:16])
  plaintext2=cipher2.encrypt(plaintext1)
  cipher3=DES.new(key1[0:8],DES.MODE_CBC,key1[8:16])
  plaintext3=cipher3.decrypt(plaintext2)
  return plaintext3

# retrieve encrypted image from Google Drive (cloud)
import requests
url = "https://drive.google.com/uc?id=1sITeSWgKSAeiRTIEJeM10iHZLC4Jm1dR&export=download"
r = requests.get(url)

# save retrieved encrypted image to "ciphertext"
with open('ciphertext', 'wb') as f:
   f.write(r.content)

# call the decryption function to decrypt encrypted image
plaintext=decrypt(ciphertext)

# save decrypted image to "imgDecryptDES.jpg"
with open("imgDecryptDES.jpg", 'wb') as f:
	f.write(plaintext)

# show the decrypted image
imgDecryptDES = cv2.imread("imgDecryptDES.jpg")
cv2_imshow(imgDecryptDES)

# the decrypted image is the same as the original image

# apply yolov5s model on "image1.jpg"
python detect.py --source "imgDecryptDES.jpg" --weights yolov5s.pt --project infer_yolov5s

# apply yolov5x model on "image1.jpg"
python detect.py --source "imgDecryptDES.jpg" --weights yolov5x.pt --project infer_yolov5x

# show object recognition results on "image1.jpg" for both yolov5s and yolov5x models
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = 21, 18
imgdec1a = plt.imread('/content/yolov5/infer_yolov5s/exp2/imgDecryptDES.jpg')
imgdec1b = plt.imread('/content/yolov5/infer_yolov5x/exp2/imgDecryptDES.jpg')

plt.subplot(121)
plt.imshow(imgdec1a)
plt.axis('off')
plt.title('YOLOV5s predictions')

plt.subplot(122)
plt.imshow(imgdec1b)
plt.axis('off')
plt.title('YOLOV5x predictions')

plt.show()