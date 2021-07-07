import cv2
import numpy as np
import argparse

parser_dec = argparse.ArgumentParser()

parser_dec.add_argument('--encrypted', default='encrypted.bmp', type=str)
parser_dec.add_argument('--key', default='key_data.npy', type=str)
parser_dec.add_argument('--decrypted', default='recovered.jpg', type=str)

args = parser_dec.parse_args()

# ------Decoder---------------
img = cv2.imread(args.encrypted, cv2.IMREAD_GRAYSCALE)
key_loaded = np.load(args.key)

recovered = (np.bitwise_xor(img, key_loaded))
cv2.imwrite(args.decrypted, recovered)
