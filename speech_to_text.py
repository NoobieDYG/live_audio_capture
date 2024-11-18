import requests
import whisper

model = whisper.load_model("small")

audio_path=r" capture\chunk.wav"

result = model.transcribe(audio_path)

print("Transcription:",result["text"])
