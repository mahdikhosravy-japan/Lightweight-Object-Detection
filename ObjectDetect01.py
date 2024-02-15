import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

# Path to the directory containing the saved model files
model_path = 'C:/Users/kcg-staff/PycharmProjects/LightObjectDetection01/models/research/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'


# Load the saved model
model = tf.saved_model.load(model_path)

# Access a specific signature (e.g., 'serving_default')
serving_default_signature = model.signatures["serving_default"]

# Access input and output tensor names
input_tensor_names = list(serving_default_signature.structured_input_signature[1].keys())
output_tensor_names = list(serving_default_signature.structured_outputs.keys())

# Read the image # The path should be to your image
#img = np.array(cv2.imread('C:/Users/kcg-staff/Downloads/Conveyorbelt_wrapper-20240210T073222Z-001/Conveyorbelt_wrapper/Testing/0000.jpg'))
img = np.array(cv2.imread('C:/Users/kcg-staff/Downloads/ezyzip/vegitabr.jpg'))

# Create a batch tensor from the image (adjust batch size as needed)
input_tensor = tf.convert_to_tensor([img], dtype=tf.uint8)

# Perform inference
output_tensors = serving_default_signature(**{input_tensor_names[0]: input_tensor})

# Retrieve results from output tensors (modify based on actual output tensor names)
result_boxes = output_tensors['detection_boxes'].numpy()
result_scores = output_tensors['detection_scores'].numpy()

# Draw bounding boxes on the image (modify based on actual output tensor names)
for box, score in zip(result_boxes[0], result_scores[0]):
    if score > 0.2:
        y_min, x_min, y_max, x_max = box
        img = cv2.rectangle(img, (int(x_min * img.shape[1]), int(y_min * img.shape[0])),
                            (int(x_max * img.shape[1]), int(y_max * img.shape[0])), (0, 255, 0), 2)

# Show the result
plt.imshow(img)
plt.colorbar()
plt.show()