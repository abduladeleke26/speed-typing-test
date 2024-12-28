from tkinter import *

time = 0
on = False
stopwatch = None

def startt():
    global time
    global stopwatch
    global on
    if on == False:
        time = 0
        on = True
        text.delete(0, 'end')
    if on == True:
        stopwatch = window.after(1000,startt)
        time += 1
        print(time)




def end():
    global time
    global stopwatch
    global on
    window.after_cancel(stopwatch)
    on = False
    min = time/60
    words = text.get()
    x = words.split()
    print(x)
    wpmm = round(len(x)/min)
    wpm["text"] = f"{wpmm} WPM"







window = Tk()
window.minsize(width=1000,height=250)


title = Label(text="SPEED WRITER", font=("Courier",50))
title.place(x=300,y=0)

instructions = Label(text="Press start to start the timer then press end to stop the timer", font=("Courier",20))
instructions.place(x=70,y=50)

start = Button(text="Start",command=startt)
start.place(x=350,y=100)

end = Button(text="End",command=end)
end.place(x=550,y=100)

text = Entry(width="100")
text.place(x=35,y=150)

wpm = Label(text="0 WPM", font=("Courier",30))
wpm.place(x=425,y=180)

window.mainloop()

