import tkinter as tk
import pickle
import pathlib

#############################
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

##################

from Account import *
from Expanse import *

############################


def load_all(database):
    with open(database, "rb") as data_file:
        while True:
            try:
                yield pickle.load(data_file)
            except EOFError:
                break

def save_object(created_object):
    with open("database.pkl", "ab") as data_file:
        pickle.dump(created_object, data_file, pickle.HIGHEST_PROTOCOL)
        
#############################################################

class CyberCrop(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        
        self.characteristics()
        self.bind("<Escape>", self.exit_question)
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

    def exit_question(self, event):
        if tk.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.withdraw()
            self.destroy()
    
    def characteristics(self):
        self.resizable()
        self.title("Cyber Crop")
        self.geometry("1600x900")
        self.iconbitmap("logo.ico")
        self.configure(background = "white")
    
class LogInGUI(tk.Frame):
  
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, background = "white")
        
        master.title("Cyber Crop - Log In")
        
        ############ styles to be used with entries
        
        entry_style_black = ttk.Style()
        entry_style_black.configure("Black.TEntry", foreground = "black", background = "white")
        entry_style_grey = ttk.Style()
        entry_style_grey.configure("Grey.TEntry", foreground = "grey", background = "white")
        
        label_style = ttk.Style()
        label_style.configure("White.TLabel", background = "white")
        
        ################# make the text blink
        def on_entry_click_username(event):
            
            """function that gets called whenever entry is clicked"""
            if username.get() == 'Enter your username...':
                username.delete(0, "end") # delete all the text in the entry
                username.insert(0, '') #Insert blank for user input
                username.configure(style = "Black.TEntry")
        
        def on_focusout_username(event):
            if username.get() == '':
                username.insert(0, 'Enter your username...')
                username.configure(style = "Grey.TEntry")
                     
        def on_entry_click_password(event):
            
            """function that gets called whenever entry is clicked"""
            if password.get() == 'Enter your password...':
                password.delete(0, "end") # delete all the text in the entry
                password.insert(0, '') #Insert blank for user input
                password.configure(style = "Black.TEntry")
                
        def on_focusout_password(event):
            if password.get() == '':
                password.insert(0, 'Enter your password...')
                password.configure(style = "Black.TEntry")        
        
        ########################################################################

        def check_database():
            password_data = password.get()
            username_data = username.get()
            
            password.delete(0, "end")
            username.delete(0, "end")
            
            global global_username
            global global_privillege
            
            
            flag = False
            data_file = list(load_all("database.pkl"))
            
            #print(data_file)
            
            for obj in data_file:
                if username_data == obj.username and password_data == obj.password:
                    global_username = username_data
                    global_privillege = obj.account_privillege
                    master.switch_frame(WelcomeUser)
                    break
            else:
                flag = True
            if flag == True:
                master.displayUpgrade()

        
        # logo
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = "N"+"W"+"E"+"S" )
        
        label1.configure(bg = "white")
        
        # Entries
        ##################
        
        
        username = ttk.Entry(self, width = 30, background = "white")
        username.grid(row = 4, column = 2, padx = 30)
        username.insert(0, "Enter your username...")
        
        username.bind('<FocusIn>', on_entry_click_username)
        username.bind('<FocusOut>', on_focusout_username)
        username.configure(style = "Black.TEntry")
        
        ########################
        
        password = ttk.Entry(self, width = 30, show = "*")
        password.grid(row = 6, column = 2, padx = 30)
        password.insert(0, "Enter your password...")
        
        password.bind('<FocusIn>', on_entry_click_password)
        password.bind('<FocusOut>', on_focusout_password)
        
        
        ############################
        #label2 = tk.Label(self, text="Log In ", font=('Helvetica', 32, "bold")).grid(row = 2 , column = 2)
        
        #Labels
        username_label = ttk.Label(self, text = "Username:")
        password_label = ttk.Label(self, text = "Password:")
        
        username_label.configure(style = "White.TLabel")
        password_label.configure(style = "White.TLabel")
        
        username_label.grid(row = 4, column = 1)
        password_label.grid(row = 6, column = 1)
        
        
        # Buttons - Log In
        
        button2 = ttk.Button(self, text="Don't have an account ?", command=lambda: master.switch_frame(SignUpGUI)).grid(row = 7, column = 3)
        button3 = ttk.Button(self, text = "Press Me", command = master.displayUpgrade).grid(row = 8, column = 3)
        Log_In_button = ttk.Button(self, text = "Login", command = check_database).grid(row = 4, column = 3)
        
        ######################################################################################################
        
        tk.Label(self, text="Log In", font=('Helvetica', 30, "bold"), background = "white").grid(row = 1, column = 2 , pady=10, padx = 10, sticky = "E")

