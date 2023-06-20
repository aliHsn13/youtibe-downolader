
from pytube import YouTube

link = input("Enter the YouTube video link: ")

try:
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    if stream:
        stream.download()
        print("Video downloaded successfully!")
    else:
        print("Unable to find a stream with highest resolution.")
except Exception as e:
    print("An error occurred:", str(e))
