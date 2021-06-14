from tkinter import *
wd=Tk()
wd.resizable(FALSE,FALSE)
wd.geometry("412x262")
#wd.resizable(FALSE,FALSE)
wd.configure(bg="black")
wd.attributes("-alpha",1.0)


wd.title("Simple Calculator")
e=Entry(wd,width=64,borderwidth=7)
e.grid(row=0,column=0,columnspan=5,ipady=7)
e.bind("<Key>", lambda e: "break")  

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_delete():
    e.delete(len(e.get())-1)

def button_equal():
    try:
        total=str(eval(e.get()))
        e.delete(0,END)
        e.insert(0,total)
    except:
        e.delete(0,END)
        e.insert(0,"Math error")


b1=Button(text="7",bg="red",padx=42,pady=10,command=lambda:button_click(7))
b2=Button(text="8",bg="red",padx=43.5,pady=10,command=lambda:button_click(8))
b3=Button(text="9",bg="red",padx=45,pady=10,command=lambda:button_click(9))

b4=Button(text="4",bg="red",padx=42,pady=10,command=lambda:button_click(4))
b5=Button(text="5",bg="red",padx=43.5,pady=10,command=lambda:button_click(5))
b6=Button(text="6",bg="red",padx=45,pady=10,command=lambda:button_click(6))

b7=Button(text="1",bg="red",padx=42,pady=10,command=lambda:button_click(1))
b8=Button(text="2",bg="red",padx=43.5,pady=10,command=lambda:button_click(2))
b9=Button(text="3",bg="red",padx=45,pady=10,command=lambda:button_click(3))

bdiv=Button(text="/",bg="#ff9933",padx=45.5,pady=10,command=lambda:button_click("/"))
bmul=Button(text="*",bg="#ff9933",padx=45.5,pady=10,command=lambda:button_click("*"))
bsub=Button(text="-",bg="#ff9933",padx=45.5,pady=10,command=lambda:button_click("-"))
badd=Button(text="+",bg="#ff9933",padx=43.5,pady=10,command=lambda:button_click("+"))

b0=Button(text="0",bg="red",padx=42,pady=10,command=lambda:button_click(0))
bpnt=Button(text=".",bg="#e60000",padx=45.4,pady=10,command=lambda:button_click("."))
beq=Button(text="=",bg="#2eb82e",padx=44,pady=10,command=button_equal)

bclear=Button(text="clear",bg="#cc9900",padx=84,pady=10,command=button_clear)
bdelete=Button(text="delete",bg="#cc9900",padx=85,pady=10,command=button_delete)

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

bdiv.grid(row=1,column=3)
bmul.grid(row=2,column=3)
bsub.grid(row=3,column=3)

badd.grid(row=4,column=3)
b0.grid(row=4,column=0)
bpnt.grid(row=4,column=1)
beq.grid(row=4,column=2)

bclear.grid(row=5,column=0,columnspan=2)
bdelete.grid(row=5,column=2,columnspan=2)

wd.mainloop()