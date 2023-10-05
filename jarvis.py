
from tkinter import *

from PIL import ImageTk
import sys
import time
from tkinter import ttk
import pyttsx3
import os
import datetime as dt
import speech_recognition as sr
import webbrowser

root=Tk()
#root.configure(bg="red")
root.maxsize(width=720,height=415)
root.minsize(width=720,height=415)
root.title("JARVICE")
#root.iconbitmap("calculator.ico")
bg_image=ImageTk.PhotoImage(file='background1.png')
f_image=ImageTk.PhotoImage(file='frame.png')


#..................................jarvis functions......................
engine = pyttsx3.init()

def times():
    Time=time.strftime("%H:%M:%S")
    engine.say(Time)

def date():
    date = dt.datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    engine.say(format_date)

hour=dt.datetime.now().hour

data=[]

def Commands():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listen="Jarvis Listening...."
        ce_label.config(text=listen)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognize....")
        re=("Jarvis recognize...")
        ce1_label.config(text=re)
        query = r.recognize_google(audio, language='en-in')
        ce2_label.config(text="Sir Command is:"+query)
        del data[0:1]
        data.append(query)
        print(data)
        if "hello" in data:
            hihello()

        if "hi" in data:
            hihello()

        if "hai" in data:
            hihello()

        if "open Microsoft Office" in data:
            msoffice()


        if "close Microsoft Office" in data:
            msclose()

        if "open text file" in data:
            textfiles()
            
        if "open text file" in data:
            closetextfiles()
            
        if "open WhatsApp" in data:
            openexe()

        if "close WhatsApp" in data:
            closeexe()

        if "open Visual Studio" in data:
            editor()

        if "close Visual Studio" in data:
            closeedit()

        if "open email" in data:
            email()

        if "open company website" in data:
            google()

        if "close service" in data:
            sys.exit()
            des()
        

    except Exception as e:
        print(e)
        engine.say("please speak again")
        return  "None"
    return query
        
#................................end jarvice functions....................................
def call():
    while(1):
        #engine.say("hello am a Jarvise Assistance")
        #engine.say("The current Time is")
        #times()
        #engine.say('The Current date is')
        #date() 
        #if hour >= 6 and hour<12:
            #engine.say('good morning sir')
        engine.say("commands is running sir")
        #elif hour >= 12 and hour<18:
            #engine.say('Good Afternoon sir')
            #engine.say("commands is runnig sir")
        #elif hour >= 18 and hour<24:
            #engine.say('Good Evening sir')
            #engine.say("commands is running sir ")
        #else:
           # engine.say('good night sir')
        Commands()
        engine.runAndWait()
#...........................
def hihello():
        engine.say('hello sir')
        engine.say('i am your assitant ')
        # engine.say('a two it')
        engine.say("How can i help you") 
       
def editor():
    my_programe="C:/Users/hmish/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    os.system('"%s"' % my_programe)

def closeedit():
    #my_programe=filedialog.askopenfilename()
    my_programe="C:/Users/hmish/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    #text_l.config(text=my_programe)
    #x=os.system(my_programe)
    os.system('"%s"' % +'TASKKILL /F /IM Code.exe')
    
#......................................open and close................
def openexe():
    my_programe="C:/Users/hmish/Downloads/WhatsApp.exe"
    os.system(my_programe)

def closeexe():
    my_programe="C:/Users/hmish/Downloads/WhatsApp.exe"
    os.system('TASKKILL /F /IM WhatsApp.exe')


new = 1
url = "https://mail.google.com"
def email():
    webbrowser.open(url,new=new)

new2 = 1
url2 = "https://www.google.com/"
def google():
    webbrowser.open(url2,new=new2)

def des():
     root.destroy()
     
def textfiles():
    my_programe="file.txt"
    os.system(my_programe)

def closetextfiles():
    my_programe="file.txt"
    os.system('TASKKILL /F /IM file.txt')

    
def msoffice():
    programe=("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Word 2010.lnk")
    os.system('"%s"' % programe)

def msclose():
    os.system('TASKKILL /F /IM Microsoft-Word-2010.lnk')
    



#......................................open close programe..............

#..................................jarvis function end...................



background_image=Label(root,image=bg_image,bd=0).place(x=0,y=0,relwidth=1,relheight=1)

btn_enter=Button(root,text="Enter",font=("times new roman",16),command=call,border="5",bg="black",activebackground='white',fg="white",activeforeground='black',cursor='hand2')
btn_enter.place(x=290,y=370,width=130,height=40)

#......................................... Clock .........................
def clock():
    G_time=time.strftime("%H:%M:%S")
    c_label.config(text=G_time)
    c_label.after(1000,clock)
    
    
clock_frame=Frame(root,relief=RIDGE,bg="black")
clock_frame.place(x=280,y=15,width=140,height=40)

c_label=Label(clock_frame,bd=0,font=("arial",25,"italic"),fg="white",bg="black")
c_label.place(x=0,y=0)
clock()


#........................................ Clock End...................

w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 25))
w.place(x=210,y=305,width=280,height=40)

#.......................center frame.................................
center_frame=Frame(root,relief=RIDGE,bg="white",bd=10)
center_frame.place(x=200,y=60,width=305,height=235)

fr_image=Label(center_frame,image=f_image,bd=0).place(x=0,y=0,relwidth=1,relheight=1)

ce_label=Label(center_frame,text=data,font=("arial",12,"italic"),fg="black",bg="white")
ce_label.place(x=10,y=10)

ce1_label=Label(center_frame,text="",font=("arial",12,"italic"),fg="black",bg="white")
ce1_label.place(x=30,y=30)

ce2_label=Label(center_frame,text="",font=("arial",12,"italic"),fg="black",bg="white")
ce2_label.place(x=50,y=50)

#.........................progress bar...................
my_progress =ttk.Progressbar(center_frame,orient=HORIZONTAL,mode="indeterminate")
my_progress.place(x=15,y=170,width=250)

def progress():
    my_progress["value"]=40
    my_progress.start(10)
progress()

#...........................second progress bar
root_progress =ttk.Progressbar(root,orient=VERTICAL,mode="indeterminate")
root_progress.place(x=100,y=70,width=25,height=200)

def progress1():
    root_progress["value"]=40
    root_progress.start(10)
progress1()

#...........................third progress bar................

root1_progress =ttk.Progressbar(root,orient=VERTICAL,mode="indeterminate")
root1_progress.place(x=570,y=70,width=25,height=200)

def progress2():
    root1_progress["value"]=40
    root1_progress.start(10)
progress2()



root.mainloop()


   


    


  

