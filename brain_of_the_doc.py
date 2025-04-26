#step one setup GROQ api key
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
import base64 #convets bit and bytes to string

def encode_image(image_path):
    image_file = open (image_path, "rb") #open image in binary mode
    return base64.b64encode(image_file.read()).decode("utf-8") #encode image to base64 string


#setup multimodal llm
from groq import Groq

def analyze_image_with_query(query, model, encoded_image):

    client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": 
                    {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                        "image": encoded_image
                    },
            },
        ],
    }]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return (chat_completion.choices[0].message.content)