# For installaiton of object-detection module

To install the object-detection module in PyCharm, you need to follow these steps:
## 1. Create a Virtual Environment:
It's good practice to use a virtual environment to manage your project. 
 Create a virtual environment named "venv"
 Go in terminal (Alt F12), then run 
> 'python -m venv venv'te a virtual environment named "venv"python -m venv 

Activate the Virtual Environment (for Windows):
## 2. Activate the virtual environment
Terminal> venv\Scripts\activate

# 3. Install TensorFlow:
Make sure you choose a version compatible with the object_detection module.
Install other dependencies needed for the object detection module:
Terminal> pip install opencv-python-headless matplotlibstall opencv-python-headless matplotlib


### Download TensorFlow Models Repository:
Download the TensorFlow Models repository from GitHub, which contains the object_detection module.
At the Terminal
>  git clone https://github.com/tensorflow/models.git


# 4. Update PYTHONPATH:
e the TensorFlow Models repository
Add the research directory from the downloaded models to your PYTHONPATH. This allows Python to find the object_detection module.
Go to  Windows Command Prompt
> set PYTHONPATH=%PYTHONPATH%;C:\Users\kcg-staff\PycharmProjects\pythonProject1\models

This path is for my KCG notebook pc: C:\Users\kcg-staff\PycharmProjects\pythonProject1\models
# 5. Verify Installation:
Open PyCharm, and in your Python script or notebook, try importing module: 
> from object_detection.utils import label_map_util                      \
> from object_detection.utils import visualization_utils as vis_util

If it recognize them but giving some error from inside he module, then it means the modules are installed, then ignor the error
Remember to activate your virtual environment whenever you work on your project:
On Windows: 
> venv\Scripts\activate

On Linux or macOS: 
> source venv/bin/activate

These steps assume you have Git installed on your system. If not, you can download the repository manually from https://github.com/tensorflow/models and extract it into your project directory.


—--
# Downloading and using a model from the TensorFlow Model Zoo: 
It is how to download a model and used with object-detection module, the case of 'ObjectDetect01' is without inference, without key labels and just putting box around the object. 

Download the model from 
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md
Extract the downloaded model.
It is a zipped *.gz file, unzip it. 



Copy the model folder in the folder considered for your project models. 
In our case of taking a model from TensorFlow Model Zoo, Ensure that this path directly contains the necessary files like saved_model.pb, pipeline.config, and others.
The path to the model is determined as (in our case)
> model_path = 'C:/Users/kcg-staff/PycharmProjects/pythonProject1/models/research/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'

Ensure that this path directly contains the necessary files like saved_model.pb, pipeline.config, and others, also it should has the files and subfolders as follows: 
ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/                                                \
|-- saved_model.pb                                                                            \
|-- variables/                                                                                \
|   |-- variables.data-*                                                                      \
|   |-- variables.index                                                                       \




