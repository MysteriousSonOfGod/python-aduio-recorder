import sounddevice
from scipy.io.wavfile import write

fps = 44100
duration = 10
record_name = input("file name: ")
print("recording....")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("Done.")

write(f"{record_name}.wav", fps, recording)
