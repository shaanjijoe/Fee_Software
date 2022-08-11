import struct
from tkinter import *
from typing import Dict
from a1_format import *


def rgb(colors):
    return "#%02x%02x%02x" % colors  

def b1_logout():
    Mframe.place_forget()
    Addstudframe.place_forget()
    Sframe.place(x=0,y=0)

def b1_returntomenu():
    Addstudframe.place_forget()
    Mframe.place(x=0,y=0)
    Addstudframe.place_forget()



def b1_addstudent():
    Mframe.place_forget()
    global Addstudframe
    Addstudframe=LabelFrame(root,text="Add Student Page",width=screen_width-40,height=screen_height-100)
    Addstudframe.place(x=0,y=0)
    Addstudframe.configure(bg='white')
    # Addstudframe.place(relx=0.02,rely=0.02)
            
    def addstudentpagerefresh():
        admissionnoentry2.delete(0,END)
        studentnameentry2.delete(0,END)
        fathernameentry2.delete(0,END)
        phonenumberentry2.delete(0,END)
        Errorlabel2.config(text="")
        defaultradio2.select()

    def addstudentpagesubmit():
        kernel=[0,0,0,0,0,[],0,0,0,0]
        diction=dict()
        # kernel[0]=admissionnoentry2.get()
        diction['ADMINNO']=admissionnoentry2.get()
        # kernel[1]=studentnameentry2.get()
        diction['NAME']=studentnameentry2.get()
        # kernel[2]=fathernameentry2.get()
        diction['FATHERNAME']=fathernameentry2.get()
        # kernel[3]=phonenumberentry2.get()
        diction['PHONENUM']=phonenumberentry2.get()
        # kernel[4]=classname2.get()
        diction['CLASS']=classname2.get()
        if (diction['ADMINNO']==''):
            Errorlabel2.config(text="Admission Number field cannot be empty")
        elif (a1_checknumber(diction['ADMINNO'])==False):
            Errorlabel2.config(text="Only Numeric enrtries in admission number")
        elif (diction['NAME']==''):
            Errorlabel2.config(text="Student Name field cannot be empty")
        elif (diction['FATHERNAME']==''):
            Errorlabel2.config(text="Father Name field cannot be empty")
        elif (diction['PHONENUM']==''):
            Errorlabel2.config(text="Phone Number field cannot be empty")
        elif (a1_checknumber(diction['PHONENUM'])==False):
            Errorlabel2.config(text="Only Numeric enrtries in phone number")
        elif (diction['CLASS']==-1):
            Errorlabel2.config(text="Please select class")
        else:
            Errorlabel2.config(text="")
            print(diction)
            # outcome41=addstudentmiddleman(kernel)
            # print(outcome41)
            # if (outcome41==True):
            #     Errorlabel2.config(text="Success")
            # else:
            #     Errorlabel2.config(text="Failed")
    classlist=['NUR','LKG','UKG','I','II','III','IV','V','VI','VII','VII']
    

    logout=Button(Addstudframe, text="Logout", command=b1_logout,height=3,width=12)
    logout.place(relx=0.88,rely=0.05)
    logout.config(font=('Helvatical bold',15),bg="white")

    returnback=Button(Addstudframe, text="Return", command=b1_returntomenu,height=3,width=12)
    returnback.place(relx=0.88,rely=0.19)
    returnback.configure(font=('Helvatical bold',15),bg="white")

    
    butsubmit2=Button(Addstudframe, text="Submit", command=addstudentpagesubmit,height=3,width=12)
    butsubmit2.place(relx=0.75,rely=0.33)
    butsubmit2.configure(font=('Helvatical bold',15),bg="white")

    butrefresh2=Button(Addstudframe, text="Refresh", command=addstudentpagerefresh,height=3,width=12)
    butrefresh2.place(relx=0.88,rely=0.33)
    butrefresh2.configure(font=('Helvatical bold',15),bg="white")
  


    admissionno2=Label(Addstudframe, text="Admission No :")
    admissionno2.place(relx=0.05,rely=0.1)
    admissionno2.config(font=('Helvatical bold',15),bg="white")

   
    studentname2=Label(Addstudframe, text="Student Name :")
    studentname2.place(relx=0.05,rely=0.2)
    studentname2.config(font=('Helvatical bold',15),bg="white")

      
    fathername2=Label(Addstudframe, text="Father Name :")
    fathername2.place(relx=0.05,rely=0.3)
    fathername2.config(font=('Helvatical bold',15),bg="white")

    phonenumber2=Label(Addstudframe, text="Phone number :")
    phonenumber2.place(relx=0.05,rely=0.4)
    phonenumber2.config(font=('Helvatical bold',15),bg="white")

    
    Errorlabel2=Label(Addstudframe, text="")
    Errorlabel2.place(relx=0.05,rely=0.5)
    Errorlabel2.config(font=('Helvatical bold',15),bg="white")

      
    admissionnoentry2=Entry(Addstudframe, width=20,font=('Helvatical bold',15),borderwidth=3)
    admissionnoentry2.place(relx=0.2,rely=0.1)


    studentnameentry2=Entry(Addstudframe, width=20,font=('Helvatical bold',15),borderwidth=3)
    studentnameentry2.place(relx=0.2,rely=0.2)

 
   
    fathernameentry2=Entry(Addstudframe, width=20,font=('Helvatical bold',15),borderwidth=3)
    fathernameentry2.place(relx=0.2,rely=0.3)

    
    phonenumberentry2=Entry(Addstudframe, width=20,font=('Helvatical bold',15),borderwidth=3)
    phonenumberentry2.place(relx=0.2,rely=0.4)


    
    # class selector 

    classlabel2=Label(Addstudframe, text="Class :")
    classlabel2.place(relx=0.45,rely=0.1)
    classlabel2.config(font=('Helvatical bold',15),bg="white")

    
    classname2=IntVar()

    r02=Radiobutton(Addstudframe,text=classlist[0],value=0,variable=classname2,bg="white",font=('Helvatical bold',14))
    r12=Radiobutton(Addstudframe,text=classlist[1],value=1,variable=classname2,bg="white",font=('Helvatical bold',14))
    r22=Radiobutton(Addstudframe,text=classlist[2],value=2,variable=classname2,bg="white",font=('Helvatical bold',14))
    r32=Radiobutton(Addstudframe,text=classlist[3],value=3,variable=classname2,bg="white",font=('Helvatical bold',14))
    r42=Radiobutton(Addstudframe,text=classlist[4],value=4,variable=classname2,bg="white",font=('Helvatical bold',14))
    r52=Radiobutton(Addstudframe,text=classlist[5],value=5,variable=classname2,bg="white",font=('Helvatical bold',14))
    r62=Radiobutton(Addstudframe,text=classlist[6],value=6,variable=classname2,bg="white",font=('Helvatical bold',14))
    r72=Radiobutton(Addstudframe,text=classlist[7],value=7,variable=classname2,bg="white",font=('Helvatical bold',14))
    r82=Radiobutton(Addstudframe,text=classlist[8],value=8,variable=classname2,bg="white",font=('Helvatical bold',14))
    r92=Radiobutton(Addstudframe,text=classlist[9],value=9,variable=classname2,bg="white",font=('Helvatical bold',14))
    r102=Radiobutton(Addstudframe,text=classlist[10],value=10,variable=classname2,bg="white",font=('Helvatical bold',14))
    defaultradio2=Radiobutton(Addstudframe,text="",value=-1,variable=classname2,bg="white",font=('Helvatical bold',14))

    defaultradio2.select()
   
    r02.place(relx=0.52,rely=0.1)
    r12.place(relx=0.62,rely=0.1)  
    r22.place(relx=0.72,rely=0.1)
    r32.place(relx=0.52,rely=0.15) 
    r42.place(relx=0.62,rely=0.15)
    r52.place(relx=0.72,rely=0.15) 
    r62.place(relx=0.82,rely=0.15)
    r72.place(relx=0.52,rely=0.2)
    r82.place(relx=0.62,rely=0.2)
    r92.place(relx=0.72,rely=0.2) 
    r102.place(relx=0.82,rely=0.2)

    # addstudentpagerefresh()  

