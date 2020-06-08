class ProfitCalculation():
    def __init__(self, CountryID):
        self.CountryID = CountryID
		

    def prof_calc_crop(self, crop_ob): #Συνάρτηση υπολογισμού κέρδους
        
        if crop_ob.crop_type == "Strawberry":
            seeds_cost = float(crop_ob.size) * 0.4
        
        elif crop_ob.crop_type == "Orange":
            seeds_cost = float(crop_ob.size) * 0.3
        
        elif crop_ob.crop_type == "Eggplant":
            seeds_cost = float(crop_ob.size) * 0.6
    
        transport_cost = 100 * float(crop_ob.est_yield)
        selling_income = 1500 * float(crop_ob.est_yield)
        true_profit = selling_income - transport_cost - seeds_cost
                
        if self.CountryID == "USA":
            profit_usd = str(true_profit*1.3)
            return ("True profit in America is: " + profit_usd +" USD" )
        
        elif self.CountryID == "Germany":
            german_transport_cost = transport_cost * 2.0
            new_profit = str(selling_income - german_transport_cost)
            return ("True profit in Germany is: " + new_profit+ "EUR" )
        
        elif self.CountryID == "France":
            str_profit = str(new_profit)
            return ("True profit in France is: " + str_profit +" EUR")
        
        elif self.CountryID == "England":
            profit_eng = str(true_profit * 0.8)
            return ("True profit in England is: " + profit_eng +" GBP")
        
        elif self.CountryID == "Greece":
            str_profit = str(new_profit)
            return ("True profit in Greece is: "+ true_profit + " EUR")
        
        elif self.CountryID == "Russia":
            new_profit = str(true_profit * 77.0)
            return ("True profit in Russia is: "+ new_profit +" RUB")
        
        elif self.CountryID == "China":
            new_profit = str(true_profit*8.0)
            return ("True profit in China is: " + new_profit+ " CNY")


    def prof_calc_photovoltaic(self, photo_ob):
        #only selling within country of origin possible
        selling_income = 100 * photo_ob.production* photo_ob.efficiency
        
        if photo_ob.ph_type == "Monocrystalline silicon":
            installation_cost = float(photo_ob.size) * 50.0
        elif photo_ob.ph_type == "Amorphous silicon":
            installation_cost = float(photo_ob.size) * 100.0
        elif photo_ob.ph_type == "Polymer and organic":
            installation_cost = float(photo_ob.size) * 25.0
        
        if self.CountryID == "USA":
            profit_usd = str((selling_income * 0.7) - installation_cost)
            return ("True profit in America is: "+ profit_usd +"USD")
        
        elif self.CountryID == "Germany":
            new_profit = str((selling_income * 2.0) - installation_cost)
            return ("True profit in Germany is: " + new_profit + " EUR" )
        
        elif self.CountryID == "France":
            new_profit = str((selling_income * 1.5) - installation_cost)
            return ("True profit in France is: "+ new_profit + " EUR")
        
        elif self.CountryID == "England":
            profit_eng = str((selling_income * 2.0) - installation_cost)
            return ("True profit in England is: " + profit_eng + " GBP" )
        
        elif self.CountryID == "Greece":
            new_profit = str(selling_income - installation_cost)
            return ("True profit in Greece is: " + new_profit + " EUR")
        
        elif self.CountryID == "Russia":
            new_profit = str((selling_income * 77.0) - installation_cost)
            return ("True profit in Russia is: " + new_profit + " RUB")
        
        elif self.CountryID == "China":
            new_profit = str((selling_income * 8.0) - installation_cost)
            return ("True profit in China is: " + new_profit + " CNY")
        
    
def ChooseParameters(): #Επιλογή χώρας πώλησης και νομίσματος    
    country_and_currency = {"USA" : "USD", "Germany" : "EUR", "France": "EUR", "England" : "GBP", "Greece" : "EUR", "Russia" : "RUB", "China" : "CNY"}    

    print("The available countries are USA, Germany, France, England, Greece, Russia, China...")
    country = input("Select on of the above. \n")
    currency = country_and_currency.get(country)
    return country, currency

