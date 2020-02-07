import os
import speech_recognition as sr

tomp3 = "ffmpeg -i /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture2.webm /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.mp3"
towav = "ffmpeg -i /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.mp3 /home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.wav"

os.system(tomp3)
os.system(towav)

r = sr.Recognizer()

with sr.AudioFile("/home/jasmeet/PycharmProjects/shikshak/video_lectures/Lecture1.wav") as source:
    audio = r.record(source, duration=100)

try:
    text = r.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0} ".format(e))



