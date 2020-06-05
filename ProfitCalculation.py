class ProfitCalculation(): #Χρειάζεται εισαγωγή δεδομένων από Account και Expanse
    def __init__(self, ExpanseID, CountryID, CurrencyID):
        self.ExpanseID=ExpanseID
        self.CountryID = CountryID
        self.CurrencyID = CurrencyID
		

    def prof_calc_crop(self, crop_ob): #Συνάρτηση υπολογισμού κέρδους
        transport_cost = 100 * crop_ob.est_yield
        selling_income = 1500 * crop_ob.est_yield
        true_profit = selling_income - transport_cost
        
        if self.CountryID == "USA":
            profit_usd = true_profit*1.3
            print("True profit in America is: "+profit_usd +" " +self.CurrencyID)
        
        elif self.CountryID == "Germany":
            german_transport_cost = transport_cost*2.0
            new_profit = selling_income - german_transport_cost
            print("True profit in Germany is: "+ new_profit +" " +self.CurrencyID)
        
        elif self.CountryID == "France":
            print("True profit in France is: "+ true_profit +" "+ self.CurrencyID)
        
        elif self.CountryID == "England":
            profit_eng = true_profit*0.8
            print("True profit in England is: "+ profit_eng+ " "+ self.CurrencyID)
        
        elif self.CountryID == "Greece":
            print("True profit in Greece is: "+ true_profit+" "+ self.CurrencyID)
        
        elif self.CountryID == "Russia":
            new_profit = true_profit*77.0
            print("True profit in Russia is: "+ new_profit+" "+ self.CurrencyID)
        
        elif self.CountryID == "China":
            new_profit = true_profit*8.0
            print("True profit in China is: "+ new_profit+" "+ self.CurrencyID)


    def prof_calc_photovoltaic(self, photo_ob):
        #only selling within country of origin possible
        selling_income = 100 * photo_ob.production* photo_ob.efficiency
        
        if self.CountryID == "USA":
            profit_usd = selling_income * 0.7
            print("True profit in America is: "+profit_usd +" " +self.CurrencyID)
        
        elif self.CountryID == "Germany":
            new_profit = selling_income * 2.0
            print("True profit in Germany is: "+ new_profit +" " +self.CurrencyID)
        
        elif self.CountryID == "France":
            new_profit = selling_income * 1.5
            print("True profit in France is: "+ new_profit +" "+ self.CurrencyID)
        
        elif self.CountryID == "England":
            profit_eng = selling_income * 2.0
            print("True profit in England is: "+ profit_eng+ " "+ self.CurrencyID)
        
        elif self.CountryID == "Greece":
            print("True profit in Greece is: "+ selling_income +" "+ self.CurrencyID)
        
        elif self.CountryID == "Russia":
            new_profit = selling_income * 77.0
            print("True profit in Russia is: "+ new_profit+" "+ self.CurrencyID)
        
        elif self.CountryID == "China":
            new_profit = selling_income * 8.0
            print("True profit in China is: "+ new_profit+" "+ self.CurrencyID)
    
    def AutomaticCalculation(ExpanseID): #Συνάρτηση αυτόματου υπολογισμού
        pass
    
    def SaveResult(): #Συνάρτηση αποθήκευσης αποτελέσματος του υπολογισμού
        pass

    
def ChooseParameters(): #Επιλογή χώρας πώλησης και νομίσματος    
    country_and_currency = {"USA" : "USD", "Germany" : "EUR", "France": "EUR", "England" : "GBP", "Greece" : "EUR", "Russia" : "RUB", "China" : "CNY"}    

    print("The available countries are USA, Germany, France, England, Greece, Russia, China...")
    country = input("Select on of the above. \n")
    currency = country_and_currency.get(country)
    return country, currency

