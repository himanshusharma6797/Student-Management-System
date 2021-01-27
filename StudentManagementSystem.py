def addstudent():
    def submitadd():
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)' # this is query
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addedtime, addeddate))
            con.commit()
            res = messagebox.askyesno(
                'Notification', 'Id {} Name {} Student successfully added do you want to clean the form.'.format(id,
                                                                                                                 name)
                , parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications','Sorry Id already exist.', parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Add Student')
    addroot.config(bg='blue')
    addroot.iconbitmap("lala.ico")
    addroot.resizable(False, False)

    #-------------------------------------- Add student labels
    idlable = Label(addroot, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(addroot, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelable.place(x=10, y=70)

    mobilelable = Label(addroot, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelable.place(x=10, y=130)

    emaillable = Label(addroot, text='Enter E-mail : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(addroot, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(addroot, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(addroot, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblable.place(x=10, y=370)

    ##--------------------------------------------------------- add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    #############------------------------------- add button
    submitbt = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=submitadd)
    submitbt.place(x=150, y=420)

    addroot.mainloop()


def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr, id)
            datas = mycursor.fetchall()

            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr, mobile)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr, email)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            # command for data cleaning if we do not doing this then the old data will showing
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)  # searching data will showing in the list

        elif(gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr, gender)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr, dob)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr, addeddate)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Search Student')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap("lala.ico")
    searchroot.resizable(False,False)
    #-------------------------------------- Add student labels

    idlable = Label(searchroot, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3
                    , width=12, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(searchroot, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelable.place(x=10, y=70)

    mobilelable = Label(searchroot, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12
                    , anchor='w')
    mobilelable.place(x=10, y=130)

    emaillable = Label(searchroot, text='Enter E-mail : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(searchroot, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(searchroot, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(searchroot, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblable.place(x=10, y=370)

    datelable = Label(searchroot, text='Enter Date : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelable.place(x=10, y=430)

    ##--------------------------------------------------------- add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    #############-------------------------------add button
    submitbt = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=search)
    submitbt.place(x=150, y=480)

    searchroot.mainloop()


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully.'.format(pp))

    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        strr='update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Modified Successfully'.format(id), parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x590+220+160')
    updateroot.title('Search Student')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap("lala.ico")
    updateroot.resizable(False, False)
    #-------------------------------------- Add student labels
    idlable = Label(updateroot, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3
                    , width=12, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(updateroot, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelable.place(x=10, y=70)

    mobilelable = Label(updateroot, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelable.place(x=10, y=130)

    emaillable = Label(updateroot, text='Enter E-mail : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(updateroot, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(updateroot, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(updateroot, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblable.place(x=10, y=370)

    datelable = Label(updateroot, text='Enter Date : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelable.place(x=10, y=430)

    timelable = Label(updateroot, text='Enter Time : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelable.place(x=10, y=490)

    ##---------------------------------------------------------- add student entry

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    #############------------------------------- add button
    submitbt = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=update)
    submitbt.place(x=150, y=540)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()


def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]),
        gender.append(pp[5]), dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added time']
    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is saved in {}'.format(paths))


def exitstudent():
    res = messagebox.askyesno('Notifiaction','Do you want to exit?')
    if res == True:
        root.destroy()


############################################################################ connection of database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),' \
                   'address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database created and now you are connected to the database.....',
                                parent=dbroot)
        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database!', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('Student.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    #-----------------------------Connectdb Labels
    hostlabel = Label(dbroot, text="Enter Host :", bg="gold2", font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User :", bg="gold2", font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg="gold2", font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)


    #-------------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry= Entry(dbroot,font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #-----------------------------------------Connectdb button
    submitbutton = Button(dbroot, text='submit', font=('roman', 15, 'bold'), bg='lemon chiffon', bd=5, width=20,
                          activebackground='gray30', activeforeground='white', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()
##################################################


def tick():
    time_string = time.strftime('%H:%M:%S')
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date :'+date_string+"\n""Time :"+time_string)
    clock.after(200, tick)

############################################################################INTRO SLIDER


import random
colors =['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLableColorTick():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(20, IntroLableColorTick)


def IntroLableTick():
    global count, text
    if count >= len(hs):
        count = 0
        text = ''
        SliderLable.config(text=text)
    else:
        text = text+hs[count]
        SliderLable.config(text=text)
        count += 1
    SliderLable.after(150, IntroLableTick)
##########################################################################################


from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='gold3')
root.geometry('1170x700+200+50')
root.iconbitmap("college.ico")
root.resizable(False, False)


##########################################################################################  Frames
##-------------------------------------------------------------------------------- dataentry Frame
DataEntryFrame = Frame(root, bg='light goldenrod', relief=GROOVE, borderwidth=4)
DataEntryFrame.place(x=10, y=88, width=500, height=600)

frontlabel = Label(DataEntryFrame, text='------------------Welcome------------------', width=30,
                   font=("arial", 22, 'italic bold'), bg='gold3')
frontlabel.pack(side=TOP, expand=True)
addbtn = Button(DataEntryFrame, text='1. Add Student', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3',
                activebackground='blue', relief=RIDGE, activeforeground='white', command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='2. Search Student', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3'
                   , activebackground='blue', relief=RIDGE, activeforeground='white', command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='3. Delete Student', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3'
                   , activebackground='blue', relief=RIDGE, activeforeground='white', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='4. Update Student', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3'
                   , activebackground='blue', relief=RIDGE, activeforeground='white', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(DataEntryFrame, text='5. Show All', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3',
                    activebackground='blue', relief=RIDGE, activeforeground='white', command=showstudent)
showallbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='6. Export Data', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3',
                   activebackground='blue', relief=RIDGE, activeforeground='white', command=exportstudent)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='7. Exit', font=('chiller', 20, 'bold'), width=20, bd=6, bg='skyblue3',
                 activebackground='blue', relief=RIDGE, activeforeground='white', command=exitstudent)
exitbtn.pack(side=TOP, expand=True)


##-------------------------------------------------------------------------Show data frame
ShowDataFrame = Frame(root, bg='light goldenrod', relief=GROOVE, borderwidth=4)
ShowDataFrame.place(x=540, y=88, width=620, height=600)

#------------------------------------------------------------------Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B',
                                                'Added Date', 'Added Time'), yscrollcommand=scroll_y.set,
                        xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=200)
studenttable.column('Mobile No', width=200)
studenttable.column('Email', width=300)
studenttable.column('Address', width=200)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date', width=150)
studenttable.column('Added Time', width=150)
studenttable.pack(fill=BOTH, expand=1)

##########################################################################################Slider
hs = 'WELCOME TO STUDENT MANAGEMENT SYSTEM'
count = 0
text = ''

##########################################################################################
SliderLable = Label(root, text=hs, font=('Arial', 20, 'italic bold'), relief=RIDGE, borderwidth=4, width=38, bg='khaki')
SliderLable.place(x=260, y=0 )
IntroLableTick()
IntroLableColorTick()

##########################################################################################Clock
clock = Label(root, font=('times', 15, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()

####################################################################### ConnectDatabaseButton
connectbutton = Button(root, text='Connect To Database', width=17, font=('normal', 16, 'bold'), relief=RIDGE,
                       borderwidth=4, bd=6, bg='green2', activebackground='blue', activeforeground='white',
                       command=Connectdb)
connectbutton.place(x=932.1, y=0)
root.mainloop()