class UpgradeGUI(tk.Frame):
    
    def __init__(self, master):
        
        def upgrade_account():
            data_file = list(load_all("database.pkl"))
            
            index = 0
            up_password = ""
            up_e_mail = ""
            up_firstname = ""
            up_lastname = ""
            up_business_name = bus_name.get()
            up_choice = upgrade_choice.get()
            
            for i, obj in enumerate(data_file):
                if obj.username == global_username:
                    up_password = obj.password
                    up_e_mail = obj.e_mail
                    up_firstname = obj.FirstName
                    up_lastname = obj.LastName
                    index = i
                    break
            
            if up_choice == "Professional":
                upgraded_account = Professional(up_firstname, up_lastname, global_username, up_e_mail, up_password)
                
            elif up_choice == "Business":
                upgraded_account = Business(up_firstname, up_lastname, global_username, up_business_name, up_e_mail, up_password)
            
            del data_file[index]
            data_file.append(upgraded_account)
            
            for account in data_file:
                with open("database.pkl", "wb") as database:
                    pickle.dump(account, database, pickle.HIGHEST_PROTOCOL)
            
            master.switch_frame(SuccessfulUpgrade)

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, background='white')
        
        master.title("Cyber Crop - Account Upgrade")
        
        #image2 = Image.open("bca8e31f-f7c7-4a24-9fac-5ee24e7f56d4_200x200.jpg")
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label2 = tk.Label(self, image = photo, background = "white")
        label2.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label2.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10, sticky = "N"+"W"+"E"+"S" )
        
        tk.Label(self, text = "Choose from the available choices to upgrade to: ", background = "white", font = ("Arial", 14, "bold") ).grid(row = 5, column = 0, padx = 5, pady = 5, sticky = tk.E)
        
        upgrade_choice = tk.StringVar()
        
        R4 = ttk.Radiobutton(self, text = "Professional", variable = upgrade_choice, value = "Professional")
        R5 = ttk.Radiobutton(self, text = "Business", variable = upgrade_choice, value = "Business")
        
        tk.Label(self, text = "Business Name :", background = "white").grid(row = 7, column = 0)
        bus_name = tk.Entry(self, text = "Insert business name...", background = "white", width = 30)
        bus_name.grid(row = 7, column = 1, padx = 5, pady = 5, sticky = tk.E)
        
        if global_privillege == "Professional":
            R4.configure(state = "disabled")
        
        R4.grid(row = 4, column = 1, padx = 5, pady = 5)
        R5.grid(row = 6, column = 1, padx = 5, pady = 5)
        
        tk.Label(self, text="Upgrade", font=('Helvetica', 24, "bold"), background = "white").grid(row = 1, column = 0 , pady=10, padx = 10, sticky = "E")
        ttk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogInGUI)).grid(row = 7, column = 4)
        
        upgrade_button = ttk.Button(self, text = "Upgrade Account", command = upgrade_account).grid(row = 8, column = 4, padx = 5, pady = 5)
       

            
class SignUpGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background = 'white')
        
        ######### title
        master.title("Cyber Crop - Sign Up")

        ########################## list of styles
        entry_style_black = ttk.Style()
        entry_style_black.configure("Black.TEntry", foreground = "black", background = "white")
        entry_style_grey = ttk.Style()
        entry_style_grey.configure("Grey.TEntry", foreground = "grey", background = "white")        


        label_style = ttk.Style()
        label_style.configure("White.TLabel", background = "white")
        
        ######################## used for blinking entries ###############################################################
        def on_entry_click_s_username(event):
            
            """function that gets called whenever entry is clicked"""
            if s_username.get() == 'Username...':
                s_username.delete(0, "end") # delete all the text in the entry
                s_username.insert(0, '') #Insert blank for user input
                s_username.configure(style = "Black.TEntry")
        
        def on_focusout_s_username(event):
            if s_username.get() == '':
                s_username.insert(0, 'Username...')
                      
        def on_entry_click_s_password(event):
            
            """function that gets called whenever entry is clicked"""
            if s_password.get() == 'Password...':
                s_password.delete(0, "end") # delete all the text in the entry
                s_password.insert(0, '') #Insert blank for user input
                s_password.configure(style = "Black.TEntry")
        
        def on_focusout_s_password(event):
            if s_password.get() == '':
                s_password.insert(0, 'Password...')
                s_password.configure(style = "Black.TEntry") 

        def on_entry_click_s_firstname(event):
            
            """function that gets called whenever entry is clicked"""
            if s_firstname.get() == 'First name...':
                s_firstname.delete(0, "end") # delete all the text in the entry
                s_firstname.insert(0, '') #Insert blank for user input
                s_firstname.configure(style = "Black.TEntry")
        
        def on_focusout_s_firstname(event):
            if s_firstname.get() == '':
                s_firstname.insert(0, 'First name...')
                
                     
        def on_entry_click_s_lastname(event):
            """function that gets called whenever entry is clicked"""
            if s_lastname.get() == 'Last name...':
                s_lastname.delete(0, "end") # delete all the text in the entry
                s_lastname.insert(0, '') #Insert blank for user input
                s_lastname.configure(style = "Black.TEntry")
                
        def on_focusout_s_lastname(event):
            if s_lastname.get() == '':
                s_lastname.insert(0, 'Last name...')
                s_lastname.configure(style = "Black.TEntry")
        
        def on_entry_click_s_email(event):
            
            """function that gets called whenever entry is clicked"""
            if s_email.get() == 'Email...':
                s_email.delete(0, "end") # delete all the text in the entry
                s_email.insert(0, '') #Insert blank for user input
                s_email.configure(style = "Black.TEntry")
                
        def on_focusout_s_email(event):
            if s_email.get() == '':
                s_email.insert(0, 'Email...')
                s_email.configure(style = "Black.TEntry") 
        
        def on_entry_click_s_bus_name(event):
            
            """function that gets called whenever entry is clicked"""
            if s_business_name.get() == 'Complete only if you select Business...':
                s_business_name.delete(0, "end") # delete all the text in the entry
                s_business_name.insert(0, '') #Insert blank for user input
                s_business_name.configure(style = "Black.TEntry")
                
        def on_focusout_s_bus_name(event):
            if s_business_name.get() == '':
                s_business_name.insert(0, 'Complete only if you select Business...')
                s_business_name.configure(style = "Black.TEntry")
        
        ################ function that creates account and stores in the database file ############################
        
        def create_account():
            new_username = s_username.get()
            new_password = s_password.get()
            new_firstname = s_firstname.get()
            new_lastname = s_lastname.get()
            new_email = s_email.get()
            new_bus_name = s_business_name.get()
            acc_choice = choice.get()
            
            #print(acc_choice)

            print(new_username, new_password)
            
            if acc_choice == "Amateur":
                new_account = Amateur(new_firstname, new_lastname, new_username, new_email, new_password)
                with open("database.pkl", "ab") as data_file:
                    pickle.dump(new_account, data_file, pickle.HIGHEST_PROTOCOL)

            elif acc_choice == "Professional":
                new_account = Professional(new_firstname, new_lastname, new_username, new_email, new_password)
                with open("database.pkl", "ab") as data_file:
                    pickle.dump(new_account, data_file, pickle.HIGHEST_PROTOCOL)
                    
            elif acc_choice == "Business":
                new_account = Business(new_username, new_lastname, new_username, new_bus_name, new_email, new_password)
                with open("database.pkl", "ab") as data_file:
                    pickle.dump(new_account, data_file, pickle.HIGHEST_PROTOCOL)
        
            master.switch_frame(SuccessfulSignUp)
            
        ################################ image#######################
        
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        image_label = tk.Label(self, image = photo)
        image_label.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        image_label.grid(row = 0, column = 0, columnspan = 4)
        image_label.configure(background = "white")
        
        ###################### info Labels
        
        tk.Label(self, text="Sign Up", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 1,padx = 5, pady=5, sticky = "E")
        username_label = tk.Label(self, text = "Username: ", background = "white")
        password_label = tk.Label(self, text = "Password: ", background = "white")
        fname_label = tk.Label(self, text = "Firstname: ", background = "white")
        lnmae_label = tk.Label(self, text = "Lastname: ", background = "white")
        mail_label = tk.Label(self, text = "E-mail: ", background = "white")
        busi_name_label = tk.Label(self, text = "Business Name: ", background = "white")
        
        username_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.E)
        password_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.E)
        fname_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.E)
        lnmae_label.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = tk.E)
        mail_label.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = tk.E)
        busi_name_label.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = tk.E)
        
        ####################### info Entries
        
        s_username = ttk.Entry(self, width = 20)
        s_password = ttk.Entry(self, width = 20)        
        s_firstname = ttk.Entry(self, width = 20)
        s_lastname = ttk.Entry(self, width = 20)
        s_email = ttk.Entry(self, width = 20) 
        s_business_name = ttk.Entry(self, width = 30)
        
        #### radio button check like in mockup
        
        choice = tk.StringVar()
        
        R1 = ttk.Radiobutton(self, text = "Amateur", variable = choice, value = "Amateur")
        R2 = ttk.Radiobutton(self, text = "Professional", variable = choice, value = "Professional")
        R3 = ttk.Radiobutton(self, text = "Business", variable = choice, value = "Business")
        
        radio_label = ttk.Label(self, text = "Choose type of account: ")
        radio_label.configure(style = "White.TLabel")
        radio_label.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = tk.E)
        
        R1.grid(row = 8, column = 1, padx = 5, pady = 5)
        R2.grid(row = 9, column = 1, padx = 5, pady = 5)
        R3.grid(row = 10, column = 1, padx = 5, pady = 5)
       
        ################ put entries on the grid
        
        s_username.grid(row = 2, column = 1, padx = 30)
        s_password.grid(row = 3, column = 1, padx = 30)
        s_firstname.grid(row = 4, column = 1, padx = 30)
        s_lastname.grid(row = 5, column = 1, padx = 30)
        s_email.grid(row = 6, column = 1, padx = 30)
        s_business_name.grid(row = 7, column = 1, padx = 30)
        
        ############################### entries - default inserts
        
        s_username.insert(0, "Username...")
        s_username.bind('<FocusIn>', on_entry_click_s_username)
        s_username.bind('<FocusOut>', on_focusout_s_username)
        s_username.configure(style = "Black.TEntry")
        
        s_password.insert(0, "Password...")
        s_password.bind("<FocusIn>", on_entry_click_s_password)
        s_password.bind("<FocusOut>", on_focusout_s_password)
        s_password.configure(style = "Black.TEntry")
        
        s_firstname.insert(0, "First name...")
        s_firstname.bind("<FocusIn>", on_entry_click_s_firstname)
        s_firstname.bind("<FocusOut>", on_focusout_s_firstname)
        s_firstname.configure(style = "Black.TEntry")
        
        s_lastname.insert(0, "Last name...")
        s_lastname.bind("<FocusIn>", on_entry_click_s_lastname)
        s_lastname.bind("<FocusOut>", on_focusout_s_lastname)
        s_lastname.configure(style = "Black.TEntry")
        
        
        s_email.insert(0, "Email...")
        s_email.bind("<FocusIn>", on_entry_click_s_email)
        s_email.bind("<FocusOut>", on_focusout_s_email)
        s_email.configure(style = "Black.TEntry")
        
        s_business_name.insert(0, "Complete only if you select Business...")
        s_business_name.bind("<FocusIn>", on_entry_click_s_bus_name)
        s_business_name.bind("<FocusOut>", on_focusout_s_bus_name)
        s_business_name.configure(style = "Black.TEntry")
        
        ttk.Button(self, text = "Sign Up", command = create_account).grid(row = 8, column = 4)
        ttk.Button(self, text="Return to Log In", command=lambda: master.switch_frame(LogInGUI)).grid(row = 9, column = 4)

