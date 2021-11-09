from logging import root
from os import read
from pathlib import WindowsPath
from tkinter import *
import tkinter
from tkinter.ttk import *
import mysql.connector
import tkinter.messagebox as m
import smtplib
import random
from datetime import datetime
from PIL import Image, ImageTk
import requests
from tkinter import Tk
import re
import math

from requests import api
def openlogwind():
    window1=Tk()
    window1.geometry("600x600")
    window1.title("WeatherData-Login")
    window1.config(background="#B8B5FF")
    sty=Style()
    sty.configure('Btn.TButton', font =('Courier', 10, 'bold'),foreground = '#153B44',background="#29A19C")
    label1 = tkinter.Label(window1, text="Login",background="#B8B5FF", foreground="#153B44",font=("Courier",25,"bold")).place(relx = 0.5,rely = 0.14,anchor = 'center')
    label1 = tkinter.Label(window1, text="WeatherData-Easy & Accurate!",background="#B8B5FF", foreground="#153B44",font=("Courier",23,"bold")).place(relx = 0.5,rely = 0.28,anchor = 'center')
    con = mysql.connector.connect(host="localhost", user="root",passwd="A@shishcricket100", database="weatherperson") 
    cursor = con.cursor() ###DOUBTSSSSSSSSSSS
    username = Label(window1,text="Username:",foreground="#2B2B2B",background="#B8B5FF", font="Garamond 16 bold")
    username.place(x=50,y=220)
    email = Label(window1,text="Email:",foreground="#2B2B2B", background="#B8B5FF", font="Garamond 16 bold")
    email.place(x=50,y=270)
    password = Label(window1,text="Password:",foreground="#2B2B2B", background="#B8B5FF", font="Garamond 16 bold")
    password.place(x=50,y=320)
    e1 = Entry(window1,style='Ent.TEntry')
    e1.place(x=150,y=220)
    e2 = Entry(window1,style='Ent.TEntry')
    e2.place(x=150,y=270)
    e3 = Entry(window1,show="*", style='Ent.TEntry')
    e3.place(x=150,y=320)
    def checklog():
        cona=mysql.connector(host="localhost", user="root",passwd="A@shishcricket100", database="weatherperson")
        cura=cona.cursor()
        conb=mysql.connector(host="localhost", user="root",passwd="A@shishcricket100", database="weatherperson")
        curb=conb.cursor()
        cura.execute("select email from datareglog")
        curb.execute("select password from datareglog")
        em=e2.get()
        ps=e3.get()
        a1=[]
        a2=[]
        for x in cura:
            a1.append(x)
        for n in curb:
            a2.append(n)
        l=len(a1)
        q=0
        while q<l:
            if a1[q][0]==em & a2[q][0]==ps:
                m.showinfo(title="Done",message="Login Is Done")
                break
            else:
                m.showerror(title="Error",message="Please check your Login credentials.")
    login =tkinter.Button(window1,text="Login",background='#99A799',width=10,font="Courier 12 bold",command=weasearch)
    login.place(relx=0.5,rely=0.7,anchor="center")
    window1.mainloop()
def opensignwind():
    window.destroy()
    window2=Tk()
    window2.geometry("600x600")
    window2.title("WeatherData-Signup")
    window2.config(background="#FFDD93")
    sty=Style()
    sty.configure('Ent.TEntry', font =('Courier', 10, 'bold'),foreground = '#153B44',background="#29A19C")
    label2 = tkinter.Label(window2, text="Signup",background="#FFDD93", foreground="#153B44",font=("Courier",25,"bold")).place(relx = 0.5,rely = 0.14,anchor = 'center')
    label2 = tkinter.Label(window2, text="WeatherData-Easy & Accurate!",background="#FFDD93", foreground="#153B44",font=("Courier",23,"bold")).place(relx = 0.5,rely = 0.28,anchor = 'center')
    
    #MySQL CONNECTIONS LEFT!
    con = mysql.connector.connect(host="localhost", user="root",passwd="A@shishcricket100", database="weatherperson") 
    cursor = con.cursor() ###DOUBTSSSSSSSSSSS
    username = Label(window2,text="Username:",foreground="#2B2B2B",background="#FFDD93", font="Garamond 16 bold")
    username.place(x=50,y=220)
    email = Label(window2,text="Email:",foreground="#2B2B2B", background="#FFDD93", font="Garamond 16 bold")
    email.place(x=50,y=270)
    password = Label(window2,text="Password:",foreground="#2B2B2B", background="#FFDD93", font="Garamond 16 bold")
    password.place(x=50,y=320)
    confirmpassword = Label(window2,text="Confirm Password:",foreground="#2B2B2B",background="#FFDD93",  font="Garamond 16 bold")
    confirmpassword.place(x=50,y=370)
    e1 = Entry(window2,style='Ent.TEntry')
    e1.place(x=150,y=220)
    e2 = Entry(window2,style='Ent.TEntry')
    e2.place(x=150,y=270)
    e3 = Entry(window2,show="*", style='Ent.TEntry')
    e3.place(x=150,y=320)
    e4 = Entry(window2,show="*",style='Ent.TEntry')
    e4.place(x=230,y=370)
    def error():
        m.showerror(title="Error", message="Password values are not same")
    def insert():
        cursor.execute("INSERT INTO datareglog VALUES (%s, %s, %s, %s)", (e1.get(), e2.get(), e3.get(),e4.get()))
        if e3.get() == e4.get():
            con.commit()
        else:
            error()
    btnregister = tkinter.Button(window2,text="Register",background="#4E9F3D",width=10,font="Courier 12 bold",command=insert)
    btnregister.place(relx = 0.5,rely = 0.7,anchor = 'center')
    label = tkinter.Label(window2, text="Already a member?",background="#FFDD93", foreground="#153B44",font=("Courier",14,"bold")).place(relx = 0.5,rely = 0.8,anchor = 'center')
    btnlogin = tkinter.Button(window2,text="Login",background="#4E9F3D",width=7,font="Courier 12 bold",command=openlogwind)
    btnlogin.place(relx = 0.5,rely = 0.86,anchor = 'center')
    btnexit = tkinter.Button(window2,text="Exit",background="#950101",width=7,foreground="white",font="Courier 12 bold", command=window2.destroy)
    btnexit.place(relx = 0.5,rely = 0.97,anchor = 'center')
    window2.mainloop()
