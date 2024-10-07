import requests
import whisper

model = whisper.load_model("small")

audio_path=r"C:\Users\Affaan Jaweed\Desktop\Live audio capture\chunk.wav"

result = model.transcribe(audio_path)

print("Transcription:",result["text"])


#ok done