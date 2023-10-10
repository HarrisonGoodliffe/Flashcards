#Import tkinter
from tkinter import * 
import random



class flashcards:
    def __init__(self):
        self.engine = {
                        "ENGINE":"An engine or motor is a machine designed to convert one form of energy into mechanical energy.",
                        "GARETH":"GARETH"
                        
                        }
        self.gearbox = {
                        "GEARBOX":"A gearbox is a mechanical device utilized to increase the output torque or change the speed (RPM) of a motor.",
                        "GARETH":"GARETH"
                        }
        self.brakes = {
                        "BRAKES":"A brake is a mechanical device that inhibits motion by absorbing energy from a moving system.",
                        "GARETH":"GARETH"
                        }
        self.steering = {
                        "STEERING":"Steering is the collection of components, linkages, etc. which allows any vehicle (car, motorcycle, bicycle) to follow the desired course.",
                        "GARETH":"GARETH"
                        }
        self.suspension = {
                        "SUSPENSION":"Suspension is the system of tires, tire air, springs, shock absorbers and linkages that connects a vehicle to its wheels and allows relative motion between the two.",
                        "GARETH":"GARETH"
                        }
        self.wheels = {
                        "WHEELS":"A wheel is a circular component that is intended to rotate on an axle bearing.",
                        "GARETH":"GARETH"
                        }
        self.tyres = {
                        "TYRES":"A tire is a ring-shaped covering that fits around a wheel's rim to protect it and enable better vehicle performance.",
                        "GARETH":"GARETH"
                        }
        self.exhaust = {
                        "EXHAUST":"An exhaust system is usually piping used to guide reaction exhaust gases away from a controlled combustion inside an engine.",
                        "GARETH":"GARETH"
                        }  
    


info=flashcards()


def button_click_engine():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.engine.items())))

def button_click_gearbox():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.gearbox.items())))

def button_click_brakes():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.brakes.items())))

def button_click_steering():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.steering.items())))

def button_click_suspension():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.suspension.items())))

def button_click_wheels():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.wheels.items())))

def button_click_tyres():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.tyres.items())))

def button_click_exhaust():
    mainbox.delete(0.0,END)
    mainbox.insert(END, random.choice(list(info.exhaust.items())))

      

#create a window + assign to variable "window"
window = Tk()
#set a minimum size for the window
window.minsize(1000, 700)

#Give the window a title
window.title("Car Flashcards")

#create a label and adding to variable
label1 = Label(window, text="CARS")
#position the window
label1.grid(row=0, column=0, sticky=W)

#create a button widget
engine_button = Button(window, text="engine", width=5, command=button_click_engine)
engine_button.grid(row=5, column=1, sticky=W)
engine_button.tag = ("engine")
engine_button.place(x=20, y=20, width=100, height=100)

gearbox_button = Button(window, text="gearbox", width=5, command=button_click_gearbox)
gearbox_button.grid(row=7, column=1, sticky=W)
gearbox_button.tag = ("gearbox")
gearbox_button.place(x=20, y=120, width=100, height=100)

brakes_button = Button(window, text="brakes", width=5, command=button_click_brakes)
brakes_button.grid(row=9, column=1, sticky=W)
brakes_button.tag = ("brakes")
brakes_button.place(x=20, y=220, width=100, height=100)

steering_button = Button(window, text="steering", width=5, command=button_click_steering)
steering_button.grid(row=11, column=1, sticky=W)
steering_button.tag = ("steering")
steering_button.place(x=20, y=320, width=100, height=100)

suspension_button = Button(window, text="suspension", width=5, command=button_click_suspension)
suspension_button.grid(row=13, column=1, sticky=W)
suspension_button.tag = ("suspension")
suspension_button.place(x=20, y=420, width=100, height=100)

wheels_button = Button(window, text="wheels", width=5, command=button_click_wheels)
wheels_button.grid(row=15, column=1, sticky=W)
wheels_button.tag = ("wheels")
wheels_button.place(x=20, y=520, width=100, height=100)

tyres_button = Button(window, text="tyres", width=5, command=button_click_tyres)
tyres_button.grid(row=17, column=1, sticky=W)
tyres_button.tag = ("tyres")
tyres_button.place(x=20, y=620, width=100, height=100)

exhaust_button = Button(window, text="exhaust", width=5, command=button_click_exhaust)
exhaust_button.grid(row=19, column=1, sticky=W)
exhaust_button.tag = ("exhaust")
exhaust_button.place(x=20, y=720, width=100, height=100)




#create the text box to display info
mainbox = Text(window, width=30, height=30, wrap=WORD, background="white")
#mainbox.grid(row=5, column=15, columnspan=5, sticky=W)
mainbox.place(x=200, y=20, width=300, height=400)


#Run the event loop
window.mainloop()