def weasearch():
    windoww=Tk()
    windoww.geometry("600x600")
    windoww.config(background="#2FDD92")
    windoww.title("Search City")
    sty=Style()
    sty.configure('Ent.TEntry', font =('Courier', 10, 'bold'),foreground = '#153B44',background="#29A19C")
    welcom= Label(windoww,text="Welcome, Please Enter a City in USA!",foreground="#2B2B2B",background="#2FDD92", font="Courier 16 bold").place(relx=0.5,rely=0.34,anchor="center")
    city= Label(windoww,text="City:",foreground="#2B2B2B",background="#2FDD92", font="Courier 14 bold").place(relx=0.4,rely=0.5,anchor="center")
    var9=StringVar(windoww)
    def get_cname():
        from PIL import Image, ImageTk
        cname=var9.get()
        apikey="cc98a3cda65f7305e73e8e2a492c8cb3"
        ia=",US"
        url=f"http://api.openweathermap.org/data/2.5/weather?q={cname.join(ia)}&appid={apikey}"
        response=requests.get(url).json()
        temperat=response['main']['temp']
        temperat=math.floor((temperat*1.8)-459.67)
        temp_f=response['main']['feels_like']
        temp_f=math.floor((temp_f*1.8)-459.67)
        humid=response['main']['humidity']
        wind_sp=response['wind']['speed']
        window4=tkinter.Toplevel()
        window4.geometry("600x600")
        window4.config(background="#31112C")
        window4.title(f"Weather Data for {cname}")
        c_label=Label(window4,text=f"{cname}",font="Courier 25 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.25,anchor="center")
        t_label=Label(window4,text=f"Temperature:{temperat} °F",font="Courier 21 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.35,anchor="center")
        fe_label=Label(window4,text=f"Feels Like:{temp_f} °F",font="Courier 21 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.45,anchor="center")
        h_label=Label(window4,text=f"Humidity:{humid} %",font="Courier 21 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.55,anchor="center")
        w_label=Label(window4,text=f"Wind Speed:{wind_sp} m/s",font="Courier 21 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.65,anchor="center")
        p_label=Label(window4,text="Powered By:",font="Courier 21 bold",foreground="#FFF338",background="#31112C").place(relx=0.5,rely=0.75,anchor="center")
        img1 = Image.open("OpenWeather.jpg")
        img1 = img1.resize((140,120), Image.ANTIALIAS)
        tes2 = ImageTk.PhotoImage(img1)
        lab2 = Label(window4,image=tes2)
        lab2.image = tes2
        lab2.place(relx = 0.5, rely = 0.9,anchor = 'center')
    eac=Entry(windoww,textvariable=var9).place(relx=0.6,rely=0.5,anchor="center")
    btnsub=tkinter.Button(windoww,text="Submit",background="#153B44",width=7,font="Courier 12 bold",command=get_cname).place(relx=0.5,rely=0.62,anchor="center")
    windoww.mainloop()
window=Tk()
title_pic=PhotoImage(file="Weather.png")
window.geometry("600x600")
window.title("WeatherData")
window.config(background="#91C788")
sty=Style()
sty.configure('Btn.TButton', font =('Courier', 10, 'bold'),foreground = '#153B44',background="#29A19C")
label = tkinter.Label(window, text="WeatherData",background="#91C788", foreground="#153B44",font=("Courier",25,"bold")).place(relx = 0.5,rely = 0.14,anchor = 'center')
label = tkinter.Label(window, text="WeatherData-Easy & Accurate!",background="#91C788", foreground="#153B44",font=("Courier",23,"bold")).place(relx = 0.5,rely = 0.28,anchor = 'center')
login = Button(window,text="Login",style='Btn.TButton',command=openlogwind).place(relx = 0.5,rely = 0.5,anchor = 'center')
signin = Button(window,text="SignUp",style='Btn.TButton',command=opensignwind).place(relx = 0.5,rely = 0.6,anchor = 'center')
img0 = Image.open("weather.png")
img0 = img0.resize((100,100), Image.ANTIALIAS)
tes1 = ImageTk.PhotoImage(img0)
lab1 = Label(image=tes1,background="#91C788")
lab1.image = tes1
lab1.place(relx = 0.5, rely = 0.78,anchor = 'center')
window.mainloop()