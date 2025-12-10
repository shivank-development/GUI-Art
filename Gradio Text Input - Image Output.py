import gradio as gr
from PIL import Image
import requests

emoji_map = {
    "cat": "https://tinyurl.com/2p8y6s2x",  # Example placeholder URL
    "dog": "https://tinyurl.com/2p8f4c6v"   # Example placeholder URL
}

def show_emoji(word):
    url = emoji_map.get(word.lower(), "https://tinyurl.com/2p87zx7b")  # Fallback image
    return Image.open(requests.get(url, stream=True).raw)

gr.Interface(show_emoji, "text", "image", title="Emoji Lookup").launch(share=False)
