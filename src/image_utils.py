import cv2
from PIL import Image
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    return image

def convert_opencv_to_pil(opencv_image):
    # Convertir l'image OpenCV en format RGB
    rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

    # Créer un objet PIL.Image à partir de l'image RGB
    pil_image = Image.fromarray(rgb_image)

    return pil_image

def get_optimal_size(image_size, label_size):
    image_width, image_height = image_size
    label_width, label_height = label_size

    image_ratio = image_width / image_height
    label_ratio = label_width / label_height

    if image_ratio > label_ratio:
        new_width = label_width
        new_height = int(label_width / image_ratio)
    else:
        new_height = label_height
        new_width = int(label_height * image_ratio)

    return new_width, new_height

def extract_image_portion(image, x1, y1, x2, y2):

    # Extraire la portion de l'image
    portion = image[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)]

    # Retourner la portion extraite de l'image
    return portion

def get_coords(x, y, w, h, W, H):
    return int((w * x) / W), int((h * y) / H)

def mask_polygon(image, points):
    
    # Créer un masque d'image vide avec la même taille que l'image originale
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    
    # Convertir les points du polygone en un format utilisable par OpenCV
    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    
    # Créer un masque rempli avec les pixels à l'intérieur du polygone
    cv2.fillPoly(mask, [pts], (255,))
    
    # Appliquer le masque sur l'image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result

def getContours(image, imgBox, min_area, max_area):
        count = 0
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if min_area < area < max_area:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                x, y, w, h = cv2.boundingRect(approx)

                # cv2.rectangle(imgBox, (x, y), (x + w, y +h), (0, 0, 255), 1)
                cv2.circle(imgBox,(x + int(w/2), y + int(h/2)),1,(0, 0, 255),-1)

                count += 1
        
        return count

def hsv(image,
        min_hue, max_hue,
        min_saturation, max_saturation,
        min_value, max_value,
        min_threshold, max_threshold,
        min_area, max_area,
        blur, erode, dilate,
        inverse):
    
    if inverse:
        image = inverse_colors(image)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (min_hue, min_saturation, min_value), (max_hue, max_saturation, max_value))
    imghsv = cv2.bitwise_and(image, image, mask=mask)

    imgGray = cv2.cvtColor(imghsv, cv2.COLOR_BGR2GRAY)

    if blur > 1:
        median = cv2.medianBlur(imgGray, blur)
    else:
        median = imgGray

    _, dst = cv2.threshold(median, min_threshold, max_threshold, cv2.THRESH_BINARY)

    if erode > 1:
        kernel1 = np.ones((erode, erode), np.uint8)
        dst = cv2.erode(dst, kernel1)

    if dilate > 1:
        kernel2 = np.ones((dilate, dilate), np.uint8)
        dst = cv2.dilate(dst, kernel2)

    count = getContours(dst, image, min_area, max_area)

    return image, dst, count

def inverse_colors(image):
    inverted_image = cv2.bitwise_not(image)
    return inverted_image