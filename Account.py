class Account:
    def __init__(self, FirstName, LastName, Certificate, BusinessName, e-mail, password):
    self.FirstName = FirstName
    self.LastName = LastName
    self.Certificate = Certificate
    self.BusinessName = BusinessName
    self.e-mail = e-mail
    self.password = password
    
    
    def LogIn(e-mail,password):
    def SignUp(e-mail,passowrd,FirstName,Certificate,BusinessName):
    def Upgrade(e-mail,passowrd,FirstName,Certificate,BusinessName):
    
    
 
 

class Amateur(Account):
    def __init__(self, e-mail, password, FirstName, LastName) : super().init(e-mail,password,FirstName,LastName)
        account_privillege = 'Amateur' # static variable
    
class Professional(Account):
    def __init__(self, e-mail, password, FirstName, LastName, Certificate) : super().init(e-mail,password,FirstName,LastName,Certificate)
    account_privillege = 'Professional'
    
class Business(Account):
    def __init__(self, e-mail, password, FirstName, LastName, Certificate, BusinessName) : super().init(e-mail,password,FirstName,LastName,Certificate,BusinessName)
                
    account_privillege = 'Business'
