import cv2
import numpy as np
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--img', default='Mona_Lisa.jpg', type=str)
my_parser.add_argument('--out', default='encrypted.bmp', type=str)
my_parser.add_argument('--key_name', default='key_data', type=str)
args = my_parser.parse_args()


image = cv2.imread(args.img, cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape

# ------Encoder---------------
array_image = np.asarray(image)

key = np.random.randint(256, size=(rows, cols))
output = (np.bitwise_xor(image, key))

cv2.imwrite(args.out, output)
np.save(args.key_name, key)


