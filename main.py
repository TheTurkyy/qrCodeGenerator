import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image


def generate_qr():
    url = url_entry.get()

    if not url: 
        messagebox.showerror("Input Error", "Please enter a URL.")
        return

    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  
        border=4,  
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img.save("generated_qr_code.png")

    img_tk = ImageTk.PhotoImage(img)

    
    img_label.config(image=img_tk)
    img_label.image = img_tk  

    messagebox.showinfo("Done!", "Your QR Code was generated")


root = tk.Tk()
root.title("QR-Code Generator")

root.geometry("400x400")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)
url_entry.insert(0, "Enter an URL") 

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

img_label = tk.Label(root)
img_label.pack(pady=10)

root.mainloop()