################################### Frames that are used for moving ###################################
class WelcomeUser(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
    
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Welcome " + global_username, font = ("Times New Roman", 24), background = "white").pack(side="top", fill="x", pady=5)
        self.after(1200, lambda: master.switch_frame(UserMenuGUI))


class SuccessfulSignUp(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
    
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Successful Sign-up", font = ("Times New Roman", 24), background = "white").pack(side="top", fill="x", pady=5)
        self.after(1200, lambda: master.switch_frame(LogInGUI))


class SuccessfulUpgrade(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
    
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Successful Upgrade", font = ("Times New Roman", 24), background = "white").pack(side="top", fill="x", pady=5)
        self.after(1200, lambda: master.switch_frame(LogInGUI))

class SuccessfulAdd(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
    
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.pack()
        
        tk.Label(self, text="Successfully Added", font = ("Times New Roman", 24), background = "white").pack(side="top", fill="x", pady=5)
        self.after(1200, lambda: master.switch_frame(ExpanseGUI))

###################################################################################
class UserMenuGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - User Menu")
        
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = ttk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1)
        
        tk.Label(self, text="User Menu", font=('Helvetica', 18, "bold"), background = "white").grid(row = 1, column = 1 , pady=5, padx = 5)
        ttk.Button(self, text="Go back to Log In", command=lambda: master.switch_frame(LogInGUI)).grid(row = 2, column = 0, sticky = tk.E)
        ttk.Button(self, text = "Customer Support", command = lambda: master.switch_frame(CustomerSupportGUI)).grid(row = 3, column = 0)
        
        butt_upgrade = ttk.Button(self, text="Upgrade", command=lambda: master.switch_frame(UpgradeGUI))
        butt_upgrade.grid(row = 5, column = 0)
        
        butt_expanse = ttk.Button(self, text = "Expanse", command = lambda: master.switch_frame(ExpanseGUI))
        butt_expanse.grid(row = 4, column = 0)
        
        if global_privillege == "Business":
            butt_upgrade.configure(state = "disabled")
        
class CustomerSupportGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - Customer Support")
        
        ######################## notebook style
        
        nb_style_white = ttk.Style()
        nb_style_white.configure("White.TNotebook", background = "white")
        
        
        ################ image
        
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, padx = 10, pady = 10)
        label1.configure(background = "white")
        
        customer_support_notebook = ttk.Notebook(self)
        customer_support_notebook.configure(style = "White.TNotebook")
        customer_support_notebook.grid(row = 2, column = 1)
        
        ####################### telephone tab
        telephone_frame = tk.Frame(customer_support_notebook, width = 200, height = 80)
        telephone_frame.configure(background = "white")
        customer_support_notebook.add(telephone_frame, text = "Telephones")
        
        
        telephone1 = tk.Label(telephone_frame, text = " Telephone 1 : 2610 524 985")
        telephone1.configure(background = "white")
        telephone1.pack(side = "top", fill = "x", padx = 10, pady = 10)
        
        telephone2 = tk.Label(telephone_frame, text = "Telephone 2 : 210 9875 099")
        telephone2.configure(background = "white")
        telephone2.pack(side = "top", fill = "x", padx = 10, pady = 10)
        
        telephone3 = tk.Label(telephone_frame, text = "Telephone 3 : +30 6984 344 766")
        telephone3.configure(background = "white")
        telephone3.pack(side = "top", fill = "x", padx = 10, pady = 10)
        
        ######################################### email tab
        email_frame = tk.Frame(customer_support_notebook, width = 300, height = 405)
        email_frame.configure(background = "white")
        customer_support_notebook.add(email_frame, text = "E-mail")
        
        mail_window = tk.Text(email_frame)
        mail_window.pack(side = "top")
        
        send_mail = ttk.Button(email_frame, text = "Send")
        send_mail.pack(side = "right", fill = "x")
        
        if global_privillege == "Amateur":
            customer_support_notebook.tab(1, state = "disabled")
        
        ######################################### live chat tab
        live_chat = tk.Frame(customer_support_notebook, width = 240, height = 120)
        customer_support_notebook.add(live_chat, text = "Live Chat")
        
        if global_privillege == "Amateur":
            customer_support_notebook.tab(2, state = "disabled")
        
        if global_privillege == "Amateur":
            tk.Label(self, text = " Email and live chat are unavailable in the Amateur version.", background = "white", font = ("Arial",18, "bold")).grid(row = 3, column = 1)
        
        tk.Label(self, text="Customer Support", font=('Helvetica', 18, "bold"), background = "white").grid(row = 1, column = 1, pady=5, padx = 5)
        ttk.Button(self, text="Go back to User Menu", command=lambda: master.switch_frame(UserMenuGUI)).grid(row = 2, column = 2, padx = 5, pady = 5)


class ExpanseGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - Expanse Options")
        
        
        ################ image
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 2, padx = 5, pady = 5)
        label1.configure(background = "white")
        
        tk.Label(self, text="Expanse Options", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 2,padx = 5, pady=5)
        
        ttk.Button(self, text = "Add Expanse", command = lambda: master.switch_frame(AddExpanseGUI)).grid(row = 2, column = 1, padx = 5, pady = 5)
        crop_add = ttk.Button(self, text = "Add Crop", command = lambda: master.switch_frame(AddCropGUI))
        photo_add = ttk.Button(self, text = "Add Photovoltaic", command = lambda: master.switch_frame(AddPhotovoltaicGUI))
        
        crop_add.grid(row = 2, column = 2, padx = 5, pady = 5)
        photo_add.grid(row = 2, column = 3, padx = 5, pady = 5)
        ttk.Button(self, text="Go back to User Menu", command=lambda: master.switch_frame(UserMenuGUI)).grid(row = 5, column = 5, padx = 5, pady = 5)
        
        ################## check if file exists, if not create it
        file = pathlib.Path("areas_database.pkl")
        
        if not file.exists():
            open('areas_database.pkl', 'w+')
        ##############################################3
        
        data_file = list(load_all("areas_database.pkl"))
        i = 0
        for ob in data_file:
            if isinstance(ob, Expanse):
                if global_username == ob.owner_username:
                    i += 1
        if i == 0:
            crop_add.configure(state = "disabled")
            photo_add.configure(state = "disabled")
        ###################################################

class AddExpanseGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - Add Expanse")
        
        entry_style_black = ttk.Style()
        entry_style_black.configure("Black.TEntry", foreground = "black", background = "white")
        entry_style_grey = ttk.Style()
        entry_style_grey.configure("Grey.TEntry", foreground = "grey", background = "white")
        
        #################################### add expanse
        def add_expanse():
            new_size = size_entry.get()
            new_longitude = long_entry.get()
            new_latitude = lat_entry.get()
            new_owner_username = global_username
            new_exp_id = 1
            
            file = pathlib.Path("areas_database.pkl")
            
            
            
            if file.exists():
                data_file = list(load_all("areas_database.pkl"))
                for ob in data_file:
                    if isinstance(ob, Expanse):
                        if global_username == ob.owner_username:
                            new_exp_id += 1
            
            new_expanse = Expanse(global_username, new_exp_id, new_size, new_longitude, new_latitude)
            with open("areas_database.pkl", "ab") as data_file:
                pickle.dump(new_expanse, data_file, pickle.HIGHEST_PROTOCOL)
            
            master.switch_frame(SuccessfulAdd)

        ############################# make entries blinking
        
        def on_entry_click_size(event):
            
            """function that gets called whenever entry is clicked"""
            if size_entry.get() == 'Size...':
                size_entry.delete(0, "end") # delete all the text in the entry
                size_entry.insert(0, '') #Insert blank for user input
                size_entry.configure(style = "Black.TEntry")
        
        def on_focusout_size(event):
            if size_entry.get() == '':
                size_entry.insert(0, 'Size...')
                      
        def on_entry_click_longitude(event):
            
            """function that gets called whenever entry is clicked"""
            if long_entry.get() == 'Longitude...':
                long_entry.delete(0, "end") # delete all the text in the entry
                long_entry.insert(0, '') #Insert blank for user input
                long_entry.configure(style = "Black.TEntry")
        
        def on_focusout_longitude(event):
            if long_entry.get() == '':
                long_entry.insert(0, 'Longitude...')
                long_entry.configure(style = "Black.TEntry") 

        def on_entry_click_latitude(event):
            
            """function that gets called whenever entry is clicked"""
            if lat_entry.get() == 'Latitude...':
                lat_entry.delete(0, "end") # delete all the text in the entry
                lat_entry.insert(0, '') #Insert blank for user input
                lat_entry.configure(style = "Black.TEntry")
        
        def on_focusout_latitude(event):
            if lat_entry.get() == '':
                lat_entry.insert(0, 'Latitude...')
        
        ################ image
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 5)
        label1.configure(background = "white")
        
        ############################# entry labels
        
        size_label = tk.Label(self, text = "Size: ", background = "white")
        long_label = tk.Label(self, text = "Longitude: ", background = "white")
        lat_label = tk.Label(self, text = "Latitude: ", background = "white")
        
        
        size_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.E)
        long_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.E)
        lat_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.E)
        
        
        
        ####################### info Entries
        
        size_entry = ttk.Entry(self, width = 20)
        long_entry = ttk.Entry(self, width = 20)        
        lat_entry = ttk.Entry(self, width = 20)
        
        size_entry.grid(row = 2, column = 1, padx = 30)
        long_entry.grid(row = 3, column = 1, padx = 30)
        lat_entry.grid(row = 4, column = 1, padx = 30)
        
        size_entry.insert(0, "Size...")
        size_entry.bind('<FocusIn>', on_entry_click_size)
        size_entry.bind('<FocusOut>', on_focusout_size)
        size_entry.configure(style = "Black.TEntry")
        
        long_entry.insert(0, "Longitude...")
        long_entry.bind("<FocusIn>", on_entry_click_longitude)
        long_entry.bind("<FocusOut>", on_focusout_longitude)
        long_entry.configure(style = "Black.TEntry")
        
        lat_entry.insert(0, "Latitude...")
        lat_entry.bind("<FocusIn>", on_entry_click_latitude)
        lat_entry.bind("<FocusOut>", on_focusout_latitude)
        lat_entry.configure(style = "Black.TEntry")
        
        tk.Label(self, text="Add Expanse", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 1, padx = 5, pady=5, sticky = tk.E)
        ttk.Button(self, text = "Add Expanse", command = add_expanse).grid(row = 5, column = 1, padx = 5, pady = 5)

class AddCropGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - Add Crop")
        
        
        ################### entries styles
        
        entry_style_black = ttk.Style()
        entry_style_black.configure("Black.TEntry", foreground = "black", background = "white")
        entry_style_grey = ttk.Style()
        entry_style_grey.configure("Grey.TEntry", foreground = "grey", background = "white")
        
        ############################# make entries blinking
        
        def on_entry_click_size(event):
            
            """function that gets called whenever entry is clicked"""
            if size_entry.get() == 'Crop size...':
                size_entry.delete(0, "end") # delete all the text in the entry
                size_entry.insert(0, '') #Insert blank for user input
                size_entry.configure(style = "Black.TEntry")
        
        def on_focusout_size(event):
            if size_entry.get() == '':
                size_entry.insert(0, 'Crop size...')
                      
        def on_entry_click_crop_name(event):
            
            """function that gets called whenever entry is clicked"""
            if crop_name_entry.get() == "Give a name for your crop...":
                crop_name_entry.delete(0, "end") # delete all the text in the entry
                crop_name_entry.insert(0, '') #Insert blank for user input
                crop_name_entry.configure(style = "Black.TEntry")
        
        def on_focusout_crop_name(event):
            if crop_name_entry.get() == '':
                crop_name_entry.insert(0, "Give a name for your crop...")
                crop_name_entry.configure(style = "Black.TEntry") 

        def on_entry_click_est_yield(event):
            
            """function that gets called whenever entry is clicked"""
            if est_yield_entry.get() == "Give an estimation of your yield...":
                est_yield_entry.delete(0, "end") # delete all the text in the entry
                est_yield_entry.insert(0, '') #Insert blank for user input
                est_yield_entry.configure(style = "Black.TEntry")
        
        def on_focusout_est_yield(event):
            if est_yield_entry.get() == '':
                est_yield_entry.insert(0, "Give an estimation of your yield...")
        
        
        def add_crop():
            
            crop_name_data = crop_name_entry.get()
            size_data = size_entry.get()
            est_yield_data = est_yield_entry.get()
            
            exp_id_choice = expanse_select_option.get()
            crop_type_choice = crop_types.get()
            
            new_latitude = 0.0
            new_longitude = 0.0
            
            data_file = list(load_all("areas_database.pkl"))
            
            for ob in data_file:
                if isinstance(ob, Expanse):
                    if global_username == ob.owner_username and exp_id_choice == ob.exp_id:
                        new_latitude = ob.latitude
                        new_longitude = ob.longitude
            
            new_counter_id = 1
            for ob in data_file:
                if isinstance(ob, Crop):
                    if global_username == ob.owner_username:
                        new_counter_id += 1
            
            new_crop = Crop(new_counter_id, crop_type_choice, crop_name_data, est_yield_data, size_data, new_longitude, new_latitude, exp_id_choice, global_username)
            
            with open("areas_database.pkl", "ab") as data_file:
                pickle.dump(new_crop, data_file, pickle.HIGHEST_PROTOCOL)
            
            master.switch_frame(SuccessfulAdd)
        
        ################ image
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, padx = 5, pady = 5)
        label1.configure(background = "white")
        
        
        tk.Label(self, text="Add Crop", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.E)
        expanse_select_label = tk.Label(self, text = "Select expanse to add crop to: ", background = "white")
        crop_types_label = tk.Label(self, text = "Select Crop type: ", background = "white")
        crop_name_label = tk.Label(self, text = "Name your Crop: ", background = "white")
        est_yield_label = tk.Label(self, text = "Give estimation of crop yield: ", background = "white")
        size_label = tk.Label(self, text = "Give crop area size: ", background = "white")
        
        expanse_select_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.E)
        crop_types_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.E)
        crop_name_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.E)
        est_yield_label.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = tk.E)
        size_label.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = tk.E)
        ########################## find available expanses to add crops and option menus
        
        data_file = list(load_all("areas_database.pkl"))
        available_expanses_id = []
        
        for ob in data_file:
            if isinstance(ob, Expanse):
                if global_username == ob.owner_username:
                    available_expanses_id.append(ob.exp_id)
        
        
        crop_available_options =["Strawberry", "Orange", "Eggplant"]
        
        crop_types = tk.StringVar() ## to get available crops from optionmenu1
        expanse_select_option = tk.IntVar() # to get available expanse id from optionmenu2
        
        crop_types.set(crop_available_options[0])
        expanse_select_option.set(available_expanses_id[0])
        
        crop_optionmenu = ttk.OptionMenu(self, crop_types, *crop_available_options)
        expanse_selection_menu = ttk.OptionMenu(self, expanse_select_option, *available_expanses_id)
        
        crop_optionmenu.grid(row = 3, column = 1, padx = 5, pady = 5)
        expanse_selection_menu.grid(row = 2, column = 1, padx = 5, pady = 5)
        
        ################### entries
        crop_name_entry = ttk.Entry(self, width = 25)
        est_yield_entry = ttk.Entry(self, width = 25)
        size_entry = ttk.Entry(self, width = 25)
        
        crop_name_entry.grid(row = 4, column = 1)
        est_yield_entry.grid(row = 5, column = 1)
        size_entry.grid(row = 6, column = 1)
        
        crop_name_entry.insert(0, "Give a name for your crop...")
        crop_name_entry.bind('<FocusIn>', on_entry_click_crop_name)
        crop_name_entry.bind('<FocusOut>', on_focusout_crop_name)
        crop_name_entry.configure(style = "Black.TEntry")
        
        est_yield_entry.insert(0, "Give an estimation of your yield...")
        est_yield_entry.bind("<FocusIn>", on_entry_click_est_yield)
        est_yield_entry.bind("<FocusOut>", on_focusout_est_yield)
        est_yield_entry.configure(style = "Black.TEntry")
        
        size_entry.insert(0, "Crop size...")
        size_entry.bind('<FocusIn>', on_entry_click_size)
        size_entry.bind('<FocusOut>', on_focusout_size)
        size_entry.configure(style = "Black.TEntry")
        
        ttk.Button(self, text = "Add Crop", command = add_crop).grid(row = 9, column = 1, padx = 5, pady = 5)
        
