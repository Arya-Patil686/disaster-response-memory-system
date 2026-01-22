from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer
from audio_to_text import audio_to_text

client = QdrantClient(path="qdrant_data")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert audio to text
transcript = audio_to_text("audio/emergency_call.wav")

vector = model.encode(transcript).tolist()

point = PointStruct(
    id=200,
    vector=vector,
    payload={
        "modality": "audio",
        "location": "Pune",
        "type": "Flood",
        "importance": 1.0,
        "transcript": transcript,
        "description": "Emergency call reporting flooded hospital"
    }
)

client.upsert(
    collection_name="disasters_audio",
    points=[point]
)

print("Audio disaster memory stored!")
print("Transcript:", transcript)
