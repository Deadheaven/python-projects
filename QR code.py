import pyqrcode
img = pyqrcode.create("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
img.png("QR code.jpg")