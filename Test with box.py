import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *


def get_scale(eventorigin):
    global x0,y0
    x1 = eventorigin.x
    y1 = eventorigin.y
    
    print("x - ", x1," y - ", y1)
    box_bound.append(x1)
    box_bound.append(y1)
    print(box_bound)
    

    #print("Angle rotor 1 - ", start_deg + y0*discr)
    #w.delete("all")
    #lmain.create_image(0, 0, image=img, anchor="nw")
    #lmain.create_oval(x0-3, y0-3, x0+3, y0+3, width = 0, fill = 'red')
    
def get_box():
    lmain.bind("<Button 1>", get_scale)
    

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()
box_bound = []

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    cropped = img.crop((0, 0, 200, 200))
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    while len(box_bound) < 10:
        get_box()
    cropped = img.crop((box_bound[4]-5, box_bound[7]-5, box_bound[8]+5, box_bound[3]+5))

show_frame()
root.mainloop()