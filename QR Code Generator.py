import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)
Link = input("Enter the link : \n")
qr.add_data(Link)
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
Name = input("Enter a name to save: \n")
img.save(Name)
