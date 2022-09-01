from gtts import gTTS
import playsound as p

audio = gTTS(text = 'um controlador do fogo secreto',lang = 'pt-br')
audio.save('./output/audio_teste.mp3')
p.playsound('./output/audio_teste.mp3')