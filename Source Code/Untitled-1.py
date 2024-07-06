import pymysql
from customtkinter import *
from CTkMessagebox import CTkMessagebox 
from tkinter import *
from datetime import *
from PIL import Image, ImageTk
win=CTk()
win.geometry("710x485")
win.title("pickAspot: Automared Parking Experience")
img=ImageTk.PhotoImage(Image.open("D:\\pickAspot\\pict2.jpg"))
imge=ImageTk.PhotoImage(Image.open("D:\\pickAspot\\logo1.png"))
lbl1=CTkLabel(win,text="",width=480,image=img)
lbl1.place(x=0,y=0)
lbl3=CTkLabel(win,text="",image=imge)
lbl3.place(x=0,y=40)
textimg=ImageTk.PhotoImage(Image.open("D:\\pickAspot\\choicetext1.png"))
lbl4=CTkLabel(win,text="",image=textimg,fg_color = ('#88909b'),text_color=('black'))
lbl4.place(x=450,y=150)

def parking_fr():
    global parkfr
    parkfr=CTk()
    parkfr.title("Parking Dashboard")
    parkfr.geometry("353x330")
    lbl8=CTkLabel(parkfr,text="    Parking Dashboard    ",bg_color="#b97c0c",height=65,font=("Arial Bold", 32),text_color='black')
    lbl8.place(x=0,y=0)
    lbl9=CTkLabel(parkfr,text ='', height=225, width=320,fg_color = ('#b97c0c'), text_color = ('black'),corner_radius = 10)
    lbl9.place(x=16,y=83)
    ent3=CTkEntry(parkfr,placeholder_text="Enter Name",border_width=0,height=30,width=294,corner_radius=20,bg_color="#b97c0c",fg_color='black')
    ent3.place(x=30,y=100)
    ent4=CTkEntry(parkfr,placeholder_text="Enter Phone Number",border_width=0,height=30,width=294,corner_radius=20,bg_color="#b97c0c",fg_color='black')
    ent4.place(x=30,y=140)
    ent5=CTkEntry(parkfr,placeholder_text="Enter Vehicle Number",border_width=0,height=30,width=294,corner_radius=20,bg_color="#b97c0c",fg_color='black')
    ent5.place(x=30,y=180)
    lbl10=CTkLabel(parkfr,text="SLOT : ",bg_color="#b97c0c",font=("Arial Bold", 14),text_color='black')
    lbl10.place(x=37,y=221)
    que="select * from slots"
    c.execute(que)
    a=c.fetchall()
    d = [item for i in a for item in i]
    combobox = CTkComboBox(parkfr, values=d,bg_color="#b97c0c",width=235,corner_radius=20,fg_color='black')
    combobox.place(x=87,y=220)
    btn7=CTkButton(parkfr,text="SUBMIT",hover_color = 'green',bg_color="grey",fg_color="black", command=lambda:[submit(ent3,ent4,ent5,combobox,parkfr)])
    btn7.place(x=30,y=260)
    btn8=CTkButton(parkfr,text="CANCEL",bg_color="grey",fg_color="black",hover_color="dark red",command=parkfr.destroy)
    btn8.place(x=180,y=260)
    parkfr.resizable(0,0)
    parkfr.mainloop()

def submit(nm,phn,vh,cm,parkfr):
    name=nm.get()
    phno=phn.get()
    vehno=vh.get().upper()
    combx=cm.get()
    now=datetime.now()
    global entime
    entime=now.strftime("%H:%M")
    que1="insert into entry values('{}',{},'{}','{}','{}')".format(name,phno,vehno,entime,combx)
    que2="delete from slots where slot='{}'".format(combx)
    c.execute(que1)
    c.execute(que2)
    c.execute("commit") 
    CTkMessagebox(title="PARKED",message="Vehicle Parked Successfully!!",icon="D:\\pickAspot\\tick.ico")
    parkfr.destroy()

def picking_fr():
    global pickfr
    pickfr=CTk()
    pickfr.title("Picking Dashboard")
    pickfr.geometry("388x270")
    lbl11=CTkLabel(pickfr,text="      Picking Dashboard      ",bg_color="#b97c0c",height=65,font=("Arial Bold", 32),text_color='black')
    lbl11.place(x=0,y=0)
    lbl13=CTkLabel(pickfr,text = '', height=165, width=360,fg_color = ('#b97c0c'), text_color = ('black'),corner_radius = 10)
    lbl13.place(x=16,y=83)
    lbl12=CTkLabel(pickfr,text="Please select your VEHICLE NO. and press SUBMIT : ",bg_color="#b97c0c",text_color='black',font=("Arial Bold", 14))
    lbl12.place(x=19,y=90)
    que4="select VehicleNo from entry"
    c.execute(que4)
    y=c.fetchall()
    e = [item for i in y for item in i]
    combobox1 = CTkComboBox(pickfr, values=e,bg_color="#b97c0c",fg_color='black',width=245,corner_radius=20)
    combobox1.place(x=70,y=130)
    btn10=CTkButton(pickfr,text="SUBMIT",hover_color = 'green',bg_color="#b97c0c",fg_color="black",command=lambda:[picsub(combobox1,pickfr)])
    btn10.place(x=42,y=200)
    btn11=CTkButton(pickfr,text="CANCEL",bg_color="#b97c0c",fg_color="black",hover_color="dark red",command=pickfr.destroy)
    btn11.place(x=195,y=200)
    pickfr.resizable(0,0)
    pickfr.mainloop()

