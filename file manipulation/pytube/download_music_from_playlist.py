import pytube as p

# edit this variables
url = 'https://www.youtube.com/watch?v=RsUD8CTDdAw&list=PLyRcl7Q37-DUM5Fx1DqYEfxfnjNvNfnPL'
path = 'C:\\Users\\Casa\\Desktop'

for url in playlist:
    musica = pytube.YouTube(url).streams.filter(only_audio=True).first()
    
    # be careful with special characters in music´s name, it´s rainsing OSError [Errno 22] 
    nome_musica = musica.title
    for special_char in ['|',':']:
        nome_musica = nome_musica.replace(special_char,'') 
        
    musica.download(output_path = path, filename = nome_musica + '.mp3')

