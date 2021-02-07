import pytube as p

# edit this variables
url = 'https://www.youtube.com/playlist?list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe'
path = 'path'

playlist = p.Playlist(url)

for video in playlist.videos:
    video = video.streams.get_audio_only()
    video.download(output_path = path)
