import tkinter
from tkinter import ttk
from expanse import Expanse
from crop import Crop

class Account:

    def __init__ (self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Certificate = Certificate
        self.BusinessName = BusinessName
        self.e_mail = e_mail
        self.password = password
        
    def LogIn(e_mail,password):
        pass
    def SignUp(e_mail,password,FirstName,Certificate,BusinessName):
        pass
    def Upgrade(e_mail,password,FirstName,Certificate,BusinessName):
        pass
    
    def ReturnPrivillege():
        pass
    def CheckPrivillege():
        pass
 
crop10 = Crop(4, "type", "name", 5, "est_yield", "longitude", "latitude")

print(crop10.crop_id)


