import os
import json
from shutil import copyfile
from tqdm import tqdm

ANNOTATION_PATH = "/home/nqthuc/Documents/Zalo/TrafficDet/annotations"
IMAGE_PATH = "/home/nqthuc/Documents/Zalo/TrafficDet/za_traffic_2020/traffic_train/images"
DATA_PATH = "./dataset/trafic_sign"
TRAIN_SET_NAME = "train"
VAL_SET_NAME = "val"

DEST_ANNOTATION_PATH = os.path.join(DATA_PATH, "annotations")
if (not os.path.exists(DEST_ANNOTATION_PATH)):
        os.makedirs(DEST_ANNOTATION_PATH)

for fname in os.listdir(ANNOTATION_PATH):
    isTrain = (fname.find("train") != -1)
    if (isTrain):
        DEST_IMAGE_PATH = os.path.join(DATA_PATH, TRAIN_SET_NAME)
        copyfile(os.path.join(ANNOTATION_PATH, fname), os.path.join(DEST_ANNOTATION_PATH, "instances_" + TRAIN_SET_NAME + ".json"))
    else:
        DEST_IMAGE_PATH = os.path.join(DATA_PATH, VAL_SET_NAME)
        copyfile(os.path.join(ANNOTATION_PATH, fname), os.path.join(DEST_ANNOTATION_PATH, "instances_" + VAL_SET_NAME + ".json"))
    if (not os.path.exists(DEST_IMAGE_PATH)):
        os.makedirs(DEST_IMAGE_PATH)
    with open(os.path.join(ANNOTATION_PATH, fname)) as json_file:
        images = json.load(json_file)['images']
        for img_info in tqdm(images):
            img_src_path = os.path.join(IMAGE_PATH, str(img_info['file_name']))
            img_dest_path = os.path.join(DEST_IMAGE_PATH, str(img_info['file_name']))
            copyfile(img_src_path, img_dest_path)




