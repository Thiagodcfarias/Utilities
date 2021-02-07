import pytube as p
from moviepy.editor import VideoFileClip

# edit this variables
url = 'https://www.youtube.com/playlist?list=PLt8FmCIXMl280bnpT4VAotkVkcN33R8qL'
path = 'C:\\Users\\Casa\\.spyder-py3\\'

playlist = p.Playlist(url)

for video in playlist.videos:
    video = video.streams.get_highest_resolution()
    video.download()
    
    mp4_file = path + video.title + '.mp4'
    mp3_file = path + video.title + '.mp3'
    
    print(mp4_file)
    
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
