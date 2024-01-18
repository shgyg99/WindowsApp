import pyautogui as auto
from PIL import ImageGrab
import time
import keyboard
from tkinter import *
import customtkinter
color_check_possition=None
click_possition1=None
color_checks_color=None
color_one=None
color_two=None
def get_color_check_possition():#مکان تشخیص رنگ
    global color_check_possition
    time.sleep(3)
    color_check_possition=auto.position()
    return color_check_possition
def get_click_possition1():#مکان کلیک در صورت دیدن رنگ اول
    global click_possition1
    time.sleep(3)
    click_possition1=auto.position()
    return click_possition1
def get_click_possition2():#مکان کلیک در صورت دیدن رنگ دوم
    global click_possition2
    time.sleep(3)
    click_possition2=auto.position()
    return click_possition2
def get_color_checks_color():#دریافت رنگ پیکسل برای چک
    global color_checks_color
    screen_shot=ImageGrab.grab()
    color_checks_color=screen_shot.getpixel(color_check_possition)
    return color_checks_color
def get_color_one():#رنگ اول
    global color_one
    time.sleep(3)
    color_p=auto.position()
    screen=ImageGrab.grab()
    color_one=screen.getpixel(color_p)
    return color_one
def get_color_two():#ر نگ دوم
    global color_two
    time.sleep(3)
    color_p=auto.position()
    screen=ImageGrab.grab()
    color_two=screen.getpixel(color_p)
    return color_two
def check_and_click():#چک کن و کلیک کن
    get_color_checks_color()
    if color_checks_color==color_one:
        auto.click(click_possition1[0],click_possition1[1])
    elif color_checks_color==color_two:
        auto.click(click_possition2[0],click_possition2[1])
def count_run():#اجرا با شمارنده
    n=int(count.get())
    for i in range(n):
        check_and_click()
        time.sleep(int(timer.get()))
        if keyboard.is_pressed('ctrl+/'):
            break
def run_timer():
    hour=int(hours.get())
    minute=int(minutes.get())
    second=int(seconds.get())
    end_time=time.time()+(hour*3600)+(minute*60)+second
    while time.time()<end_time:
        check_and_click()
        time.sleep(int(timer.get()))
        if keyboard.is_pressed('ctrl+/'):
            break
#------------------------------------------------------------
root=customtkinter.CTk()
root.title('AUTO CLICKER')
root.geometry('400x300')
root.resizable(width=False,height=False)
checkPossition=customtkinter.CTkButton(root,text='color check place',command=get_color_check_possition)
checkPossition.place(x=10,y=10)
click1Possition=customtkinter.CTkButton(root,text='click 1 place',command=get_click_possition1)
click1Possition.place(x=10,y=60)
click2Possition=customtkinter.CTkButton(root,text='click 2 place',command=get_click_possition2)
click2Possition.place(x=10,y=110)
color1=customtkinter.CTkButton(root,text='color 1',command=get_color_one)
color1.place(x=240,y=20)
color2=customtkinter.CTkButton(root,text='color 2',command=get_color_two)
color2.place(x=240,y=70)
countLabel=customtkinter.CTkLabel(root,text='how many times?')
countLabel.place(x=20,y=160)
count=customtkinter.CTkEntry(root,placeholder_text='how many')
count.place(x=10,y=160)
run=customtkinter.CTkButton(root,text='run',command=lambda:count_run())
run.place(x=10,y=220)
#------------------------------------------------------------------------------------

hours=customtkinter.CTkEntry(root,placeholder_text='hour')
hours.place(x=250,y=160)
minutes=customtkinter.CTkEntry(root,placeholder_text='minute')
minutes.place(x=250,y=200)
seconds=customtkinter.CTkEntry(root,placeholder_text='second')
seconds.place(x=250,y=240)
runTimer=customtkinter.CTkButton(root,text='run with timer',command=lambda:run_timer())
runTimer.place(x=10,y=250)

timer=customtkinter.CTkEntry(root,placeholder_text='times between')
timer.place(x=250,y=120)
root.mainloop()
customtkinter.Buton(root,text=("Hello world"),font_size=32)