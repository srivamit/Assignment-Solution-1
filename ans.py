from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  

labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)

lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
  
lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)  
  
lb4= Label(base, text="Contact Number", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  
  
lb5= Label(base, text="Address", width=15, font=("arial",12))  
lb5.place(x=19, y=240)  
en5= Entry(base)  
en5.place(x=200, y=240)  


Button(base, text="Submit", width=10).place(x=200,y=400)  
base.mainloop()  
