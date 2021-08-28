import pytube

url = 'https://www.youtube.com/watch?v=YDVAQI-4lto'
path = 'C:\\Users\\Casa\\Desktop'
nome_musica = 'These days'

pytube.YouTube(url).streams.filter(only_audio=True).first().download(output_path = path, filename = nome_musica + '.mp3')
