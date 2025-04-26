# Text-to-image-using-Transformers
This project will take a text prompt as input and generate an image using a pretrained Stable Diffusion model.

## Note 
1. before running this project create a environment using Venv
2. if system is having CPU, it may take time, though CUDA is compitable with Nvidia processors.
3. First install requirements using pip.

## create virtual environment 
python -m venv venv

venv\Scripts\activate


## install dependencies
 pip install torch torchvision transformers diffusers accelerate gradio


## Run
python app.py
