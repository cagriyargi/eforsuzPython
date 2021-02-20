import tkinter as tk
from tkinter import *
import pyperclip as pc
import sys, os 
import pyttsx3
from pyttsx3.drivers import sapi5

#coding=utf8

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

master = tk.Tk()
master.title("EFORSUZ") #başlık
photo = PhotoImage(file=resource_path("eforsuz.png"))
master.iconphoto(False,photo)
master.geometry("600x640")#program size wxh
master.configure(background="red4")
text = tk.Text(master, height=17, width=60, bd=7, highlightcolor="black", highlightbackground="black",highlightthickness=7,background="gray99")

lane1 = [ "░░", "███░", "██░░", "███░", "███░", "███░░", "███░", "███░", "███░", "░█░░", "█░█░", "███░", "░█░░", "░░█░", "█░░█░", "█░░░", "█████░", "█░░░█░", "███░", "█░█░", "███░", "░███░░", "███░░", "███░", "███░" ,"███░", "█░░█░", "█░░█░", "█░░░█░", "█░░░█░", "█░░░█░", "█░░░█░", "███░" ]
lane2 = [ "░░", "█░█░", "█░█░", "█░░░", "█░░░", "█░░█░", "█░░░", "█░░░", "█░░░", "███░", "█░█░", "░█░░", "███░", "░░█░", "█░█░░", "█░░░", "█░█░█░", "██░░█░", "█░█░", "███░", "█░█░", "█░░░█░", "█░░█░", "█░░░", "█░░░" ,"░█░░", "█░░█░", "░░░░░", "█░░░█░", "█░░░█░", "░█░█░░", "░█░█░░", "░░█░" ]
lane3 = [ "░░", "███░", "██░░", "█░░░", "█░░░", "█░░█░", "███░", "██░░", "█░█░", "█░░░", "███░", "░█░░", "░█░░", "░░█░", "██░░░", "█░░░", "█░█░█░", "█░█░█░", "█░█░", "█░█░", "███░", "█░█░█░", "███░░", "███░", "███░" ,"░█░░", "█░░█░", "█░░█░", "░█░█░░", "█░█░█░", "░░█░░░", "░░█░░░", "░█░░" ]
lane4 = [ "░░", "█░█░", "█░█░", "█░░░", "███░", "█░░█░", "█░░░", "█░░░", "█░█░", "█░█░", "█░█░", "░█░░", "░█░░", "█░█░", "█░█░░", "█░░░", "█░░░█░", "█░░██░", "█░█░", "█░█░", "█░░░", "█░░██░", "█░░█░", "░░█░", "░░█░" ,"░█░░", "█░░█░", "█░░█░", "░███░░", "█░█░█░", "░█░█░░", "░░█░░░", "█░░░" ]
lane5 = [ "░░", "█░█░", "██░░", "███░", "░█░░", "███░░", "███░", "█░░░", "███░", "███░", "█░█░", "███░", "███░", "███░", "█░░█░", "███░", "█░░░█░", "█░░░█░", "███░", "███░", "█░░░", "░██░█░", "█░░█░", "███░", "█░█░" ,"░█░░", "████░", "████░", "░░█░░░", "█████░", "█░░░█░", "░░█░░░", "███░" ]

letters =  [" ", "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z"]

label1 = Label(master, text = "Kelimeyi Giriniz, 5 Karakteri Geçmeyiniz, \nNick Satırı İçin Uygun Boşluk Sembol ile Otomatik Verilecektir",background="red4", font=("Helvetica",14,"bold"))
e1 = Entry(master, bd = 7,highlightthickness=7,highlightcolor="black", highlightbackground="black", background="gray99")

###################################################################################

lane_1 = ""
lane_2 = ""
lane_3 = ""
lane_4 = ""
lane_5 = ""

def laner(lane, index):
    if lane == 1:
        global lane_1
        word = lane_1 
        word += lane1[index]
        lane_1 = word
    if lane == 2:
        global lane_2
        word = lane_2 
        word += lane2[index]
        lane_2 = word
    if lane == 3:
        global lane_3
        word = lane_3 
        word += lane3[index]
        lane_3 = word
    if lane == 4:
        global lane_4
        word = lane_4 
        word += lane4[index]
        lane_4 = word
    if lane == 5:
        global lane_5
        word = lane_5 
        word += lane5[index]
        lane_5 = word

def printer():
    text.insert(INSERT, lane_1 + "\n")
    text.insert(INSERT, lane_2 + "\n")
    text.insert(INSERT, lane_3 + "\n")
    text.insert(INSERT, lane_4 + "\n")
    text.insert(INSERT, lane_5 + "\n")
    pc.copy("(͠≖ ͜ʖ͠≖)"+"\n"+lane_1 + "\n"+lane_2 + "\n"+lane_3 + "\n"+lane_4 + "\n"+lane_5 + "\n")

def cleaner():
    text.delete("1.0", "end")
    global lane_1
    global lane_2
    global lane_3
    global lane_4
    global lane_5
    lane_1 = ""
    lane_2 = ""
    lane_3 = ""
    lane_4 = ""
    lane_5 = ""
    e1.delete(0,'end')

def main():
    kelime = e1.get()
    word = kelime.lower()
    for lane in range(1, 6):
        for index in range(len(word)):
            for letIndex in range(len(letters)):
                if word[index] == letters[letIndex]:
                    laner(lane, letIndex)
    printer()
    
def speaker_TR():
    #1 tr 2jp 0eng
        speak = pyttsx3.init()
        speak.setProperty('rate',100)
        voices = speak.getProperty('voices')
        speak.setProperty("voice",voices[1].id)
        speak.say(e1.get())
        speak.runAndWait()

def speaker_JP():
    #1 tr 2jp 0eng
        speak = pyttsx3.init()
        speak.setProperty('rate',100)
        voices = speak.getProperty('voices')
        speak.setProperty("voice",voices[2].id)
        speak.say(e1.get())
        speak.runAndWait()
        
def speaker_ENG():
    #1 tr 2jp 3eng
        speak = pyttsx3.init()
        speak.setProperty('rate',100)
        voices = speak.getProperty('voices')
        speak.setProperty("voice",voices[0].id)
        speak.say(e1.get())
        speak.runAndWait()

###################################################################################

submit = Button(master, text = "Kelimeyi Dönüştür ve Kopyala", command = main, bd=7)
label2 = Label(master, text = "Metin Alanını Yeni Girişler İçin Temizlemeyi Unutmayın",background="red4", font=("Helvetica",14,"bold"))
submit2 = Button(master, text = "Temizle", command = cleaner, bd=7)
label3 = Label(master, text = " ",background="red4", font=("Helvetica",5,"bold"))
submit3 = Button(master, text = " Girilen Bilgiyi Türk Seslendirici ile Okutmak  ", command = speaker_TR, bd = 7)
submit4 = Button(master, text = " Girilen Bilgiyi Japon Seslendirici ile Okutmak ", command = speaker_JP, bd = 7)
submit5 = Button(master, text = "Girilen Bilgiyi İngiliz Seslendirici ile Okutmak", command = speaker_ENG, bd = 7)
label4 = Label(master, text = " ",background="red4", font=("Helvetica",5,"bold"))

label3.pack()
label1.pack()
e1.pack()
submit.pack()
label2.pack()
submit2.pack()
text.pack()
label4.pack()
submit3.pack()
submit4.pack()
submit5.pack()

master.mainloop()
