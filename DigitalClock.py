from tkinter import*
from tkinter .ttk import*
from time import strftime

top=Tk()
top.title("DIGITAL CLOCK")
def clock():
      text=strftime("%H %M %S %p")
      lbl.config(text=text)
      lbl.after(1000,clock)
lbl=Label(top,font=("digital-7",50,"bold"),
          background="lightblue",foreground="Blue")

lbl.pack(anchor="center")
clock()
mainloop()
