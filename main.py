#https: // youtu.be/LWcaBf52Oh4
from PIL import Image
import qrcode

link = ""#add your text or link here| link veya yazı girin

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black",back_color="white")
img.save("qr.png")
img.show()
