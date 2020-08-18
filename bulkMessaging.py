import pandas as pd
import tkinter.messagebox as tmsg
from tkinter import *
import smtplib

def sendMsg():
    df = pd.read_csv("msgData.csv")
    for index, item in df.iterrows():
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('shreebandal0@gmail.com','Shree@123')
        s.sendmail('shreebandal0@gmail.com',item['Email-id'],f"Subject:{window.Sub.get()}\nHey {item['Name']},\n\n{window.Msg.get()}")
        s.quit()
    tmsg.showinfo("Msg", "All Messages send successfully")

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("msg.ico")
        self.title("Send Bulk Messages")
        self.geometry("460x280")
        self.minsize(460, 280)
        self.maxsize(460, 280)

    def createOutputScreen(self):
        frame1 = Frame(self)
        Label(frame1, text="\t", font=("Arial",21)).pack(side=LEFT)
        frame1.pack()
        frame2 = Frame(self)
        Label(frame2, text="Enter Sub   -   ", font=("Arial",21)).pack(side=LEFT)
        self.Sub = Entry(frame2, font=("Arial",12))
        self.Sub.pack(side=LEFT, fill=BOTH, expand=1)
        frame2.pack()
        frame3 = Frame(self)
        Label(frame3, text="\t", font=("Arial",21)).pack(side=LEFT)
        frame3.pack()
        frame4 = Frame(self)
        Label(frame4, text="Enter Msg   -   ", font=("Arial", 21)).pack(side=LEFT)
        self.Msg = Entry(frame4, font=("Arial", 12))
        self.Msg.pack(side=LEFT, fill=BOTH, expand=1)
        frame4.pack()
        frame5 = Frame(self)
        Label(frame5, text="\t", font=("Arial", 21)).pack(side=LEFT)
        frame5.pack()
        btn = Button(self, text="Send Msg", font=("Arial",12))
        btn.pack(padx=(12, 12), pady=(12, 12))
        btn.config(command=sendMsg)

if __name__ == "__main__":
    window = GUI()
    window.createOutputScreen()
    window.mainloop()