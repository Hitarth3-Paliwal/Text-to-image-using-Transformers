import gradio as gr
from model import generate_image

def generate(prompt):
    """
    Calls the image generation function with the given prompt.
    """
    image_path = generate_image(prompt)
    return image_path

# Gradio Interface
iface = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Enter text prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="AI Text-to-Image Generator",
    description="Enter a text prompt and generate an AI-generated image using Stable Diffusion.",
    allow_flagging="never"
)

# Launch the Web App
if __name__ == "__main__":
    iface.launch(share=True)
