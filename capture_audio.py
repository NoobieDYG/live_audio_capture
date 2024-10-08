import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

#def list_devices():
    #print(sd.query_devices())

#list_devices()

'''device_number=3 #got this from list of devices using sounddevice lib
fs=16000
duration = 1 #duration of recording
output_file="chunk.wav" #opened new file to save the recording'''


#saving audio
def recording_audio_from_livestream():
    device_number=3 #got this from list of devices using sounddevice lib
    fs=16000
    duration = 1 #duration of recording
    output_file="chunk.wav" #opened new file to save the recording

    audio = sd.rec(int(duration*fs),samplerate=fs,channels=1,dtype="int16",device=device_number)
    print("...recording")
    sd.wait()
    write(output_file, fs, audio)  #output file , rate , the audio recorded
    #sd.play(audio,fs)
    #sd.wait()
    return audio 

recording_audio_from_livestream() #calling function