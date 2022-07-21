#!/usr/bin/env python
#-*-coding:utf-8-*-

from  Tkinter import *
import subprocess

def nmap():
    try:
        IP=etiket.get()
        yazi="nmap -sS -sV "+IP
        sonuc = subprocess.check_output(yazi, shell=True)
        label["text"] = sonuc
    except:
        print "IP den farkli birsey girildi"

pencere = Tk()
pencere.title("Nmap Syn Scan")
pencere.geometry("1024x768")


label = Label(text = "IP giriniz.....")
label.pack()

etiket = Entry(width=16)
etiket.pack()


dugme = Button(text="Lokalde syn Scan baslat!",command=nmap)
dugme.pack()

mainloop()
