import tkinter
from tkinter import messagebox
app = tkinter.Tk()

def data():
    #### display input
    # v=v1.get()
    # l2.config(text=v)

    #### message (ok)
    # messagebox.showinfo("display",v1.get())

    # #### messagebox(ok,cancle)
    # messagebox.askokcancel("display",v1.get())

    #### check button
    if v_c1.get()==1:
        print("Mal selected")
    
    if v_c2.get()==1:
        print("Mal selected")


    #### radio button
    if vr1.get()==1:
        print("Male")
    
    if vr1.get()==2:
        print("female")

    
app.title("synnefo")
app.minsize(400,400)
app.maxsize(800,800)
app.config(bg="light blue")
l1=tkinter.Label(app,text="Welcome",bg="white",fg="blue")
l1.pack()
v1=tkinter.StringVar()
e1=tkinter.Entry(app,textvariable=v1)
e1.pack()
v_c1=tkinter.IntVar()
v_c2=tkinter.IntVar()
c1=tkinter.Checkbutton(app,text="mal",variable=v_c1)
c1.pack()
c2=tkinter.Checkbutton(app,text="mal",variable=v_c2)
c2.pack()

vr1=tkinter.IntVar()
r1=tkinter.Radiobutton(app,text="Male",value=1,variable=vr1)
r2=tkinter.Radiobutton(app,text="female",value=2,variable=vr1)
r1.pack()
r2.pack()



b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="green",activeforeground="red",padx=10,pady=10,command=data)
b1.pack()
l2=tkinter.Label(app)
l2.pack()
app.mainloop()