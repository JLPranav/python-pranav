from pytube import YouTube
# Install the required module using pip
# "pip install pytube"
link = input("enter ur youtube url : ")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
dn_video = videos[2]
dn_video.download()
print(" downloaded successfully ")
