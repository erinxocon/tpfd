import speech_recognition as sr
import tpfd

#instantiate parser
p = tpfd.Parser()

#Set up basic rule that looks for the string blank song,
#e.x. play song, next song, previous song
@p.on_parse('{Action} song')
def main(action):
    print(action)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

#try and recognize the captured audio and pass the recognized
#phrase to the parse method
try:
    string = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + string)
    p.parse(string)