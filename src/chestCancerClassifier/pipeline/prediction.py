import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0
        # Get raw predictions (probabilities)
        predictions = model.predict(test_image)
        print(f"Raw predictions: {predictions}")
        
        # Get predicted class index
        result = np.argmax(predictions, axis=1)
        print(f"Predicted class index: {result}")
        
        # Get confidence score (probability of predicted class)
        confidence = float(np.max(predictions))
        
        # Get probabilities for each class
        # Class order depends on how ImageDataGenerator sorted folders (alphabetically)
        # Adenocarcinoma folder comes before Normal alphabetically
        prob_adenocarcinoma = float(predictions[0][0])
        prob_normal = float(predictions[0][1])
        
        if result[0] == 0:
            prediction = "Adenocarcinoma Cancer"
        else:
            prediction = "Normal"
        
        return [{
            "image": prediction,
            "confidence": confidence,
            "probabilities": {
                "Adenocarcinoma Cancer": prob_adenocarcinoma,
                "Normal": prob_normal
            }
        }]