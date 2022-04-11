import matplotlib.pyplot as plt
from absl import logging
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
from scipy.spatial import cKDTree
from skimage.feature import plot_matches
from skimage.measure import ransac
from skimage.transform import AffineTransform
from six import BytesIO
import tensorflow as tf
import tensorflow_hub as hub
from six.moves.urllib.request import urlopen
import urllib.request
import skimage
import os
import json

import csv
import codecs
import glob
from itertools import accumulate
from os import walk
import pandas as pd
import numpy as np
import ast

delf = hub.load('model').signatures['default']
destfolder='./data/Train/Train1/raw/'
result_path = './data/Test/results/true/'
result_path_false = './data/Test/results/false/'
path_im_test = './data/Test/resized/'
path_test = './data/Test/final_test_ciphered/'

def download_and_resize(name, url, new_width=256, new_height=256):
  urllib.request.urlretrieve(url, name)
  image = Image.open(name)
  image = ImageOps.fit(image, (new_width, new_height), Image.ANTIALIAS)
  image = image.convert('RGB')
  return image

def run_delf(image):
  np_image = np.array(image)
  float_image = tf.image.convert_image_dtype(np_image, tf.float32)

  return delf(
      image=float_image,
      score_threshold=tf.constant(100.0),
      image_scales=tf.constant([0.25, 0.3536, 0.5, 0.7071, 1.0, 1.4142, 2.0]),
      max_feature_num=tf.constant(1000))

def match_images(data, result2):
    distance_threshold = 0.6

    num_features_1 = len(data['locations'])
    num_features_2 = result2['locations'].shape[0]

    d1_tree = cKDTree(data['descriptors'])
    _, indices = d1_tree.query(
        result2['descriptors'],
        distance_upper_bound=distance_threshold)

    locations_2_to_use = np.array([
        result2['locations'][i,]
        for i in range(num_features_2)
        if indices[i] != num_features_1
    ])
    locations_1_to_use = np.array([
        data['locations'][indices[i]]
        for i in range(num_features_2)
        if indices[i] != num_features_1
    ])

    _, inliers = ransac(
        (locations_1_to_use, locations_2_to_use),
        AffineTransform,
        min_samples=3,
        residual_threshold=20,
        max_trials=1000)
    return {"inliers": sum(inliers)}

def resize_image(srcfile, destfile, new_width=256, new_height=256):
    pil_image = Image.open(srcfile)
    pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)
    pil_image_rgb = pil_image.convert('RGB')
    pil_image_rgb.save(destfile, format='JPEG', quality=90)

def prognoz(path_im_test, name_test, list_f, destfolder, result_path):
    result1 = run_delf(Image.open(path_im_test+name_test))
    inliers_counts = {}
    inliers_counts['name'] = name_test
    inliers_rez = []
    for i in list_f:
        j = i.split('.json')[0]
        with open(destfolder+i, 'r') as fp:
            data = json.load(fp)
        try:
            result = match_images(data, result1)
            inliers_rez.append({"index": j, "inliers": int(result['inliers'])})
        except:
            pass
    top_match = sorted(inliers_rez, key=lambda k: k['inliers'], reverse=True)[0]
    inliers_counts['index'] = top_match['index']
    inliers_counts['inliers'] = top_match['inliers']
    with open(result_path+name_test.split('.jpg')[0]+'.json', 'w') as fp:
        json.dump(inliers_counts, fp)

def MODEL():
    for srcfile in glob.iglob(os.path.join(path_test, '*.[Jj][Pp][Gg]')):
        src_basename = os.path.basename(srcfile)
        destfile=os.path.join(path_im_test,src_basename)
        resize_image(srcfile, destfile)

    list_f = []

    for (dirpath, dirnames, filenames) in walk(destfolder):
        list_f.extend(filenames)
        break

    list_test =[]

    for (dirpath, dirnames, filenames) in walk(path_im_test):
        list_test.extend(filenames)
        break

    for test in list_test:
        print (test)
        try:
            prognoz(path_im_test, test, list_f, destfolder, result_path)
        except:
            lm = {}
            lm['name'] = test
            with open(result_path_false+test.split('.jpg')[0]+'.json', 'w') as fp:
                json.dump(lm, fp)

    list_true = []

    for (dirpath, dirname, filenames) in walk(result_path):
        list_true.extend(filenames)
        break

    list_false = []

    for (dirpath, dirname, filenames) in walk(result_path_false):
        list_false.extend(filenames)
        break

    with open ('./data/results/false_results.csv', 'w', newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['filename'])
        for i in list_false:
            writer.writerow([i.replace('.json','.jpg')])

    with open ('./data/results/true_results.csv', 'w', newline='') as csvfile:
        writer=csv.writer(csvfile, delimiter=';')
        writer.writerow(['image','filename','entitity'])
        for i in list_true:
            with open(result_path+'/'+ i) as fp:
                b = ast.literal_eval(fp.read())
                writer.writerow([b['name'],b['index'],b['inliers']])
                
    data_train = pd.read_csv('./data/Train/Train1/train_labels.csv', sep =';')
    data_test_true = pd.read_csv('./data/results/true_results.csv', sep =';')
    comm_true = data_train.merge(data_test_true, on=['filename'])
    true = comm_true[['latitude','longitude']]
    return([true.iloc[0:]['latitude'], true.iloc[0:]['longitude']])
