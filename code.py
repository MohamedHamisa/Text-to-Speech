# install the module
!pip install gTTS

from gtts import gTTS
import os

# input
text = 'Welcome to Hackers Realm. It contains tutorial videos on technology'

# convert text to speech
text_to_speech = gTTS(text=text, lang='en', slow=False)

# save the audio file
text_to_speech.save('test.mp3')

# play the audio
os.system('test.mp3')


#Pyttsx - Offline
# install the module
!pip install pyttsx3


import pyttsx3

# input
text = 'Welcome to Hackers Realm. It contains tutorial videos on technology'

# initialize the module
text_to_speech = pyttsx3.init()

# adjust the speed
text_to_speech.setProperty('rate', 150)

# change the voice
voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[1].id) # 0 for male and 1 for female

# convert text to speech
text_to_speech.say(text)

# save the audio file
text_to_speech.save_to_file(text, 'test.mp3')

# listen to audio
text_to_speech.runAndWait()
