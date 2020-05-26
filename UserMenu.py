import tkinter as tk
from PIL import Image, ImageTk

from Account import Account


class UserMenu(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LogIn)
        

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def createNewWindow(self):
        newWindow = tk.Toplevel(self)
        labelExample = tk.Label(newWindow, text = "New Window")
        buttonExample = tk.Button(newWindow, text = "New Window button")
        button1 = tk.Button(newWindow, text = "Press me so i can die", command = lambda:newWindow.destroy())
        
        
        labelExample.pack()
        buttonExample.pack()
        button1.pack()


class LogIn(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #image1 = Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg")
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        
        
        label2 = tk.Label(self, text="Log In ", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        
        button1 = tk.Button(self, text="Upgrade", command=lambda: master.switch_frame(Upgrade)).pack()
        button2 = tk.Button(self, text="Sign Up", command=lambda: master.switch_frame(SignUp)).pack()
        button3 = tk.Button(self, text = "Press Me", command = master.createNewWindow).pack()
        
        
 
class Upgrade(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        
        #image2 = Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg")
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label2 = tk.Label(self, image = photo)
        label2.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label2.pack()
        
        tk.Label(self, text="Upgrade", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogIn)).pack()

class SignUp(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        
        #image3 = Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg")
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="SignUp", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogIn)).pack()
        
    def ChooseCategory():
        pass
    
    def ChooseOption():
        pass
    

app = UserMenu()
app.geometry("500x500")
app.title("Cyber Crop")
app.mainloop()
