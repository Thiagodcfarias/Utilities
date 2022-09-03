import pyqrcode as p
import png

url = 'www.youtube.com'
qrcode_ = p.create(url)
qrcode_.png('result.png',scale = 6)