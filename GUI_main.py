import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *

# Create the main application window
root = tk.Tk()
root.configure(background="whitesmoke")
root.title("Main")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

image2=Image.open('3.jpg')
image2=image2.resize((w,h),Image.LANCZOS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


def reg():
    from subprocess import call
    call(["python","registration.py"])
    
    
def log():
    from subprocess import call
    call(["python","login.py"])
    
    

    
    
    
lbl = tk.Label(root, text=" Soil Classification & Suggest  Crop Life Cycle ",height=1,width=47, font=('Elephant', 35,' bold '),bg="white",fg="black")
lbl.place(x=1, y=15)


canvas0 = tk.Canvas(root,background="yellow",height=2,width=1600,borderwidth=0, highlightthickness=0)
canvas0.place(x=2,y=15)

canvas0 = tk.Canvas(root,background="yellow",height=2,width=1600,borderwidth=0, highlightthickness=0)
canvas0.place(x=2,y=80)




# line01 = canvas0.create_line(890, 20, 890, 190, fill="White", width=1)


# current_image_index = 0

# canvas0 = tk.Canvas(root,background="yellow",height=45,width=1500,borderwidth=0, highlightthickness=0)
# canvas0.place(x=2,y=650)

button1= tk.Button(root, text='''REGISTER''',background="white" ,font=("Times New Roman",20),bd=0,command=reg )
button1.place(x=1350,y=100)



button4= tk.Button(root, text="LOG IN" ,background="white",font=("Times New Roman",20),bd=0,command=log)
button4.place(x=1200,y=100)

root.mainloop()