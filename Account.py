import pickle
class Account:

    def __init__ (self, FirstName: str , LastName: str, username: str, e_mail: str, password: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.username = username
        self.e_mail = e_mail
        self.password = password

class Amateur(Account):
    def __init__(self, FirstName: str , LastName: str, username: str, e_mail: str, password: str, ): 
        super().__init__(FirstName, LastName,username, e_mail, password)
    account_privillege = 'Amateur' # static variable
    
    
class Business(Account):
    def __init__(self, FirstName: str , LastName: str,username: str, BusinessName: str, e_mail: str, password: str, Certificate = None): 
        super().__init__(FirstName, LastName, username, e_mail, password)
        self.BusinessName = BusinessName
    account_privillege = 'Business'
    
    def ReturnPrivillege(self):
        return self.account_privillege
    
class Professional(Account):
    def __init__(self, FirstName: str , LastName: str, username: str, e_mail: str, password: str, Certificate = None): 
        super().__init__(FirstName, LastName,username, e_mail, password)
    account_privillege = 'Professional'




###################################################




