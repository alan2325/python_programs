import tkinter

app=tkinter.Tk()
c=tkinter.Canvas(app,width=500,height=500,bg="light blue")
c.create_line(50,50,350,50)
c.create_rectangle(100,100,400,400,fill="black")
c.create_oval(100,100,400,400,fill="green")
c.create_polygon(200,100,100,100,100,100,fill="yellow")
c.pack()
app.mainloop()