import os
import speech_recognition as sr
import requests
import json

headers = {
        'Host': 'api.smrzr.io',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://smrzr.io/',
        'Content-Type': 'raw/text',
        'Origin': 'https://smrzr.io',
        'Content-Length': '838',
        'Connection': 'keep-alive',
        'TE': 'Trailers'
}
url = "https://api.smrzr.io/summarize?ratio=0.15"

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
    r = requests.post(url=url, headers=headers, data=json.dumps(text))
    print(r)
    print(r.text)


except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0} ".format(e))



