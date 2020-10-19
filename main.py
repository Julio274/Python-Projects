#importing all files from tkinter
from tkinter import *

#defining the height and width of button
button_height=1
button_width=3

#This Defines the function for click event
def click(event):
    global scvalue      #Global variable "scvalue"
    text = event = event.widget.cget("text")
    print(text)
    #This will check if the input text from user is "="
    if text == "=":
        #this will check if the scvalue is a digit or not
        if scvalue.get().isdigit():
            #this will evaluate the string value like if we type 7*8 it will give 56 as result.
            value= eval(scvalue.get())
        else:
            try:
              value= eval(scvalue.get())
            except Exception as e:
                print(e)
                value="ERROR"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        pass
    else:
        scvalue.set(scvalue.get() +text)  # this will combine the value of scvalue and text
        screen.update()  # It force updation

#It creates tkinter window or root window
root = Tk()
#Defining the geometry of the root or tkinter window
root.geometry("644x700")
#Defining the title of root or tkinker window
root.title(" SIMPLE CALCULATOR ")

#this define "scvalue" as String variable (Note: It is a global variable )
scvalue = StringVar()
#set() method is used to set and change the value stored within a tkinter variable here the variable is "scvalue"
scvalue.set("")
#Entry widget is used to accept the single line input from the user.
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
#pack() method with screen is used to organize the geometry of widget in blocks after placing in parent widget.i.e it act as a geometry manager
screen.pack(fill=X, ipadx=8, padx=10, pady=10)


#Frame for first row
#Frame widget to create container to hold other widgets (here it is holding Button widget)
f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=18, font="lucida 20 bold")  #Button Widget
b.pack(side=LEFT, padx=18, pady=5)    #packing button widget
b.bind("<Button-1>", click)           #binding function to the event "CLICK"

b = Button(f, text="8", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack() #pack() method to organize the geometry of object "f" of Frame widget


#Frame for second row
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


#Frame for third row
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)



f.pack()

#running mainloop
root.mainloop()
