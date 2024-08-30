import moviepy.editor
# Replace the parameter with the location of your file
video = moviepy.editor.VideoFileClip(input())
audio = video.audio
# Replace the parameter with the location along with filename
audio.write_audiofile('E:\Songs\sample.mp3')
