import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import  sv_ttk

class NewsApp:

    def __init__(self):
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=687f23252b6f4eac857a1188322b2381').json()
        self.load_gui()
        self.load_news_item(0)

    def load_gui(self):
        print("Setting up GUI...")
        self.root = Tk()
        self.root.geometry('350x650')
        self.root.resizable(50, 50)
        self.root.title('APNA NEWS')
        self.root.configure(background='black')


        # Add a simple label to display something on the screen
        label = Label(self.root, text="News App", bg="black", fg="white", font=("Arial", 18))
        label.pack(pady=20)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self, index):
        #clear the screen for the new news itwm
        self.clear()

        #image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://st3.depositphotos.com/23594922/31822/v/1600/depositphotos_318221368-stock-illustration-missing-picture-page-for-website.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label =Label(self.root,image=photo)
        label.pack()


        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                        justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame=Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)
        if index!=0:
            prev = Button(frame, text='prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            next = Button(frame, text='next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)
        sv_ttk.set_theme('light')
        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

obj=NewsApp()