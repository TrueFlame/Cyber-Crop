from expanse import Expanse

class History():#Χρειάζεται εισαγωγή δεδομένων από Account και ίσως σύνδεση με άλλες κλάσεις για αποθήκευση στοιχείων
    def __init__(self, AccountPrivilege, ExpanseID):
        self.AccountPrivilege=AccountPrivilege
        self.ExpanseID=ExpanseID

#Ίσως χρειαστεί συνάρτηση που θα την χρησιμοποιούν οι άλλες κλασεις για αποθήκευση του ιστορικού

    
    def ReturnPrivilege(AccountPrivilege): #Επιστροφή των δικαιωμάτων του χρήστη μέσω συνάρτησης
        pass
    
    def ChooseOption(): #Συνάρτηση που εμφανίζει και διαχειρίζεται τις επιλογές του χρήστη
        pass
    
    def ViewData(ExpanseID): #Προβολή ιστορικού/πληροφοριών της συγκεκριμένης έκτασης
        pass
    
    def DeleteData(ExpanseID): #Διαγραφή ιστορικού/πληροφοριών της συγκεκριμένης έκτασης
        pass
    
    def ExportData(ExpanseID): #Εξαγωγή των στοιχείων ιστορικού/πληροφοριών της συγκεκριμένης έκτασης σε αρχείο
        pass
