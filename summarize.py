import os
import speech_recognition as sr
from summarizer import Summarizer


model = Summarizer()

tomp3 = "ffmpeg -i /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture2.webm /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.mp3"
towav = "ffmpeg -i /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.mp3 /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.wav"

print(".....converting videos....")
os.system(tomp3)
os.system(towav)
print("....videos converted....")

r = sr.Recognizer()

with sr.AudioFile("/home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.wav") as source:
    audio = r.record(source, duration=100)

try:
    print("...converting speech to text...")
    text = r.recognize_google(audio)
    print(text)
    print("...speech-to-text done...")
    print("...summarizing...")
    summary = model(text, min_length=60)
    final = ''.join(summary)
    print("...summarized...\n")
    print(final)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0} ".format(e))



