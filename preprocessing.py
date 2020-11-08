import os

from PIL import Image, ImageOps
from tqdm import tqdm

IMAGE_TRAIN_PATH = "/home/nqthuc/Documents/Zalo/TrafficDet/dataset/trafic_sign/train"
IMAGE_VAL_PATH = "/home/nqthuc/Documents/Zalo/TrafficDet/dataset/trafic_sign/val"

def padding_imgs(img_path):
    for fname in tqdm(os.listdir(img_path)):
        img = Image.open(img_path + "/" + fname).convert('RGB')
        width, _ = img.size
        padding_img = ImageOps.pad(img, (width, width), centering=(0, 0))
        padding_img.save(img_path + "/" + fname)

padding_imgs(IMAGE_TRAIN_PATH)
padding_imgs(IMAGE_VAL_PATH)
