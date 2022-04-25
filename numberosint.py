from tkinter import *
from tkinter import font 
from tkinter import scrolledtext
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import subprocess
import socket 
number = Tk()

myfont = font.Font (family="Helvetica",size= 12 , weight="bold")

number.geometry("1300x800")
number.title("NUMOSINT")
number['background'] = '#728FCE'
homepage = Frame(number, width=150 , height=150)
def ping():
    cmd = ["ping", entry.get(), "-c", "10"]
    output = subprocess.check_output(cmd) #output = subprocess.check_output("ping {} -c 2".format(entry.get()), shell=True)
    print('>', output)# put result in label
    ping_scrolled_text.insert(END,"Processing...................","\n")
    ping_scrolled_text.insert(INSERT,"\n")
    ping_scrolled_text.insert(END,output ,"\n")

def close():
    number.destroy()

def numbers():
    numbers = num.get()
    global ch_number 
    ch_number = phonenumbers.parse(numbers, "CH")
    print(geocoder.description_for_number(ch_number, "en"))
    global service_provider
    service_provider = phonenumbers.parse(numbers, "RO")
    print(carrier.name_for_number(service_provider, "en"))
    item_scrolled_text.insert(END ,"Processing Results..............." ,"\n")
    item_scrolled_text.insert(INSERT,"\n")
    item_scrolled_text.insert(END ,(geocoder.description_for_number(ch_number, "en")) )
    item_scrolled_text.insert(INSERT,"\n")

    item_scrolled_text.insert(END , (carrier.name_for_number(service_provider, "en")),"\n")
def reset():
    item_scrolled_text.delete(1.0, END)
    number_result = Label(item_scrolled_text, text="NUMBER RESULTS WILL SHOW  HERE >", font=myfont)
    item_scrolled_text.window_create("end",window=number_result)
    num.set("")
def clear():
    ping_scrolled_text.delete(1.0,END)
    ping_result = Label(ping_scrolled_text, text="PING RESULTS WILL SHOW  HERE ", font=myfont, fg="black", bg="grey")
    ping_scrolled_text.window_create("end",window=ping_result)
    entry.set("")
    ip.set("")

def url():
    url = ip.get() 
    print("IP:",socket.gethostbyname(url))
    ping_entry.insert(END, (socket.gethostbyname(url)))

    



welcome_label = Label(number , text="WELCOME TO NUMPINGOSINT TOOL" ,font=myfont , bg="#6600cc" ) 
welcome_label.pack()
number_input = Label ( number , text = " INPUT NUMBER HERE" , font=myfont, bg="#728FCE")
number_input.place(x=100, y=100)
global num
global ip
num = StringVar()
entry=StringVar()
ip=StringVar()
global number_entry
number_entry = Entry(number, textvariable=num, font=myfont)
number_entry.place(x=100, y=150)
number_btn = Button(number, text="ScanNumber", bg="blue", fg="white" , command=numbers)
number_btn.place(x=100, y=200)

ping_label = Label(number, font=myfont , text="INPUT IP ADDRESS" , bg="#728FCE")
ping_label.place(x=100, y=250)
ping_entry = Entry(number, textvariable=entry , font=myfont )
ping_entry.place(x=100 , y=300)
ping_btn = Button(number, bg="blue" , text="Ping ", fg="White" , command=ping)
ping_btn.place(x=100, y = 350)
clear_btn = Button(number, bg="red", fg="white", text="Clear", command=clear )
clear_btn.place(x=200, y=350)

reset_btn = Button(number, fg="white", text="reset", bg="red", command=reset)
reset_btn.place(x=250,y=200)

close_btn = Button(number, text="Terminate" , bg="black",fg="red" , command=close, font=myfont)
close_btn.place(x=1150, y=0)

ip_label = Label (number, text="PASTE URL HERE" , font=myfont , fg="black", bg="#728FCE")
ip_label.place(x=100, y=400)
ip_entry= Entry(number, textvariable=ip, font=myfont )
ip_entry.place(x=100, y=450)
ip_btn = Button(number, text="Get_IP", bg="blue", fg="white" ,command=url)
ip_btn.place(x=100, y=500)

item_scrolled_text = scrolledtext.ScrolledText(number, width=40, height=20 , fg="green", bg="black")
item_scrolled_text.place(x=500, y=100)

ping_scrolled_text = scrolledtext.ScrolledText(number, width=35, height=30, bg="black", fg="green")
ping_scrolled_text.place(x=900, y=100)

ping_result = Label(ping_scrolled_text, text="PING RESULTS WILL SHOW  HERE ", font=myfont, fg="black", bg="grey")
ping_scrolled_text.window_create("end",window=ping_result)

creation_label = Label(number, text="Created by $z3ux \n www.e-poltechsolutions.com")
creation_label.place(x=1100, y=650)

number_result = Label(item_scrolled_text, text="NUMBER RESULTS WILL SHOW  HERE >",font=myfont)
item_scrolled_text.window_create("end",window=number_result)
number.mainloop()

