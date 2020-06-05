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


business1 = Business("Andrew", "oikonomou", "ok", "kati", "kati#gmail.com", "123456", "makias")

#business1.ReturnPrivillege()
account_dict = {}
account_dict[business1.username] = business1.password

#ReturnPrivillege(business1)

print(account_dict)

with open('database.pkl', 'wb') as output:
    business2 = Business("Andrew", "oikonomou", "ok", "kati", "kati#gmail.com", "123456", "kati")
    pickle.dump(business2, output, pickle.HIGHEST_PROTOCOL)

    business3 = Business("Nikos", "Papanou", "ok", "kati", "kat78678678gmail.com", "123456", "katimou")
    pickle.dump(business3, output, pickle.HIGHEST_PROTOCOL)
    
    business4 = Business("Nikos", "Papanou", "okeydokey", "katitis", "kat78678678gmail.com", "123456", "katimou")
    pickle.dump(business4, output, pickle.HIGHEST_PROTOCOL)

with open('database.pkl', 'rb') as input:
    business2 = pickle.load(input)
    print(business1.password)  # -> banana
    print(business1.FirstName)  # -> 40

    business4 = pickle.load(input)
    print(business4.password) # -> spam
    print(business4.FirstName)  # -> 42
###################################################
'''
def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield dill.load(f)
            except EOFError:
                break
'''
with open("database.pkl", "rb") as data_file:
    data = []
    while True:
        try:
            data.append(pickle.load(data_file))
        except EOFError:
            break

for obj in data:
    obj.ReturnPrivillege()

#print(items)

#input_file = open("database.pkl", "rb")
#print(dill.load(input_file))
#ReturnPrivillege(business1)

#print(account_dict)
