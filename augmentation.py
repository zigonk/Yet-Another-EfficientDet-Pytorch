import os
import numpy as np

from PIL import Image, ImageEnhance

# minimum/maximum number of signs is added next to each annotation
MIN_NUM_SIGNS = 1
MAX_NUM_SIGNS = 3
# scale ratio for added trafic sign (avoiding added sign much smaller than existed sign in original image)
SCALE_RATIO = 0.7
# Brightness ratio
LOW_BRIGHTNESS_RATIO = 0.8
HIGH_BRIGHTNESS_RATIO = 1.3
# Rotation DEGREE
ROTATE_DEGREE = 20

def checking_size(size_sign1, size_sign2):
    return size_sign1[0] / size_sign2[0] < SCALE_RATIO and size_sign1[1] / size_sign2[1] < SCALE_RATIO 

def augment_sign(img):
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(np.random.uniform(LOW_BRIGHTNESS_RATIO, HIGH_BRIGHTNESS_RATIO))
    img = img.rotate(ROTATE_DEGREE)
    return img    



def add_signs(image, annotations, traffic_signs):
    for anno in annotations:
        num_new_sign = np.random.randint(MAX_NUM_SIGNS - MIN_NUM_SIGNS) + MIN_NUM_SIGNS
        bbox = anno['bbox']
        sign_size = (bbox[2], bbox[3])
        valid_traffic_signs = [ts for ts in traffic_signs if checking_size(tf.size, sign_size)]
            if (width / bbox[2] < SCALE_RATIO and height / bbox[3] < SCALE_RATIO)
        for sign_ind in range(num_new_sign):
            traffic_signs_id = np.random.randint(len(traffic_signs))
            added_traffic_sign = valid_traffic_signs[traffic_signs]
            added_traffic_sign = added_traffic_sign.resize(sign_size)
            added_traffic_sign = augment_sign(added_traffic_sign)
            added_pos = (bbox[0] + (sign_ind + 1) * sign_size, bbox[1])
            image.paste(added_traffic_sign, added_pos)
            new_anno = anno.copy()
            new_anno['bbox'][0] = added_pos[0]
            new_anno['bbox'][1] = added_pos[1]

