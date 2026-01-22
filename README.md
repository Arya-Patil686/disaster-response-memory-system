
# Disaster Response Memory System using Qdrant
## Overview
This project is an AI-powered disaster response memory system designed to support emergency decision-making.
It uses Qdrant as a long-term vector memory to store and retrieve multimodal disaster data including text reports, satellite images, and emergency call audio.

The system enables:

- Semantic search over past disaster events
- Long-term evolving memory with decay and reinforcement
- Evidence-based decision support for public safety scenarios

## Tech Stack

- Python 3.10+
- Qdrant (Vector Database)
- Sentence Transformers (Text Embeddings)
- FastAPI (Backend API)
- Torch / Torchvision (Image Embeddings)
- Faster-Whisper (Audio Transcription)
## Setup Instructions

1. Clone or unzip the project
cd disaster-response-memory

2. Create virtual environment
python -m venv venv
source venv/bin/activate   #for macOS

3. Install dependencies
pip install -r requirements.txt
## Running the Project

Step 1: Load initial disaster memory (text)
python data_loader.py

Step 2: Create multimodal collections
python create_image_collection.py
python create_audio_collection.py

Step 3: Store image memory
python store_image_data.py

Step 4: Store audio memory
python store_audio_data.py

Step 5: (Optional) Apply memory decay
python decay.py

Step 6: Start the API server
python -m uvicorn app:app --reload

## API Usage

Open browser:
http://127.0.0.1:8000/docs

Example search query:
/search?query=flood hospital emergency&location=Pune
## Project Features
- Multimodal retrieval (text, image, audio)
- Persistent long-term memory
- Memory decay and reinforcement
- Metadata-based filtering
- Evidence-backed outputs
## Limitations

- Demo uses sample disaster data
- Audio transcription is offline and optimized for short clips
- Final decision-making requires human oversight

## Ethical Considerations
- No personal or sensitive data is stored
- Audio data is treated as anonymized emergency logs
- System is designed as decision support, not autonomous control