from tkinter import *
from tkinter import messagebox
import os


root = Tk()
root.geometry("740x420")
root.resizable(FALSE,FALSE)
root.title('DownTorn-Tube')
icon = PhotoImage(file='images\icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
arkaplan = PhotoImage(file="images/background.png")
background_label = Label(root, image=arkaplan)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = arkaplan

indir_resim = PhotoImage(file="images/Download-icon.png")
#####################
tekrar = 0
dosya_olusturma = 0

path = os.path.expanduser('~')
path = path+"\Documents"
istikamet = path + "\DownTorn-Tube"

try:
    os.mkdir(istikamet)
except:
    print("Varolan bir dosya oluşturulamaz")

def cik(event=None):
    sys.exit()

def url():
    global path
    from pytube import YouTube
    link = video_url.get()
    yt = YouTube(str(link))
    videos = yt.streams.all()
    secim = kalite_select.get()
    perde.destroy()

    count = 1
    fark = 0
    if (count >= 1):
        for v in videos:
            if (count < 21):
                text = str(count) + ".  Akış etiketi  :" + str(v)
                text = text.replace('<Stream: itag="', "")
                text = text.replace('"', "")
                text = text.replace("=", "  : ")
                text = text.replace("res", "    Kalite")
                text = text.replace("fps", "    FPS")
                text = text.replace("    FPS vcodec  : ", "          ")
                text = text.replace("mime_type", "    Tür")
                text = text.replace("None", "Yok")
                text = text.replace("vp9>", "")
                text = text.replace("avc1.4", "")
                text = text.replace("d40", "")
                text = text.replace(">", "")
                text = text.replace("abr", "    Ses kalitesi")
                text = text.replace("acodec", "    Kodek")
                cikti = Label(text=text, font="Arial 8", bg="black", fg="#679CFF")
                cikti.pack()
                cikti.place(x=0, y=fark)
                count += 1
                fark += 15

    global tekrar
    try:
        tekrar += 1
        secim_ham = int(secim)
        video = videos[secim_ham - 1]
        destination = str(istikamet)
        video.download(destination)

    except ModuleNotFoundError:
        print("Modül Bulunamadı")

    except ValueError:
        print("Miktar hatası")
        tekrar += 1
        pass

    if tekrar == 3:
        mesaj = "Linkini verdiğiniz youtube videosu   " + istikamet + " konumuna indi"
        print("\n" + mesaj)
        messagebox.showinfo("Videonuz İndi", mesaj)

video_text = Label(text="Video linkini giriniz",bg="black",fg="#ff8900",font="Verdana 12")
video_text.pack()
video_text.place(x=15,y=330)

video_url = Entry()
video_url.pack()
video_url.place(x=30,y=370)

getir = Button(text="               Getir              ",command=url,bg="green",fg="white")
getir.pack()
getir.place(x=31,y=390)

kalite_yazi = Label(text="Hangi kaliteyi istiyorsunuz. \n Üsteki tabloya bakınız. Örn* 5",bg="black",fg="#ff8900",font="Georgia 10")
kalite_yazi.pack()
kalite_yazi.place(x=200,y=330)

kalite_secim = Entry()
kalite_secim.pack()
kalite_secim.place(x=230,y=368)

perde = Label(text="                                                                  \n                                                                   \n                                                                   \n",bg="black")
perde.pack()
perde.place(x=200,y=330)

video_indir = Button(root,command=url,bg="black",image=indir_resim)
video_indir.pack()
video_indir.place(x=660,y=341)

yatay_dowloand_cerceve =  Label(text="                                   ",bg="black",fg="black")
yatay_dowloand_cerceve.pack()
yatay_dowloand_cerceve.place(x=650,y=329)
dikey_dowloand_cerceve = Label(text="\n|\n|\n|\n|\n|\n",bg="black",fg="black")
dikey_dowloand_cerceve.pack()
dikey_dowloand_cerceve.place(x=655,y=329)

root.bind("<Escape>",cik)

root.mainloop()
