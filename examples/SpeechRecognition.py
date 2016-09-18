import speech_recognition as sr
import tpfd

p = tpfd.Parser()

@p.on_recognize('{Play} song')
def main(kwargs):
    print(kwargs.get('play'))

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    string = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + string)
    p.parse_string(string)