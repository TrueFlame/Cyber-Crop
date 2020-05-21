import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Camera:
    def __init__ (self, camera_id, model, type):
        self.camera_id = camera_id
        self.model = model
        self.type = type

    def Expanse_Overview():
        white 		= "#ffffff"
        lightBlue2 	= "#adc5ed"
        font 		= "Constantia"
        fontButtons = (font, 12)
        maxWidth  	= 800
        maxHeight 	= 480

	
        mainWindow = Tk()
        mainWindow.configure(bg=lightBlue2)
        mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
        mainWindow.resizable(0,0)
	

        mainFrame = ttk.Frame(mainWindow)
        mainFrame.place(x=20, y=20)                

        #Capture video frames
        lmain = ttk.Label(mainFrame)
        lmain.grid(row=0, column=0)

        cap = cv2.VideoCapture("your camera feed")
        ret, frame = cap.read()
    
        cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        
        img   = Image.fromarray(cv2image).resize((760, 400))
        imgtk = ImageTk.PhotoImage(image = img, master = mainWindow)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
    
        closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
        closeButton.configure(command= lambda: mainWindow.destroy())              
        closeButton.place(x=270,y=430)	

        show_frame()  #Display
        mainWindow.mainloop()  #Starts GUI
