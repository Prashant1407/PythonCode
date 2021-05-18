from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YT Download")
root.iconbitmap("C:/Users/Prash/OneDrive/Documents/Python/Image_Used/USE_IMAGE.ico")

background_image= PhotoImage(file='Youtube-Splash.png')
background_label = Label(root, image = background_image)
background_label.place(relwidth =1, relheight =1)


Label(root,text = "YT Video Downloader", bg = "red", font = 'arial 15 bold').pack()
link=StringVar()


#Code to make this app open full screen
#root.attributes('-fullscreen', True)
#root.bind("<Escape>", lambda e: root.destroy())



Label(root, text='Paste Link Here:', bg ="red",font = 'arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width = 70, textvariable = link).place(x=32,y=90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x=180, y=210)


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', relief = "raised", padx = 10, command = Downloader).place(x=130 ,y = 150)

exit_button = Button(root, text="EXIT", font = 'arial 15 bold' ,bg = 'pale violet red', relief = "raised", padx = 10, command=root.destroy)
exit_button.place(x=290, y=150)

root.mainloop()
