#by Lakshya 508 words 5,332 characters 247 lines (Last Update: 20 May 2021 At 14:01)
from tkinter import *

root=Tk()
root.configure(bg="black")
root.geometry("300x435")
root.minsize(300,435)
root.maxsize(300,435)

root.title("Calculater by Lakshya")
root.wm_iconbitmap("F:\Coding\python\Run-WorkShop\Completed-Projects\Calculator\Calculator.ico")

a=StringVar()
a.set("")


def f0():
    a.set(a.get() + "0")
    root.update()
def f1():
    a.set(a.get() + "1")
    root.update()
def f2():
    a.set(a.get() + "2")
    root.update()
def f3():
    a.set(a.get() + "3")
    root.update()
def f4():
    a.set(a.get() + "4")
    root.update()
def f5():
    a.set(a.get() + "5")
    root.update()
def f6():
    a.set(a.get() + "6")
    root.update()
def f7():
    a.set(a.get() + "7")
    root.update()
def f8():
    a.set(a.get() + "8")
    root.update()
def f9():
    a.set(a.get() + "9")
    root.update()

def f11():
    a.set(a.get() + "/")
    root.update()   
def f22():
    a.set(a.get() + "*")
    root.update()
def f33():
    a.set(a.get() + "-")
    root.update()
def f44():
    a.set(a.get() + "00")
    root.update()
def f55():
    a.set(a.get() + ".")
    root.update()
def f66():
    a.set(a.get() + "+")
    root.update()
def f77():
    try:
        a.set(eval(a.get()))
        root.update()
    except:
        a.set("Error")
        root.update()
def f88():
    a.set("")
    root.update()
def f99():
    s=a.get()
    s=s[:-1]
    a.set(s)
    root.update()


t=Label(root,textvariable=a,font=',30000,bold',anchor="w",bd=5,relief=RAISED)
t.pack(pady=10,fill=X,padx=10,ipadx=10)


F1=Frame(root,bg="black")
b7=Button(F1,text="7",font="pattaya,100,bold",command=f7,padx=15,pady=10,bg="grey",fg="white",bd=5)
b7.pack(side="left",padx=6,pady=5)

b8=Button(F1,text="8",font="pattaya,100,bold",command=f8,padx=15,pady=10,bg="grey",fg="white",bd=5)
b8.pack(side="left",padx=6,pady=5)

b9=Button(F1,text="9",font="pattaya,100,bold",command=f9,padx=15,pady=10,bg="grey",fg="white",bd=5)
b9.pack(side="left",padx=6,pady=5)

b11=Button(F1,text="/",font="pattaya,100,bold",command=f11,padx=15,pady=10,fg="red",bd=5)
b11.pack(side="left",padx=6,pady=5)

F1.pack()


F2=Frame(root,bg="black")
b4=Button(F2,text="4",font=",15,bold",command=f4,padx=15,pady=10,bg="grey",fg="white",bd=5)
b4.pack(side="left",padx=6,pady=5)

b5=Button(F2,text="5",font=",15,bold",command=f5,padx=15,pady=10,bg="grey",fg="white",bd=5)
b5.pack(side="left",padx=6,pady=5)

b6=Button(F2,text="6",font=",15,bold",command=f6,padx=15,pady=10,bg="grey",fg="white",bd=5)
b6.pack(side="left",padx=6,pady=5)

b22=Button(F2,text="x",font=",15,bold",command=f22,padx=15,pady=10,fg="red",bd=5)
b22.pack(side="left",padx=6,pady=5)

F2.pack()


F3=Frame(root,bg="black")
b1=Button(F3,text="1",font=",15,bold",command=f1,padx=15,pady=10,bg="grey",fg="white",bd=5)
b1.pack(side="left",padx=6,pady=5)

b2=Button(F3,text="2",font=",15,bold",command=f2,padx=15,pady=10,bg="grey",fg="white",bd=5)
b2.pack(side="left",padx=6,pady=5)

b3=Button(F3,text="3",font=",15,bold",command=f3,padx=15,pady=10,bg="grey",fg="white",bd=5)
b3.pack(side="left",padx=6,pady=5)

b33=Button(F3,text="-",font=",15,bold",command=f33,padx=15,pady=10,fg="red",bd=5)
b33.pack(side="left",padx=6,pady=5)

F3.pack()



F4=Frame(root,bg="black")
b0=Button(F4,text="0",font=",15,bold",command=f0,padx=15,pady=10,bg="grey",fg="white",bd=5)
b0.pack(side="left",padx=6,pady=5)

b44=Button(F4,text="00",font=",15,bold",command=f44,padx=10,pady=10,fg="red",bd=5)
b44.pack(side="left",padx=8,pady=5)

b55=Button(F4,text=".",font=",15,bold",command=f55,padx=15,pady=10,fg="red",bd=5)
b55.pack(side="left",padx=6,pady=5)

b66=Button(F4,text="+",font=",15,bold",command=f66,padx=13,pady=10,fg="red",bd=5)
b66.pack(side="left",padx=10,pady=5)

F4.pack()


F5=Frame(root,bg="black")

b77=Button(F5,text="=",font=",15,bold",command=f77,padx=15,pady=10,fg="red",bd=5)
b77.pack(side="left",padx=6,pady=5)

b88=Button(F5,text="AC",font=",15,bold",command=f88,padx=45,pady=12,fg="black",bg="red",bd=5)
b88.pack(side="left",padx=6,pady=5)

b99=Button(F5,text="C",font=",15,bold",command=f99,padx=15,pady=10,fg="red",bd=5)
b99.pack(side="left",padx=6,pady=5)

F5.pack()




def bi0(e):
    a.set(a.get() + "0")
    root.update()
def bi1(e):
    a.set(a.get() + "1")
    root.update()
def bi2(e):
    a.set(a.get() + "2")
    root.update()
def bi3(e):
    a.set(a.get() + "3")
    root.update()
def bi4(e):
    a.set(a.get() + "4")
    root.update()
def bi5(e):
    a.set(a.get() + "5")
    root.update()
def bi6(e):
    a.set(a.get() + "6")
    root.update()
def bi7(e):
    a.set(a.get() + "7")
    root.update()
def bi8(e):
    a.set(a.get() + "8")
    root.update()
def bi9(e):
    a.set(a.get() + "9")
    root.update()

def bi11(e):
    a.set(a.get() + "/")
    root.update()   
def bi22(e):
    a.set(a.get() + "*")
    root.update()
def bi33(e):
    a.set(a.get() + "-")
    root.update()
def bi44(e):
    a.set(a.get() + ".")
    root.update()
def bi55(e):
    a.set(a.get() + "+")
    root.update()
def bi66(e):
    try:
        a.set(eval(a.get()))
        root.update()
    except:
        a.set("Error")
        root.update()
def bi77(e):
    s=a.get()
    s=s[:-1]
    a.set(s)
    root.update()



root.bind("0",bi0)
root.bind("1",bi1)
root.bind("2",bi2)
root.bind("3",bi3)
root.bind("4",bi4)
root.bind("5",bi5)
root.bind("6",bi6)
root.bind("7",bi7)
root.bind("8",bi8)
root.bind("9",bi9)

root.bind("/",bi11)
root.bind("*",bi22)
root.bind("-",bi33)
root.bind(".",bi44)
root.bind("+",bi55)
root.bind("<Return>",bi66)
root.bind("<BackSpace>",bi77)

root.mainloop()