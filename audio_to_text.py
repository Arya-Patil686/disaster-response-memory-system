from faster_whisper import WhisperModel

# Use small model for speed + reliability
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def audio_to_text(audio_path: str) -> str:
    segments, _ = model.transcribe(audio_path)

    transcript = ""
    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()
