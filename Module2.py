from tkinter import *
import sqlite3
conn=sqlite3.connect('Note.db')
#conn.execute("drop table Note")
#conn.execute("CREATE TABLE Note(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,CONTENT TEXT NOT NULL,PRIORITY NOT NULL);")
conn.commit()
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
frame5=Frame(master)
frame5.grid(row=4,column=2)

p = StringVar()

prio=IntVar()

def add():
    top=Toplevel()
    top.title('Add New Notes')
    fr=Frame(top)
    fr.grid(row=3,column=0)
    e1 = Entry(top,width=45,textvariable=p)
    e1.grid(row=0,column=0)
    b1=Label(top,text='Add Name',width=15,bg='cyan',fg='black')
    b1.grid(row=0,column=1)
    b2 =Label(top, text='Add PRIORITY', width=15, bg='cyan', fg='black')
    b2.grid(row=1, column=1)

    e2 = Entry(top, width=45,textvariable=prio)
    e2.grid(row=1,column=0)
    lb=Label(top,text='Add Content',width=20)
    lb.grid(row=2,column=0)

    scrollb = Scrollbar(fr, width=16)
    scrollb.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=myLis.yview)


    e3 = Text(fr, width=45,yscrollcommand=scrollb.set)
    e3.pack(side=LEFT,fill=BOTH)



    c=Button(top, text='QUIT', width=15, height=2, bg='red', fg='white',command=top.destroy)
    c.grid(row=4, column=1)
    def save():
        x=str(p.get())
        m=prio.get()

        input = str(e3.get("1.0",END))
        conn.execute("INSERT INTO Note(NAME,CONTENT,PRIORITY)VALUES(?,?,?)",(x,input,m))
        conn.commit()
    br = Button(top, text='SAVE', width=15, height=2, bg='green', fg='orange',command=save).grid(row=4, column=0)


button1=Button(frame1,text='Add New Notes>>',bg='red',width=25,height=2,fg='white',command=add).grid(row=0,column=0,padx=5,pady=10)
lbl=Label(frame3,text='Search Notes',height=3,width=20).grid(row=1,column=0)
v=StringVar()
e=Entry(frame2,width=45,textvariable=v).grid(row=2,column=0)
lb1=Label(master,text='-- Notes --',height=3,width=10).grid(row=3,column=0)
scrollbar = Scrollbar(frame4, width=16)
scrollbar.pack(side=RIGHT, fill=Y)



myLis = Listbox(frame4, yscrollcommand=scrollbar.set,width=45)
myLis.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myLis.yview)

def liste():
    myLis.delete(0,END)
    cursor=conn.execute("SELECT ID,NAME from Note")
    for row in cursor:
        myLis.insert(END,str(row))
    myLis.pack(side=LEFT, fill=BOTH)

    butt()



def search():
    myLis.delete(0, END)
    z=str(v.get())
    cursor = conn.execute("SELECT ID,NAME from Note where NAME=?",(z,))
    for row in cursor:
        print(row)
        myLis.insert(END, str(row))
    myLis.pack(side=LEFT, fill=BOTH)
    butt()

def dele():
    del_id = myLis.get(myLis.curselection())
    l = list(del_id.split(","))
    del_id = l[0][1:]
    conn.execute("DELETE FROM Note where ID=?", (del_id,))
    conn.commit()
    liste()
#    myLis.delete(0, END)

def Up():
    del_id = myLis.get(myLis.curselection())
    top = Toplevel()
    top.title('Update Notes')
    fr = Frame(top)
    fr.grid(row=3, column=0)

    l = list(del_id.split(","))
    del_id=l[0][1:]

    vr=StringVar()
    vrr = StringVar()
    l=conn.execute("SELECT NAME,PRIORITY,CONTENT FROM Note where ID=?", (del_id,))
    for row in l:
        x=row[0]
        y=row[1]
        z=row[2]

    e1 = Entry(top, width=45, textvariable=vr)
    vr.set(x)
    e1.grid(row=0, column=0)
    b1 = Label(top, text='Name', width=15, bg='cyan', fg='black')
    b1.grid(row=0, column=1)
    b2 = Label(top, text='PRIORITY', width=15, bg='cyan', fg='black')
    b2.grid(row=1, column=1)

    e2 = Entry(top, width=45,textvariable=vrr)
    e2.grid(row=1, column=0)
    vrr.set(y)
    lb = Label(top, text='Content', width=20)
    lb.grid(row=2, column=0)

    scrollb = Scrollbar(fr, width=16)
    scrollb.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=myLis.yview)

    e3 = Text(fr, width=45, yscrollcommand=scrollb.set)
    e3.pack(side=LEFT, fill=BOTH)

    e3.insert(INSERT,z)
    c = Button(top, text='QUIT', width=15, height=2, bg='red', fg='white', command=top.destroy)
    c.grid(row=4, column=1)

    def save():
        x = str(vr.get())
        m = vrr.get()

        input = str(e3.get("1.0", END))
        conn.execute("INSERT INTO Note(NAME,CONTENT,PRIORITY)VALUES(?,?,?)", (x, input, m))
        conn.commit()
        top.destroy()

        liste()


    br = Button(top, text='SAVE', width=15, height=2, bg='green', fg='orange', command=save).grid(row=4, column=0)
    conn.execute("DELETE FROM Note where ID=?", (del_id,))
    conn.commit()



def redd():
    del_id = myLis.get(myLis.curselection())
    l = list(del_id.split(","))
    del_id=l[0][1:]
    print(l)
    l=conn.execute("SELECT NAME,PRIORITY,CONTENT FROM Note where ID=?", (del_id,))
    for row in l:
        z=row[2]

    top = Toplevel()
    fr = Frame(top)
    fr.grid(row=1, column=0)

    top.title('Read Notes')
    lb = Label(top, text='Content', width=20)
    lb.grid(row=0, column=0)

    scrollb = Scrollbar(fr, width=16)
    scrollb.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=myLis.yview)

    e3 = Text(fr, width=45, yscrollcommand=scrollb.set)
    e3.pack(side=LEFT, fill=BOTH)

    e3.insert(INSERT,z)
    c = Button(top, text='QUIT', width=15, height=2, bg='red', fg='white', command=top.destroy)
    c.grid(row=4, column=0)


def butt():
    b = Button(frame5, text='Update', bg='blue', fg='orange', command=Up).grid(row=4,column=2)

    c = Button(frame5, text='Delete', bg='blue', fg='orange', command=dele).grid(row=5,column=2)

    d = Button(frame5, text='Read', bg='blue', fg='orange', command=redd).grid(row=6,column=2)

button2=Button(frame1,text='List All Notes',bg='red',width=25,height=2,fg='white',command=liste).grid(row=0,column=1,padx=5,pady=10)
button3=Button(frame2,text='Search',bg='red',width=10,height=1,fg='white',command=search).grid(row=2,column=1)

mainloop()
