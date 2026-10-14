import qrcode
from pathlib import Path

#TODO
# 1. Color of image as optional argument
# 2. Shebang

def Generate(im_name: str, data: str): # variable_name: type, ...

   qr = qrcode.QRCode(box_size=20,
                      border=2)
   qr.add_data(data)
   qr.make(fit=True)
   img = qr.make_image(fill_color="black", back_color="white")

   path = Path(im_name).with_suffix(".png")
   img.save(path)
   return path