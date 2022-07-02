from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image
root = Tk()
root.geometry("1000x1000")
root.minsize(500, 500)
root.maxsize(1000,1000)
root.title("YOUTUBE VIDEO DOWNLOADER")
root.config(bg="#423F3A")

head = Label(text="Youtube Video Downloader", bg="#FF0000", pady=10, padx=10, font="Helvetica 30 bold").pack(fill=X)
photo = ImageTk.PhotoImage(Image.open("download-removebg-preview.png"))
display = Label(image=photo).pack()
f1 = Frame(bg="#423F3A", borderwidth=20)
f1.pack(fill=X)
Label(f1, bg="#423F3A" ,text="Download any Youtube video with url", padx=20, pady=20,font="Helvetica 15 bold" ).pack()

f2 = Frame(bg="#423F3A")
f2.pack(fill=X)
Label(f2, bg="#423F3A", text="Paste the Link Below", font="Helvetica 15 bold").pack()

f3 = Frame(bg="#423F3A", pady=10, padx=10)
f3.pack(fill=X)

link = StringVar()
paste = Entry(f3, textvariable=link).pack()
def fun():
    url = link.get()
    YouTube(url).streams.get_highest_resolution().download()
    print("Downloaded Successfully")
Button(f3, text="DOWNLOAD", command=fun).pack(padx=10, pady=10)





root.mainloop()