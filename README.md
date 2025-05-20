# AI Doctor with Vision and Voice 🩺🖼️🎤

## Overview  
Meet your AI-powered medical assistant that listens to patient concerns, analyzes medical images, and provides natural, spoken doctor-like diagnoses. Combining state-of-the-art models for speech recognition, image understanding, and realistic voice synthesis, all within a sleek Gradio interface — this app makes medical AI accessible and interactive.

---

## Features  

- 🎙️ **Speech-to-Text:** Converts patient audio into accurate text using Groq's Whisper model.  
- 🖼️ **Image Analysis:** Understands and interprets uploaded medical images with a powerful vision-language model.  
- 🗣️ **Text-to-Speech:** Responds in a warm, natural doctor’s voice via ElevenLabs API.  
- 🖥️ **Intuitive UI:** Clean, easy-to-use web interface built with Gradio for seamless interaction.

---

## How It Works  

1. Patient speaks their symptoms or questions through a microphone and optionally uploads a medical image.  
2. The app transcribes speech, analyzes images, and generates a medical response.  
3. The response appears as text and is also played aloud, mimicking a doctor's tone.

---

## Tech Stack  

- Python  
- Gradio (Web Interface)  
- Groq API (Speech-to-Text)  
- LLaMA 3 Model (Vision-Language for Image Analysis)  
- ElevenLabs API (Voice Generation)  
- OpenAI / Hugging Face Transformers (Model Integrations)

---

## Setup Instructions  

```bash
git clone https://github.com/your-username/ai-doctor-vision-voice.git
cd ai-doctor-vision-voice
python -m venv medical_env
source medical_env/bin/activate  # On Windows: medical_env\Scripts\activate
pip install -r requirements.txt
