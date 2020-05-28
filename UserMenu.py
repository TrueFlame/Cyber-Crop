import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


##################

from Account import *

############################



class CyberCrop(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        
        self.characteristics()
        
        self.switch_frame(LogInGUI)
        

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



    def displayUpgrade(self):
        newWindow = tk.Toplevel(self)
        newWindow.geometry("480x240")
        newWindow.title("Cyber Crop")
        
        labelExample = tk.Label(newWindow, text = "Upgrade your Account")
        buttonExample = ttk.Button(newWindow, text = "Press to Upgrade")
        button1 = ttk.Button(newWindow, text = "Press me so i can DIE", command = lambda:newWindow.destroy())
        
        labelExample.pack()
        buttonExample.pack()
        button1.pack()


    def characteristics(self):
        self.resizable()
        self.title("Cyber Crop")
        self.geometry("640x480")
        self.configure(background = "white")
        self.iconbitmap("logo.ico")
        
        
    
class LogInGUI(tk.Frame):
  
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        
        ################# make the text blink
        def on_entry_click_username(event):
            """function that gets called whenever entry is clicked"""
            if username.get() == 'Enter your username...':
                username.delete(0, "end") # delete all the text in the entry
                username.insert(0, '') #Insert blank for user input
                username.config(fg = 'black')
        def on_focusout_username(event):
            if username.get() == '':
                username.insert(0, 'Enter your username...')
                username.config(fg = 'grey')
                
                
        def on_entry_click_password(event):
            """function that gets called whenever entry is clicked"""
            if password.get() == 'Enter your password...':
                password.delete(0, "end") # delete all the text in the entry
                password.insert(0, '') #Insert blank for user input
                username.config(fg = 'black')
        def on_focusout_password(event):
            if password.get() == '':
                password.insert(0, 'Enter your password...')
                password.config(fg = 'grey')        
        
        ########################################################################
        
        def check_data(database: dict):
            password_data = password.get()
            username_data = username.get()
            
            password.delete(0, "end")
            username.delete(0, "end")
            
            global global_username # xrisimopoieitai pio poly gia quality of life, emfanizei ston xristi to username tou kata tin eisodo
            
            
            if password_data in database.values() and username_data in database.keys():
                
                global_username = username_data 
                master.switch_frame(WelcomeUser)
            else:
                master.displayUpgrade()
        
        # logo
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, columnspan = 6)
        
        # Entries
        ##################
        username = tk.Entry(self, width = 30)
        username.grid(row = 3, column = 2)
        username.insert(0, "Enter your username...")
        
        username.bind('<FocusIn>', on_entry_click_username)
        username.bind('<FocusOut>', on_focusout_username)
        username.config(fg = 'black')
        
        
        
        ########################
        
        password = tk.Entry(self, width = 30, show = "*")
        password.grid(row = 5, column = 2, padx = 30)
        password.insert(0, "Enter your password...")
        
        password.bind('<FocusIn>', on_entry_click_password)
        password.bind('<FocusOut>', on_focusout_password)
        #password.config(fg = 'grey')
        
        
        ############################
        #label2 = tk.Label(self, text="Log In ", font=('Helvetica', 32, "bold")).grid(row = 2 , column = 2)
        
        #Labels
        ttk.Label(self, text = "Username:").grid(row = 3, column = 1)
        ttk.Label(self, text = "Password:").grid(row = 5, column = 1)
        
        
        # Buttons - Log In
        button1 = ttk.Button(self, text="Upgrade", command=lambda: master.switch_frame(UpgradeGUI)).grid(row = 6, column = 3)
        button2 = ttk.Button(self, text="Don't have an account ?", command=lambda: master.switch_frame(SignUpGUI)).grid(row = 7, column = 3)
        button3 = ttk.Button(self, text = "Press Me", command = master.displayUpgrade).grid(row = 8, column = 3)
        Log_In_button = ttk.Button(self, text = "Login", command =lambda: check_data(account_dict)).grid(row = 4, column = 3)
        
        ######################################################################################################
        
        
        
 
class UpgradeGUI(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='white')
        
        #image2 = Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg")
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label2 = ttk.Label(self, image = photo)
        label2.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label2.pack()
        
        tk.Label(self, text="Upgrade", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogInGUI)).pack()

class SignUpGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='white')
        
        
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Sign Up", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        ttk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogInGUI)).pack()

class WelcomeUser(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='white')
    
        
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Welcome " + global_username, font = ("Times New Roman", 24)).pack(side="top", fill="x", pady=5)
        self.after(3000, lambda: master.switch_frame(UserMenuGUI))
    

class UserMenuGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='white')
        
        
        photo = ImageTk.PhotoImage(Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="User Menu", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        ttk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogInGUI)).pack()




Cyber_Crop = CyberCrop()
Cyber_Crop.mainloop()
