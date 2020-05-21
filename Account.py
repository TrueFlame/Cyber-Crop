import tkinter
from tkinter import ttk


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
    
 
 

class Amateur(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
        self.account_privillege = 'Amateur' # static variable
    
class Professional(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
        self.account_privillege = 'Professional'
    
class Business(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
        self.account_privillege = 'Business'
    
    
    
business1 = Business("andreoulis1996@gmail,com", "Adr5njbfas", "FirstName", "LastName", "Certificate", "BusinessName")
print(business1.account_privillege)
