import sys
import keyboard
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import time
import pygame
from pygame import mixer
pygame.mixer.init()

window = tk.Tk()
window.geometry("600x460")
window.title("Pomodoro app")
window.iconbitmap("tomato.ico")

tasks = []
minutes = []
tasks_dict = {}
task = ""
duration = 0
pomodoro_no = 0
step = 0
btn_state = False
welcome_image_path = PhotoImage(file ="pomodoro_timer_3s.png")
pomodoro_background_image_path = PhotoImage(file="Pomodoro_label_s0-removebg-preview.png")
SOUND_START = mixer.Sound("buzzer.wav")  
SOUND_END = mixer.Sound("ping.wav")

def set_background_image():
    # setting background color and image for Welcome Window
    window.configure(background = 'black')
    welcome_image = Label(window,image=welcome_image_path,bg="black", width=400)
    welcome_image.pack()

def remove_background_image():
    # removing background image for Display Window
    background_image3 = Label(window,image="")
    background_image3.place(relheight=1,relwidth=1)

def set_background_image_timer():
    # setting background image for Pomodoro Timer Window
    background_image3 = Label(window,image=pomodoro_background_image_path)
    background_image3.place(relheight=1,relwidth=1)


""" Display tasks & Pomodoros in table format """
def display_tasks():
    if task_entry.get() != "" and minutes_entry.get() != "":
        # adding tasks one by one (up to 5)
        task_text = task_entry.get()
        if task_1.cget("text") == "":
            task_1.configure(text=task_entry.get())
            pomodoro_no = int(int(minutes_entry.get())/25) + 1
            pomodoro_1.configure(text=pomodoro_no*"o")
            tasks.append(task_text)
            tasks_dict.update({task_text:pomodoro_no})
        elif task_2.cget("text") == "":
            task_2.configure(text=task_entry.get())
            pomodoro_no = int(int(minutes_entry.get())/25) + 1
            pomodoro_2.configure(text=pomodoro_no*"o")
            tasks.append(task_text)
            tasks_dict.update({task_text:pomodoro_no})
        elif task_3.cget("text") == "":
            task_3.configure(text=task_entry.get())
            pomodoro_no = int(int(minutes_entry.get())/25) + 1
            pomodoro_3.configure(text=pomodoro_no*"o")
            tasks.append(task_text)
            tasks_dict.update({task_text:pomodoro_no})
        elif task_4.cget("text") == "":
            task_4.configure(text=task_entry.get())
            pomodoro_no = int(int(minutes_entry.get())/25) + 1
            pomodoro_4.configure(text=pomodoro_no*"o")
            tasks.append(task_text)
            tasks_dict.update({task_text:pomodoro_no})
        elif task_5.cget("text") == "":
            task_5.configure(text=task_entry.get())
            pomodoro_no = int(int(minutes_entry.get())/25) + 1
            pomodoro_5.configure(text=pomodoro_no*"o")
            tasks.append(task_text)
            tasks_dict.update({task_text:pomodoro_no})
            tkinter.messagebox.showinfo("Tasks number info", "Tasks limit reached")       
        else:
            tkinter.messagebox.showinfo("Tasks limit reached", "You can add only 5 tasks")
        btn_state = True
        # clear entry fields (preparing for new task)
        clear_entries()
        # print(tasks)          TEST LIST
        # print(tasks_dict)     TEST DICTIONARY
    else:
        tkinter.messagebox.showinfo("No data", "You must enter task and duration")
           
""" Clear input fields for tasks and minutes on 2nd window (prepare for new entry) """
def clear_entries():
    task_entry.delete(0,END)
    minutes_entry.delete(0,END)

