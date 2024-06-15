from prediction import predict_user_score, detect_post_content
from repository import input , features
import cv2
from skimage.feature import hog
from skimage import exposure
import numpy as np

def get_hog_feature(gray_image):
    hogfv, hog_image = hog(gray_image, orientations=9, pixels_per_cell=(16, 16),
                           cells_per_block=(2, 2), visualize=True)
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 5))
    return hog_image_rescaled

def check_image():
    target_size = (200,200)
    image = cv2.imread('image.jpg')
    image = cv2.resize(image, target_size)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_array = get_hog_feature(gray_image)
    numpy_array = np.array([img_array])
    print("np ",numpy_array)
    n_samples, height, width = numpy_array.shape
    X_reshaped = numpy_array.reshape(n_samples, height * width)
    post = detect_post_content(X_reshaped)
    return post
# check_image()