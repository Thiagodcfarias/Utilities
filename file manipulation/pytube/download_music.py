import pytube

url = 'https://www.youtube.com/watch?v=C01ctNg0y5E'
path = 'C:\\Users\\Casa\\Desktop'

musica = pytube.YouTube(url).streams.filter(only_audio=True).first()
nome_musica = musica.title.replace('|','') # be careful with special characters in music´s name, it´s rainsing OSError [Errno 22] 
musica.download(output_path = path, filename = nome_musica + '.mp3')