""" Displaying widgets on the first window """
def welcome_window():
    global greetings, btn_start
    set_background_image() 
    greetings = Label(window, text=
                    "Welcome to Pomodoro, a simple time management technique.\n\n"
                    "Boost your productivity by breaking large task(s) into 25-minute intervals called\n"
                    "“Pomodoros”, followed by short break.\n\n"
                    "Steps:\n\n"
                    "1. Enter your task(s) and duration of each task.\n"
                    "2. Start Pomodoro when ready to work\n"
                    "3. Work for 25 minutes until the timer rings.\n"
                    "4. Take a 5-minute break.\n"
                    "5. After 4 Pomodoros, take a 20-minute break.\n\n"
                    "Important: Use breaks for rest, not work, and focus only on work during Pomodoros.\n",
                    font=("Verdana",10), bg="black", fg="red", justify=tk.LEFT, width = 400)
    greetings.pack()
    btn_start = Button(window, command=destroy_widgets, text="Start", font=("Verdana",10,"bold"), bg="green", fg="white", width=12)
    btn_start.pack()
    
""" Delete all the windgets from the first window """
def destroy_widgets():
    greetings.destroy()          
    btn_start.destroy()          
    display_window()

def start_timer():
    global start_min, start_sec
    clock_lbl.configure(text = "02:00", bg = "black", fg= "white", padx = 10, pady = 10)
    window.update()
    start_min = 5  # define globaly
    start_sec = 60  # define globaly
    update_timer()

def update_timer():   #no
    for min in range(start_min,-1,-1):
        for sec in range(start_sec,-1,-1):
            time.sleep(0.1)
            displayed_text = "{:02d}:{:02d}".format(min,sec)
            print(displayed_text)
            clock_lbl.configure(text=displayed_text)
            window.update()

def update_text():
    total_pomodoros = 0
    break_no = 1
    for i in range(len(tasks)):
        for j in range(int(tasks_dict[tasks[i]])):
            text1 = ("DEEP WORK ON\n"+tasks[i]+" #"+str(j+1)+"/"+str(tasks_dict[tasks[i]]))
            if break_no % 4 != 0:
                text2 ="SHORT BREAK"
            else:
                text2 = "REST"
        txt_lbl.configure(text=text1)
        task_lbl.configure(text=text2)
        window.update()
        break_no += 1
    total_pomodoros += int(tasks_dict[tasks[i]])

welcome_window()

def exit_app():
    window.destroy()

""" 3rd window definition"""
def timer_window():
    
    window.geometry("400x400")
    set_background_image_timer()
    start_min = 24    # 
    start_min_pause_s = 5
    start_min_pause_l = 20
    start_sec = 60   # define global

    txt_lbl = Label(window, text="DEEP WORK ON", font=("Verdana",20,"bold"), fg="white", bg="#ED1D24")
    txt_lbl.place(x=80, y=120)
    task_lbl = Label(window, text="Code in place 2024", font=("Verdana",18,"bold"), fg="white", bg="#ED1D24")
    task_lbl.place(x=68, y=160)
    clock_lbl = Label(window, text=("25:00"), font=("Verdana",50,"bold"), bg="#B1161A")
    clock_lbl.place(x=88,y=208)
    stop_timer_btn = Button(window, command=exit_app, text="Exit", font=("Verdana",16,"bold"), bg="black", fg="white", width=12)
    stop_timer_btn.place(x=100,y=310)
    pygame.mixer.Sound.play(SOUND_START)    
    for min in range(start_min,-1,-1):
        for sec in range(start_sec,-1,-1):
            time.sleep(0.1)
            displayed_text = "{:02d}:{:02d}".format(min,sec)
            print(displayed_text)
            clock_lbl.configure(text=displayed_text)
            window.update()
            if min == 0 and sec == 0:
                pygame.mixer.Sound.play(SOUND_END)
                tkinter.messagebox.showinfo("Exit", "Good work! Thank you for using our app!")
                exit_app()

    total_pomodoros = 0
    break_no = 1
    for i in range(len(tasks)):
        for j in range(int(tasks_dict[tasks[i]])):
            text1 = ("DEEP WORK ON\n"+tasks[i]+" #"+str(j+1)+"/"+str(tasks_dict[tasks[i]]))
            print(text1)
            if break_no % 4 != 0:
                text2 ="SHORT BREAK"
            else:
                text2 = "REST"
            print(text2)
        txt_lbl.configure(text=text1)
        task_lbl.configure(text=text2)
        window.update()
        break_no += 1
    total_pomodoros += int(tasks_dict[tasks[i]])

    
