import numpy as np
import tensorflow as tf
from PIL import Image

def test_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]
    
    # Generate dummy image
    img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    
    # Trial 1: [0, 1]
    input_0_1 = (img / 255.0).astype(np.float32)
    input_0_1 = np.expand_dims(input_0_1, axis=0)
    interpreter.set_tensor(input_details['index'], input_0_1)
    interpreter.invoke()
    out_0_1 = interpreter.get_tensor(output_details['index'])[0]
    
    # Trial 2: Z-score (PyTorch)
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    input_z = ((img / 255.0) - mean) / std
    input_z = np.expand_dims(input_z.astype(np.float32), axis=0)
    interpreter.set_tensor(input_details['index'], input_z)
    interpreter.invoke()
    out_z = interpreter.get_tensor(output_details['index'])[0]
    
    # Trial 3: [-1, 1] (TF standard)
    input_neg1_1 = ((img / 127.5) - 1.0).astype(np.float32)
    input_neg1_1 = np.expand_dims(input_neg1_1, axis=0)
    interpreter.set_tensor(input_details['index'], input_neg1_1)
    interpreter.invoke()
    out_neg1_1 = interpreter.get_tensor(output_details['index'])[0]

    print("Raw output for [0, 1]:", out_0_1)
    print("Raw output for Z-score:", out_z)
    print("Raw output for [-1, 1]:", out_neg1_1)

test_model('assets/models/eye_disease_mobile.tflite')
