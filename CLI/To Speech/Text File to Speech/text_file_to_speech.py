from gtts import gTTS
import os

file = open("draft.txt", "r").read().replace("\n", " ")
language = 'en'
speech = gTTS(text=str(file), lang=language, slow=False)
speech.save('voice.mp3')
os.system('start voice.mp3')
