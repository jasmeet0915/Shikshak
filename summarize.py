import os


tomp3 = "ffmpeg -i /video_lectures/Lecture1.mp4 /video_lectures/Lecture1.mp3"
towav = "ffmpeg -i /video_lectures/Lecture1.mp3 /video_lectures/Lecture1.wav"

os.system(tomp3)
os.system(towav)

