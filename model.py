from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime

# Load Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to(device)

def generate_image(prompt, num_inference_steps=50, guidance_scale=7.5):
    """
    Generate an image based on the input text prompt.
    """
    image = pipe(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]
    
    # Save the image
    if not os.path.exists("static"):
        os.makedirs("static")
    filename = f"static/generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    image.save(filename)
    
    return filename
