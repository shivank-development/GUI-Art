from pytube import YouTube

url = input("Enter YouTube video URL: ")
yt = YouTube(url)

print("Title:", yt.title)

stream = yt.streams.get_highest_resolution()

print("Downloading:", stream.resolution)
stream.download(output_path="downloads")

print("Download complete!")


#Show available resolutions
"""
for s in yt.streams.filter(progressive=True):
    print(s.resolution)
"""


#Download only audio (MP3 style)
"""audio = yt.streams.filter(only_audio=True).first()
audio.download(output_path="downloads")
"""