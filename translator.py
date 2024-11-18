import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import requests
import whisper
import tkinter as tk
from capture_audio import recording_audio_from_livestream
from subtitle_display import subtitle_display
#loading whisper model

model = whisper.load_model("small")
def transcribe_live():
    recording_audio_from_livestream()
    audio_path=r"enter_locwtion"
    result = model.transcribe(audio_path)

    english_text=result['text']
    subtitle_label.config(text=english_text)
    root.update()

root = tk.Tk()
root.title("Live Subtitles")
root.geometry("800x100")
subtitle_label = tk.Label(root, text="", font=("Arial", 24), wraplength=700)
subtitle_label.pack()

def start_live_translation():
    while True:
        transcribe_live()

root.after(1000,start_live_translation)
root.mainloop()

#ready
