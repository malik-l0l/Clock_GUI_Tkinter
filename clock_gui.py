from tkinter import *
from time import *


def update():
    time_string = strftime('%H:%M:%S %p')  # give time to variable
    time_label.config(text=time_string)  # and put it in the label

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d %y')
    date_label.config(text=date_string)

    # time_label.after(1000, update)  # (delay,function)
    # since date,time,day are inside the window we can update window instead
    window.after(1000, update)


window = Tk()
window.title("Clock")
window.config(bg='black')
# we make 3 labels for - time,date,weak
time_label = Label(window, font=('Arial', 50), fg='#00FF00', bg='black')
time_label.pack()

day_label = Label(window, font=('Ink free', 30), fg='red', bg='black')
day_label.pack()

date_label = Label(window, font=('Ink free', 30), fg='red', bg='black')
date_label.pack()

update()

window.mainloop()
