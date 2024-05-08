import cv2

def get_filter(image):
    img = cv2.resize(image, (200,200))
    filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return filtered