###















def b1_mainpage():
    Sframe.place_forget()
    global Mframe
    Mframe=LabelFrame(root,text="Main Page",width=screen_width-40,height=screen_height-100)
    Mframe.place(x=0,y=0)
    Mframe.configure(bg='white')
    # if(usernameentry.get()!="abc" and passwordentry.get()!="123"):
    #     root.destroy()
    
    addstudent=Button(Mframe, text="Add a student", command=b1_addstudent,height=7,width=22)
    addstudent.place(relx=0.05,rely=0.15)
    addstudent.config(font=('Helvatical bold',15),bg="white")

    payfee=Button(Mframe, text="Pay Fees", command=b1_mainpage,height=7,width=22)
    payfee.place(relx=0.25,rely=0.15)
    payfee.config(font=('Helvatical bold',15),bg="white")

    editinfo=Button(Mframe, text="Edit Info", command=b1_mainpage,height=7,width=22)
    editinfo.place(relx=0.45,rely=0.15)
    editinfo.config(font=('Helvatical bold',15),bg="white")

    showfeestatus=Button(Mframe, text="Show Fees", command=b1_mainpage,height=7,width=22)
    showfeestatus.place(relx=0.65,rely=0.15)
    showfeestatus.config(font=('Helvatical bold',15),bg="white")

    logout=Button(Mframe, text="Logout", command=b1_logout,height=3,width=12)
    logout.place(relx=0.88,rely=0.05)
    logout.config(font=('Helvatical bold',15),bg="white")






def b1_mainframe():
    global Sframe
    Sframe=LabelFrame(root,text="First Page",width=screen_width-40,height=screen_height-100)
    Sframe.place(x=0,y=0)
    Sframe.configure(bg='white')

    S2frame=LabelFrame(Sframe,width=700,height=400)
    S2frame.place(relx=0.27,rely=0.25)
    S2frame.configure(bg='white',borderwidth=2,padx=30,pady=40)


    username=Label(S2frame, text="User Name :")
    username.place(relx=0.20,rely=0.30)
    username.config(font=('Helvatical bold',15),bg="white")

    password=Label(S2frame, text="Password  :")
    password.place(relx=0.20,rely=0.50)
    password.config(font=('Helvatical bold',15),bg="white")

    global usernameentry
    usernameentry=Entry(S2frame, width=20,font=('Helvatical bold',15),borderwidth=3)
    usernameentry.place(relx=0.48,rely=0.30)

    global passwordentry
    passwordentry=Entry(S2frame, width=20,font=('Helvatical bold',15),borderwidth=3)
    passwordentry.place(relx=0.48,rely=0.50)

    but=Button(S2frame, text="Submit", command=b1_mainpage,height=2,width=15)
    but.place(relx=0.350,rely=0.70)
    but.config(font=('Helvatical bold',15),bg="white")

    return

# Window Characters
root=Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
strsize=str(screen_width)+"x"+str(screen_height)
root.title("Fee Software")
root.geometry(strsize)
# root.minsize(width=1200,height=700)
# root.maxsize(width=1200,height=700)
root.maxsize(width=screen_width-5,height=screen_height-5)
root.configure(bg=rgb((255,255,240)),padx=20,pady=5)
b1_mainframe()
root.mainloop()

# b1_mainframe()