import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Encode
data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

img = qrcode.make(data)

img.save("G:/STUDY/myqrcode.png")

# Modified version of QR code

# qr = qrcode.QRCode(version=1, box_size=5, border=6)
# qr.add_data(data)
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="green", back_color="white")
#
# img.save("G:/STUDY/myqrcode2.png")

# Decode

img = Image.open("G:/STUDY/myqrcode.png")

result = decode(img)

print(result)