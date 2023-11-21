from tkinter import font
import pyttsx3


def main4():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)#Speed of Reading
    engine.setProperty('volume',1.0) #o to 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)#Two Voice 0 and 1
    engine.say(a1.get("1.0",END))
    engine.runAndWait()
    engine.stop()



from tkinter import *
r1=Tk()
r1.geometry("600x400")
label_font = font.Font(weight="bold",family='Helvetica',size=30)
l1=Label(r1,text="Speech Recognition",font=label_font, bg='#0052cc', fg='#ffffff')
l1.place(anchor="center",relx=0.5,rely=0.1)



a1 = Text(r1,height=2, width=30)
a1.place(relx=0.1,rely=0.5)

label_font = font.Font(weight="bold",family='Times New Roman',size=10)
b=Button(r1,text="Text to Speak",command=lambda:main4(),font=label_font)
b.place(relx=0.7,rely=0.5)



r1.mainloop()
