AI Doctor with Vision and Voice 🩺🖼️🎤

Overview
This project simulates an AI-powered medical assistant that can listen to patient concerns, analyze medical images, and respond with a natural, spoken doctor-like diagnosis. It combines cutting-edge AI models for speech recognition, image understanding, and realistic voice generation — all wrapped in an intuitive Gradio interface.

Features
🎙️ Speech to Text: Converts patient audio input into text using Groq's Whisper model.

🖼️ Image Analysis: Analyzes uploaded medical images and answers based on visual content.

🗣️ Text to Speech: Generates a doctor's voice response using ElevenLabs API.

🖥️ Web App Interface: Simple, clean UI built with Gradio for easy interaction.

How It Works
Patient speaks through the microphone and optionally uploads a medical image.

The app transcribes the voice, analyzes the image, and generates a medical response.

The response is both displayed as text and played as audio mimicking a doctor's tone.

Tech Stack
Python

Gradio (UI)

Groq API (Speech-to-Text)

LLaMA 3 Model (Vision-Language Model for Image Analysis)

ElevenLabs API (Voice Generation)

OpenAI / Hugging Face Transformers (for model integrations)

Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/ai-doctor-vision-voice.git
cd ai-doctor-vision-voice
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv medical_env
source medical_env/bin/activate  # On Windows: medical_env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API keys in the environment variables:

GROQ_API_KEY

ElevenLabs API key (inside your voice_of_doctor.py)

Run the app:

bash
Copy
Edit
python app.py
Folder Structure
Copy
Edit
├── app.py
├── brain_of_the_doc.py
├── voice_of_patient.py
├── voice_of_doctor.py
├── requirements.txt
└── README.md
Notes
This app is for learning and experimental purposes only, not for real medical advice.

Please ensure ethical and responsible use of AI tools, especially in sensitive fields like healthcare.

License
MIT License
