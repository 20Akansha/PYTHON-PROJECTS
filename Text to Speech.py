from gtts import gTTS
import os
f=open("py projects.py")
x=f.read()

language="en"
audio=gTTS(text=x,slow=False)

audio.save("audio.wav")
os.system("audio.wav")


