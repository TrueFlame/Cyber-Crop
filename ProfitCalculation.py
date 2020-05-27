from UserMenu import *
from tkinter import *
from PIL import Image, ImageTk
from array import *

class ProfitCalculation(): #Χρειάζεται εισαγωγή δεδομένων από Account και Expanse
    def __init__(self, CountryID, CurrencyID, Parameters):
        self.CountryID=CountryID
        self.Currency=CurrencyID
        self.Parameters=Parameters
		
        Country=[
                "USA",
                "Germany",
                "France",
                "Greece",
                "Russia",
                "China"
                ]
        
        Currency=[
                "EUR",
                "USD",
                "CNY"
                ]
        
        #dummy dedomena-------------------------------------------
        CropSale1=[[0, 200], [1,100], [2, 50], [3,60]]#country that buys + price per ton
        CropSale2=[[3, 20], [2, 50], [1,60]]
        CropSale3=[[3, 20], [1,10], [2, 5], [3,6]]
        
        
    def ChooseOption(): #Συνάρτηση διαχειρίζεται τις επιλογές του χρήστη apo gui
        '''
        # logo apo user menu class
        photo = ImageTk.PhotoImage(Image.open("logo.png"))
        label1 = tk.Label(self, image = photo)
        label1.image = photo # εχει προβληματα με το garbage disposal και γιαυτο κραταμε μια αναφορα στην εικόνα
        label1.grid(row = 0, column = 1, columnspan = 6)
        '''
        
        CalcWin= Tk()
        CalcWin.title("Profit Calculation")
        CalcWin.iconbitmap("Logo.png")
        CalcWin.geometry("640x480")
       
        #Drop Down Box
        options=[
                "Profit Calculation", 
                "Automatic Calculation"
                ]      
        click = StringVar()
        click.set(options[0])
        
        drop= OptionMenu(CalcWin, click, *options)
        drop.pack()
        pass
   
    
    def ChooseParameters(CountryID,CurrencyID): #Επιλογή χώρας πώλησης και νομίσματος apo gui
        ChosenCount=index("CountryID") #metatroph sto antistoixo id ths listas
        ChosenCurr=index("CurrencyID")
        Parameters=[ChosenCount,ChosenCurr]
        pass
   
    
    def ProfitCalculation(ExpanseID,Parameters): #Συνάρτηση υπολογισμού κέρδους
        found = false
        price = -1
        
        for r in CropSale1:
               if Parameters[1]==r:
                   price=CropSale1[r,2]
                   found =true
        if found == true:
            DisplayResult(CountryID,price)
        else:DisplayError(found)
        pass
   
    
    def DisplayResult(): #Συνάρτηση προβολής των σχετικών πληροφοριών
        pass
    
    
    def DisplayError(param): #Συνάρτηση προβολής σφάλματος
        if param==false:
            print("No country buys this crop")
        pass
    
    
    def AutomaticCalculation(ExpanseID): #Συνάρτηση αυτόματου υπολογισμού
        max=-1
        location=-1
        locationiso=-1
        iso=false
        for r in CropSale1:
            for c in r:
                if CropSale1[r,c]>max:
                    max=CropSale1[r,c]
                    location=r
                    
                elif CropSale1[r,c]==max: #se periptwsh pou dyo xwres exoun thn idia timh pwlhshs, epistrefei kai tis dyo.
                    locationiso=r
                    iso=true
           
            #xrhsh ths display synarthshs mesw gui element
            print(Country[location],max)
            if iso==true:
                print(Country[locationiso],max)
        pass
   
    
    def SaveResult(): #Συνάρτηση αποθήκευσης αποτελέσματος του υπολογισμού
        pass
