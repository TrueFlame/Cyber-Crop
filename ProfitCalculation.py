class ProfitCalculation(): #Χρειάζεται εισαγωγή δεδομένων από Account και Expanse
    def __init__(self, AccountPrivilege, ExpanseID, CountryID, Currency, Parameters):
		self.AccountPrivilege=AccountPrivilege
		self.ExpanseID=ExpanseID
		self.CountryID=CountryID
		self.Currency=Currency
		self.Parameters=Parameters
		

    def CheckPrivilege(AccountPrivilege): #Έλεγχος δικαιωμάτων πρόσβασης του χρήστη στην υπηρεσία
		pass
    def ReturnPrivilege(AccountPrivilege): #Επιστροφή των δικαιωμάτων του χρήστη μέσω συνάρτησης
		pass
    def ChooseExpanse(ExpanseID): #Επιλογή έκτασης
		pass
    def ReturnErrorCode(): #Debug συνάρτηση
		pass
    def ChooseOption(): #Συνάρτηση που εμφανίζει και διαχειρίζεται τις επιλογές του χρήστη
		pass
    def ChooseParameters(CountryID,Currency): #Επιλογή χώρας πώλησης και νομίσματος 
		pass
    def ProfitCalculation(ExpanseID,Parameters): #Συνάρτηση υπολογισμού κέρδους
		pass
    def DisplayResult(): #Συνάρτηση προβολής των σχετικών πληροφοριών
		pass
    def DisplayError(): #Συνάρτηση προβολής σφάλματος
		pass
    def AutomaticCalculation(ExpanseID): #Συνάρτηση αυτόματου υπολογισμού
		pass
    def SaveResult(): #Συνάρτηση αποθήκευσης αποτελέσματος του υπολογισμού
		pass