class AddPhotovoltaicGUI(tk.Frame):
    
    def __init__(self, master):  
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,background='white')
        
        master.title("Cyber Crop - Add Photovoltaic")
        
        
        def on_entry_click_photovoltaic_size(event):
            
            """function that gets called whenever entry is clicked"""
            if size_entry.get() == 'Photovoltaic size...':
                size_entry.delete(0, "end") # delete all the text in the entry
                size_entry.insert(0, '') #Insert blank for user input
                size_entry.configure(style = "Black.TEntry")
        
        def on_focusout_photovoltaic_size(event):
            if size_entry.get() == '':
                size_entry.insert(0, 'Photovoltaic size...')
                      
        def on_entry_click_est_production(event):
            
            """function that gets called whenever entry is clicked"""
            if est_production_entry.get() == "Give an estimation of your production...":
                est_production_entry.delete(0, "end") # delete all the text in the entry
                est_production_entry.insert(0, '') #Insert blank for user input
                est_production_entry.configure(style = "Black.TEntry")
        
        def on_focusout_est_production(event):
            if est_production_entry.get() == '':
                est_production_entry.insert(0, "Give an estimation of your production...")
                est_production_entry.configure(style = "Black.TEntry") 
        
        
        
        ################### entries styles
        
        entry_style_black = ttk.Style()
        entry_style_black.configure("Black.TEntry", foreground = "black", background = "white")
        entry_style_grey = ttk.Style()
        entry_style_grey.configure("Grey.TEntry", foreground = "grey", background = "white")
        
        
        ################ image
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, padx = 5, pady = 5)
        label1.configure(background = "white")
        
        ###################################################### labels
        
        tk.Label(self, text="Add Photovoltaic", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.E)
        expanse_select_label = tk.Label(self, text = "Select expanse to add photovoltaic to: ", background = "white")
        photo_type_label = tk.Label(self, text = "Select photovoltaic type: ", background = "white")
        est_production_label = tk.Label(self, text = "Give photovoltaic estimated production: ", background = "white")
        size_label = tk.Label(self, text = "Give photovoltaic area size: ", background = "white")
        
        ################### entries
        est_production_entry = ttk.Entry(self, width = 25)
        size_entry = ttk.Entry(self, width = 25)
        
        est_production_entry.grid(row = 5, column = 1)
        size_entry.grid(row = 6, column = 1)
        
        ### model and type will be from list for an option menu, so we will three option menus , one for expanse select, one for model and one for type
        
        data_file = list(load_all("areas_database.pkl"))
        available_expanses_id = []
        
        for ob in data_file:
            if isinstance(ob, Expanse):
                if global_username == ob.owner_username:
                    available_expanses_id.append(ob.exp_id)
        
        photovoltaic_types_options = ["Monocrystalline silicon", "Amorphous silicon", "Polymer and organic"]
        
        
        photo_types_choice = tk.StringVar() ## to get available crops from optionmenu1
        expanse_select_option = tk.IntVar()
        
        photo_types_choice.set(photovoltaic_types_options[0])
        expanse_select_option.set(available_expanses_id[0])
        
        photovoltaic_type_optionmenu = ttk.OptionMenu(self, photo_types_choice, *photovoltaic_types_options)
        expanse_selection_menu = ttk.OptionMenu(self, expanse_select_option, *available_expanses_id)
        
        photovoltaic_type_optionmenu.grid(row = 3, column = 1, padx = 5, pady = 5)
        expanse_selection_menu.grid(row = 2, column = 1, padx = 5, pady = 5)
        
        est_production_entry.insert(0, "Give an estimation of your production...")
        est_production_entry.bind("<FocusIn>", on_entry_click_est_yield)
        est_production_entry.bind("<FocusOut>", on_focusout_est_yield)
        est_production_entry.configure(style = "Black.TEntry")
        
        size_entry.insert(0, "Photovoltaic size...")
        size_entry.bind('<FocusIn>', on_entry_click_size)
        size_entry.bind('<FocusOut>', on_focusout_size)
        size_entry.configure(style = "Black.TEntry")
        
        
        
        tk.Label(self, text="Add Photovoltaic", font=('Helvetica', 28, "bold"), background = "white").grid(row = 1, column = 1,padx = 5, pady=5, sticky = tk.E)
if __name__ == '__main__':
    CyberCrop().mainloop()

