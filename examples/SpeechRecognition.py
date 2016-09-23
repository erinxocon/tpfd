import speech_recognition as sr
import tpfd

p = tpfd.Parser()

@p.on_parse('{Action} song')
def main(action):
    print(action)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    string = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + string)
    p.parse(string)