def picsub(com,pickfr):
    nom=com.get()
    que5="select Slot from entry where VehicleNo='{}'".format(nom)
    c.execute(que5)
    u=c.fetchone()
    stt=""
    for item in u:
        stt=stt+item
    que6="select EntryTime from entry where VehicleNo='{}'".format(nom)
    c.execute(que6)
    o=c.fetchone()
    sty=""
    for itm in o:
        sty=sty+itm
    que8="delete from entry where VehicleNo='{}'".format(nom)
    c.execute(que8)
    que9="insert into slots values('{}')".format(stt)
    c.execute(que9)
    c.execute("commit")
    now=datetime.now()
    global exttime
    exttime=now.strftime("%H:%M")
    entrtime=datetime.strptime(sty,"%H:%M")
    ettime=datetime.strptime(exttime,"%H:%M")
    diff=ettime-entrtime
    seconds = diff.total_seconds() 
    hour = seconds / (60 * 60) 
    hour_f= "{:.2f}".format(hour) 
    houri=float(hour_f)
    pickfr.destroy()
    global resfr
    resfr=CTk()
    resfr.title("Payment Section")
    lblpay=CTkLabel(resfr,text="")
    lblpay.place(x=30,y=10)
    if houri<=1:
        lblpay.configure(text="Your billing amount is ₹35.0.")
    else:
        lblpay.configure(text="Your billing amount is ₹{}.".format(houri*35))
    resfr.geometry("388x270")
    resfr.resizable(0,0)
    resfr.mainloop()

parklbl=ImageTk.PhotoImage(Image.open("D:\\pickAspot\\parkbtn.png"))    
btn1 = CTkButton(win,text="",image=parklbl,width=0,height=0,border_width=0,bg_color='black',fg_color='black',text_color='black',corner_radius=30,command=parking_fr)
btn1.place(x=450,y=195)
picklbl=ImageTk.PhotoImage(Image.open("D:\\pickAspot\\pickbtn.png"))
btn2 = CTkButton(win,text="",image=picklbl,width=0,height=0,border_width=0,bg_color='black',fg_color='black',text_color = 'black',corner_radius=30,command=picking_fr)
btn2.place(x=450,y=290)

def customer_support():
    CTkMessagebox(title="Customer Support", message="For any queries or support you can contact to: \n7351415200\n0121-255693",icon="D:\\pickAspot\\supp.ico")

def about_us():
    CTkMessagebox(title="About Us",message="This app is designed and developed by Ansh as a project in DBMS.",icon="D:\\pickAspot\\dev.ico")
    
def manag_log():
    global Maglog
    Maglog=CTk()
    Maglog.geometry("500x250")
    Maglog.title("Management Login")
    lbl6=CTkLabel(Maglog,text = '', height=100, width=320,fg_color = ('white'), text_color = ('black'),corner_radius = 10)
    lbl6.place(x=90,y=70)
    lbl5=CTkLabel(Maglog,text="             Management Login             ",font=("Arial Bold", 32),height=48,bg_color="grey")
    lbl5.place(x=0,y=0)
    ent1=CTkEntry(Maglog,placeholder_text="Enter Username",border_width=0,height=30,width=300,bg_color='white')
    ent1.place(x=100,y=83)
    ent2=CTkEntry(Maglog,placeholder_text="Enter Password",show="*",border_width=0,height=30,width=300,bg_color='white')
    ent2.place(x=100,y=128)
    btn3=CTkButton(Maglog,text="Login",hover_color = 'green',bg_color="black",fg_color="grey",command=lambda:[mag_ent(ent1,ent2,Maglog)])
    btn3.place(x=100,y=188)
    btn4=CTkButton(Maglog,text="Exit",bg_color="black",fg_color="grey",hover_color="dark red",command=Maglog.destroy)
    btn4.place(x=260,y=188)
    Maglog.resizable(0,0)
    Maglog.mainloop()

def mag_ent(et1,et2,Maglog):
    user=et1.get()
    pas=et2.get()
    if user=='' and pas=='':
        Maglog.destroy()
        global mag_fr
        mag_fr=CTk()
        mag_fr.title("Management Dashboard")
        mag_fr.geometry("500x250")
        lbl7=CTkLabel(mag_fr, text = '', height=100, width=350,fg_color = ('white'), text_color = ('black'),corner_radius = 10)
        lbl7.place(x=90,y=57)
        btn3=CTkButton(mag_fr,text="Show available slots",corner_radius=20,bg_color='white')
        btn3.place(x=100,y=67)
        btn4=CTkButton(mag_fr,text="Show current parking",corner_radius=20,bg_color='white')
        btn4.place(x=260,y=67)
        btn5=CTkButton(mag_fr,text="Edit entry",corner_radius=20,bg_color='white')
        btn5.place(x=100,y=120)
        btn6=CTkButton(mag_fr,text="Exit",corner_radius=20,bg_color='white',command=mag_fr.destroy)
        btn6.place(x=260,y=120)
        mag_fr.resizable(0,0)
        mag_fr.mainloop()
    else:
        CTkMessagebox(title="Information",message="Invalid Username or Password!")

con=pymysql.connect(user="root",password="",host="localhost",database="pickaspot")
c=con.cursor()     
men=Menu(win)
men.add_command(label="Management Login",command=manag_log)
men.add_separator()
men.add_command(label="Customer Support",command=customer_support)
men.add_separator()
men.add_command(label="About Us",command=about_us)
men.add_separator()
men.add_command(label="Quit",command=win.destroy)
win.config(menu=men)
win.resizable(0,0)
win.mainloop()