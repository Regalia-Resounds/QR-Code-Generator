import qrcode
from tkinter import *

#TODO
# 1. fix broken GUI
# 2. Add name argument using Path
# 3. re-export the exe
# 4. Document Function
# 5. Reorganize Codes
# 6. Readme.md (Simple)

#Function
def Generate():
   qr = qrcode.QRCode(box_size=20,
                      border=2)
   qr.add_data(link.get())
   qr.make(fit=True)
   img = qr.make_image()
   img.save("qr.png")

#Window
window = Tk()
window.title("QR Code Generator")
window.geometry("480x120")

# frame for the label and entry box
frame = Frame(window)
frame.pack(side="left")

#Entry
im_namelbl = Label(frame,
           text="Insert Name")
im_name = Entry(window,
                width="50")
linklbl = Label(frame,
                text="Insert Link")
link = Entry(window,
             width="50")

im_namelbl.pack(side="left")
im_name.pack()
linklbl.pack(side="left")
link.pack()

#Button
Generate = Button(window,
                  text="Generate",
                  command=Generate)
Generate.pack()

#Mainloop
window.mainloop()