from tkinter import *
master=Tk()
master.title('Note Taking App')
frame1=Frame(master)
frame1.grid(row=0)
frame2=Frame(master)
frame2.grid(row=2)
frame3=Frame(master)
frame3.grid(row=1)
frame4=Frame(master)
frame4.grid(row=4)
def add():
    top=Toplevel()
    top.title('Add New Notes')
    e1 = Entry(top,width=45).grid(row=0,column=0)
    b1=Label(top,text='Add Name',width=15,bg='cyan',fg='black').grid(row=0,column=1)
    b2 =Label(top, text='Add Path', width=15, bg='cyan', fg='black').grid(row=1, column=1)
    e2 = Entry(top, width=45).grid(row=1,column=0)
    lb=Label(top,text='Add Content',width=20).grid(row=2,column=0)
    e3 = Text(top, width=45).grid(row=3, column=0)
    b=Button(top,text='SAVE',width=15,height=2,bg='green',fg='orange').grid(row=4,column=0)
    c=Button(top, text='QUIT', width=15, height=2, bg='red', fg='white',command=top.destroy).grid(row=4, column=1)


button1=Button(frame1,text='Add New Notes>>',bg='red',width=25,height=2,fg='white',command=add).grid(row=0,column=0,padx=5,pady=10)
lbl=Label(frame3,text='Search Notes',height=3,width=20).grid(row=1,column=0)
v=StringVar()
e=Entry(frame2,width=45,textvariable=v).grid(row=2,column=0)
lb1=Label(master,text='-- Notes --',height=3,width=10).grid(row=3,column=0)
scrollbar = Scrollbar(frame4, width=16)
scrollbar.pack(side=RIGHT, fill=Y)

l=[1,2,3,4,5,6,77,4,3,3,2,4,5,32,2,231,12,1,1,1,1,12312,12,12]

myLis = Listbox(frame4, yscrollcommand=scrollbar.set,width=45)
myLis.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myLis.yview)

def liste():
    myLis.delete(0,END)
    for i in l:
        myLis.insert(END, str(i))
    myLis.pack(side=LEFT, fill=BOTH)

def search():
    myLis.delete(0, END)
    z=str(v.get())
    for i in l:
        if(z==str(i)):
            myLis.insert(END, str(i))
    myLis.pack(side=LEFT, fill=BOTH)


button2=Button(frame1,text='List All Notes',bg='red',width=25,height=2,fg='white',command=liste).grid(row=0,column=1,padx=5,pady=10)
button3=Button(frame2,text='Search',bg='red',width=10,height=1,fg='white',command=search).grid(row=2,column=1)

mainloop()
