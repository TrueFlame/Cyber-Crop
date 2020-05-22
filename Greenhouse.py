class Greenhouse(): #Χρειάζεται εισαγωγή δεδομένων από Account και Expanse
    def __init__(self, ID, AccountPrivilege, ExpanseID, SensorID):
        self.AccountPrivilege=AccountPrivilege
        self.ExpanseID=ExpanseID
        self.ID=ID
        self.SensorID=SensorID
		
    def CheckPrivilege(AccountPrivilege): #Έλεγχος δικαιωμάτων πρόσβασης του χρήστη στην υπηρεσία
    		pass
    def ReturnPrivilege(AccountPrivilege): #Επιστροφή των δικαιωμάτων του χρήστη μέσω συνάρτησης
    		pass
    def ChooseExpanse(ExpanseID): #Επιλογή έκτασης
    		pass
    def ReturnErrorCode(): #Debug συνάρτηση
    		pass
    def InsertData(ExpanseID): #Εισαγωγή στοιχείων αν αυτά λείπουν από την έκταση
    		pass
    def ChooseOption(): #Συνάρτηση που εμφανίζει και διαχειρίζεται τις επιλογές του χρήστη
    		pass
    def CheckSensor(SensorID): #Έλεγχος κατάστασης των αισθητήρων
    		pass
    def ReturnStatus(SensorID): #Επιστροφή κατάστασης αισθητήρων
    		pass
    def Initialize(): #Συνάρτηση ενεργοποίησης υπηρεσίας αυτόματου ποτίσματος
    		pass
    def DisplayStatus(ID): #Προβολή εσωτερικής κατάστασης του θερμοκηπίου
    		pass
    def EditStatus(ID): #Διαχείριση/αλλαγή της εσωτερικής κατάστασης
    		pass
    def AutomaticManagement(ID): #Αυτόματη διαχείριση από το σύστημα
    		pass