""" 2nd window definition"""
def display_window():
 
    global task_1, task_2, task_3, task_4, task_5, task_entry, minutes_entry, pomodoro_1, pomodoro_2, pomodoro_3, pomodoro_4, pomodoro_5, clock_lbl, txt_lbl, task_lbl
    remove_background_image()

    title_lbl = Label(window, text="Welcome")
    title_lbl.place(x=10,y=10)

    task_lbl = Label(window, text="Enter your task:")
    task_lbl.place(x=10,y=10)

    task_entry = Entry(window, width = 63)
    task_entry.place(x=200,y=10)

    duration_lbl = Label(window, text="Enter minutes per task:")
    duration_lbl.place(x=10,y=40)

    #set dinamic combo entries, populate with minutes, step 15
    combo_list = []
    for i in range(15,360+15,15):
        combo_list.append(int(i))

    # display combo with predefined dinamic entries (i)
    minutes_entry = ttk.Combobox(window, values=combo_list,width=30)
    minutes_entry.place(x=200,y=40)

    append_list_btn = Button(window, command=display_tasks, text="Add task to list", font=("Verdana",9,"bold"), bg="blue", fg="white", width=20)
    append_list_btn.place(x=409,y=40)

    clear_entries()

    task_heading = Label(window, text="Tasks",font=("Verdana",11,"bold"), bg="#84AEEB", width = 39)
    task_heading.place(x=10,y=130)    

    pomodoro_heading = Label(window, text="Pomodoros",font=("Verdana",11,"bold"), bg="#84AEEB", width = 17)
    pomodoro_heading.place(x=409,y=130) 

    task_1 = Label(window, text="", font=("Verdana",10,"bold"),bg="#84EBDA", width = 43)
    task_1.place(x=10,y=160)    

    pomodoro_1 = Label(window, text="", font=("Verdana",10,"bold"), fg="red",bg="#84EBDA", width = 19)
    pomodoro_1.place(x=409,y=160) 

    task_2 = Label(window, text="", font=("Verdana",10,"bold"),bg="#84EBDA", width = 43)
    task_2.place(x=10,y=190)    

    pomodoro_2 = Label(window, text="", font=("Verdana",10,"bold"), fg="red",bg="#84EBDA", width = 19)
    pomodoro_2.place(x=409,y=190) 

    task_3 = Label(window, text="", font=("Verdana",10,"bold"),bg="#84EBDA", width = 43)
    task_3.place(x=10,y=220)    

    pomodoro_3 = Label(window, text="", font=("Verdana",10,"bold"), fg="red",bg="#84EBDA", width = 19)
    pomodoro_3.place(x=409,y=220) 

    task_4 = Label(window, text="", font=("Verdana",10,"bold"),bg="#84EBDA", width = 43)
    task_4.place(x=10,y=250)    

    pomodoro_4 = Label(window, text="", font=("Verdana",10,"bold"), fg="red",bg="#84EBDA", width = 19)
    pomodoro_4.place(x=409,y=250) 
    
    task_5 = Label(window, text="", font=("Verdana",10,"bold"),bg="#84EBDA", width = 43)
    task_5.place(x=10,y=280)    

    pomodoro_5 = Label(window, text="", font=("Verdana",10,"bold"), fg="red",bg="#84EBDA", width = 19)
    pomodoro_5.place(x=409,y=280) 

    # displayed digital countdown timer for testing purposes on 2nd window
    clock_lbl = Label(window, text=("25:00"), font=("Verdana",50,"bold"))
    #clock_lbl.pack()   # hided after successfull testing

    # TO DO: Check if tasks list is empty, and enable button if not 
    #Enable or disable the button based on the tasks list.

    _timer_btn = Button(window, command=timer_window, text="Start timer", bg="blue", fg="white", font=("Verdana",11,"bold"), width=14)
    _timer_btn.place(x=216,y=340)

    note_lbl = Label(window, text='Note: The timer was accelerated 10 times in order to check its functionality', fg="green", font=("bold"))
    note_lbl.place(x=10,y=420)

# Testing dict items
#for keys, values in tasks_dict.items():
#    print(values)

window.mainloop()