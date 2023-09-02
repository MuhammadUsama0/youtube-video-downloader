from pytube import YouTube

url = "" #Enter Your youtube Url here

try:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()  # Get the highest resolution stream
    stream.download(filename=f"{video.title}.mp4")
    print("The video is downloaded in MP4")
except KeyError:
    print("Unable to fetch video information. Please check the video URL or your network connection.")
