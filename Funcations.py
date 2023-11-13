import cv2
import numpy as np

# Function to preprocess image
def preprocessed_image(img_path):
    
    # Step 1: Read image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Step 2: apply Gaussian blur
    img = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Step 3: image histogram equalization
    img = cv2.equalizeHist(img)
    
    #return preprocessed image
    return img 

# Funcation extra features
def extra_features(image):
    
    # Step 1: image resize
    image_resize = cv2.resize(image, (32, 32))
    
    # Step 2: flalten image
    featrures = image_resize.flatten()
    
    return featrures

def match_funcations(fingerPrintImag1,fingerPrintImag2):

    destance = np.linalg.norm(fingerPrintImag1 - fingerPrintImag2)
    
    #threshold 
    threshold = 80
    
    if destance < threshold:
        return True
    else:
        return False