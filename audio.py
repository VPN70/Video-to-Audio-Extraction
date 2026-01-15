from moviepy import VideoFileClip
import pyttsx3
import speech_recognition as sr

# load the video
video=VideoFileClip("D:\\audio\\audio.mp4")

#extract the audio  from the video
audio_file=video.audio
audio_file.write_audiofile("11.wav")

# intiliaze recognizer
r= sr.Recognizer()

# load the audio file
with sr.AudioFile("11.wav") as sourse:
    data= r. record(sourse)

# convert speech to text
text=r.recognize_google(data)

#print he data
print("\nThe resultant text from video is: \n")
print(text)

engine=pyttsx3.init()
engine.runAndWait()