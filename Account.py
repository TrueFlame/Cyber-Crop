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
    
    def ReturnPrivillege(self):
        pass
    def CheckPrivillege():
        pass
    def ChooseCategory():
        pass
    def CheckLogin():
        pass
    def CheckDatabase():
        pass
    

class Amateur(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str, username: str()): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
    account_privillege = 'Amateur' # static variable
    
    
class Business(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str, username : str): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
        self.username = username
    account_privillege = 'Business'
    '''
    def ReturnPrivillege(self):
        if self.account_privillege == "Business":
            print(True)
    '''
class Professional(Account):
    def __init__(self, FirstName: str , LastName: str, Certificate: str , BusinessName: str, e_mail: str, password: str, username: str): 
        super().__init__(FirstName, LastName, Certificate, BusinessName, e_mail, password)
        self.username = username
    account_privillege = 'Professional'

def ReturnPrivillege(business: Business):
        if business.account_privillege == "Business":
            print(True)


business1 = Business("Andrew", "oikonomou", "ok", "kati", "kati#gmail.com", "123456", "mounakias")

#business1.ReturnPrivillege()
account_dict = {}
account_dict[business1.username] = business1.password

#ReturnPrivillege(business1)

print(account_dict)

