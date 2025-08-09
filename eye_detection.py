import cv2
import numpy as np
from tensorflow.keras.models import load_model

class EyeDetector:
 def __init__(self,model_path='model_mobilenet4.h5',image_size=(48, 48),threshold=0.5):
		self.model = load_model(model_path)
		self.image_size = image_size
		self.threshold = threshold

 def detect(self, frame):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  resized = cv2.resize(gray,self.image_size)/255.0
  x = resized.reshape(1, *self.image_size, 1)
  p = self.model.predict(x)[0][0]
  is_open = p > self.threshold
  return is_open, p

