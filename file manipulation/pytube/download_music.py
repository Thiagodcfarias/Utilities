import pytube

url = 'https://www.youtube.com/watch?v=0JJvSNWfpBc'
path = 'C:\\Users\\Casa\\Desktop'

musica = pytube.YouTube(url).streams.filter(only_audio=True).first()
nome_musica = musica.title

# be careful with special characters in music´s name, it´s rainsing OSError [Errno 22] 
for special_char in ['|',':']:
    nome_musica = nome_musica.replace(special_char,'') 
    
musica.download(output_path = path, filename = nome_musica + '.mp3')
