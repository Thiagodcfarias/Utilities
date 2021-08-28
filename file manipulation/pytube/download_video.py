import pytube as p

# edit this variables
url = 'https://www.youtube.com/watch?v=xd7Lg2CtvTM'
path = 'C:\\Users\\samsung\\Desktop'
nome_arquivo = 'teste'

youtube = p.YouTube(url)

video = youtube.streams.get_highest_resolution()
video.download(output_path = path, filename = nome_arquivo + '.mp4')

