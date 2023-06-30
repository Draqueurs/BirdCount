import cv2
import numpy as np
import os
import configparser
import image_utils

class ImageAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.image_process = self.image.copy()
        self.image2display = self.image.copy()
        self.height, self.width, _ = self.image_process.shape

    def get_image(self):
        return self.image
    
    def set_image(self, image_path=None, image=None):
        if image_path is not None:
            self.image_path = image_path
            self.image = cv2.imread(image_path)
        else:
            self.image = image
        self.image_process = self.image.copy()

    def get_image2display(self):
        return self.image2display
    
    def set_image2display(self, image):
        self.image2display = image
        self.set_width_height()

    def get_image_process(self):
        return self.image_process
    
    def set_image_process(self, image=None):
        if image is None:
            self.image_process = self.image.copy()
        else:
            self.image_process = image
        self.set_width_height()
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_width_height(self):
        self.height, self.width, _ = self.image2display.shape

    def hsv(self, min_hue, max_hue,
            min_saturation, max_saturation,
            min_value, max_value,
            min_threshold, max_threshold,
            min_area, max_area,
            blur, erode, dilate,
            inverse,
            save_path):

        if save_path is not None:
            image_process_tmp = self.image_process.copy()
            image2display_tmp = self.image2display.copy()
            self.image_process = self.image.copy()

        self.image2display = self.image_process.copy()

        image, dst, self.count = image_utils.hsv(
            self.image2display,
            min_hue, max_hue,
            min_saturation, max_saturation,
            min_value, max_value,
            min_threshold, max_threshold,
            min_area, max_area,
            blur, erode, dilate,
            inverse)

        # Convert grayscale image to 3-channel image, so that they can be stacked together
        imgc = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        both = np.concatenate((imgc, image), axis=1)

        if save_path is not None:
            cv2.imwrite(os.path.join(save_path, os.path.basename(self.image_path) + '_dot.png'), self.image2display)
            cv2.imwrite(os.path.join(save_path, os.path.basename(self.image_path) + '_dst.png'), dst)

            config = {
                'HUE': {'min': min_hue, 'max': max_hue},
                'SATURATION': {'min': min_saturation, 'max': max_saturation},
                'VALUE': {'min': min_value, 'max': max_value},
                'THRESHOLD': {'min': min_threshold, 'max': max_threshold},
                'AREA': {'min': min_area, 'max': max_area},
                'BLUR': {'value': blur},
                'ERODE': {'value': erode},
                'DILATE': {'value': dilate},
                'COUNT': {'count': self.count}
            }

            config_parser = configparser.ConfigParser()
            for section, options in config.items():
                config_parser[section] = options

            with open(os.path.join(save_path, os.path.basename(self.image_path) + '_config.ini'), 'w') as configfile:
                config_parser.write(configfile)

            self.image_process = image_process_tmp
            self.image2display = image2display_tmp

        else:
            self.set_image2display(both)

    def analyze(self,
        min_hue, max_hue,
        min_saturation, max_saturation,
        min_value, max_value,
        min_threshold, max_threshold,
        min_area, max_area,
        blur, erode, dilate,
        inverse,
        save_path):
        # Effectuer des analyses supplémentaires sur l'image ici
        # Exemple : calculer des statistiques, détecter des contours, etc.
        self.hsv(
            min_hue, max_hue,
            min_saturation, max_saturation,
            min_value, max_value,
            min_threshold, max_threshold,
            min_area, max_area,
            blur, erode, dilate,
            inverse,
            save_path
        )

    def display_image(self):
        cv2.imshow('Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
