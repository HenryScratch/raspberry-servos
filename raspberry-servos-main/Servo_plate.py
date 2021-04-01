#Готовый к релизу вариант

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog
import math
import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

#Исходные данные

h = 50 #Расстояние от стола до прибора
a = 1.2*h #Длина зоны покрытия
b = math.sqrt((pow(h,2)+pow((a/2),2))) #Второстепенная информация
c = a/2
a = h
angle = (math.acos((pow(b,2)+pow(c,2)-pow(a,2))/(2*c*b))  * 180) / math.pi #угол около камеры
angle = math.ceil(angle)

start_deg = 60

step = angle / (c*2)

discr = angle / 500

print(h,c*2,angle,step,discr)


root = Tk()

#setting up a tkinter canvas
w = Canvas(root, width=500, height=500)
w.pack()

#adding the image
File = askopenfilename(parent=root, initialdir="./",title='Select an image')
original = Image.open(File)
original = original.resize((1000,1000)) #resize image
img = ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")


# Determine the origin by clicking
def getorigin(eventorigin):
    global x0,y0
    x0 = eventorigin.x
    y0 = eventorigin.y
    
    print("x - ", x0 - 250 ," y - ", y0 - 250)
    print(cart2pol(x0 - 250 , y0 - 250))
    print()
    dist = math.sqrt((x0 - 250)**2 + (y0 - 250)**2)
    #print("dist - ", dist)
    
    deltaX = x0 - 250;
    deltaY = y0 - 250;
    rad = math.atan2(deltaY, deltaX) # In radians
    deg = rad * (180 / math.pi)
    #print("angle - ", deg)
    print()
    
    #Перевод в новые координаты
    if deg < 0:
        #print("angle - ", deg * -1, "dist - ", dist * -1)
        
        print("Angle rotor 1 - ", start_deg + (dist * -1)*discr)
        print("Angle rotor 2 - ", deg * -1)
        
    else:
        #print("angle - ", deg, "dist - ", dist)
        
        print("Angle rotor 1 - ", start_deg + dist*discr)
        print("Angle rotor 2 - ", deg)

    #print("Angle rotor 1 - ", start_deg + y0*discr)
    w.delete("all")
    w.create_image(0, 0, image=img, anchor="nw")
    w.create_oval(x0-3, y0-3, x0+3, y0+3, width = 0, fill = 'green')
    
#mouseclick event
w.bind("<Button 1>",getorigin)

root.mainloop()