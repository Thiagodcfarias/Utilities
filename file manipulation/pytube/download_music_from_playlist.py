import pytube as p

# edit this variables
url = 'https://www.youtube.com/watch?v=RsUD8CTDdAw&list=PLyRcl7Q37-DUM5Fx1DqYEfxfnjNvNfnPL'
path = 'C:\\Users\\Casa\\Desktop'

for url in playlist:
    musica = pytube.YouTube(url).streams.filter(only_audio=True).first()
    nome_musica = musica.title.replace('|','') # be careful with special characters in music´s name, it´s rainsing OSError [Errno 22] 
    musica.download(output_path = path, filename = nome_musica + '.mp3')

