
from clovek import Clovek

class Evidence:  

# konstruktor - spouští metodu s nabídkou a vytváří seznam pojištěnců (v defaultu prázdný)
    def __init__(self, seznam_lidi = []):
        self.seznam_lidi = seznam_lidi
        self.nabidka()
    
        
    def nabidka(self):
        print("Vítejte v evidenci")
        print(""" 
        Proveďte volbu:
        1. Nový pojištěnec
        2. Výpis pojištěnců
        3. Vyhledat pojištěného
        4. Konec""")

# ukládání volby do proměnné
        volba = int(input("Vaše volba?\n"))

# proměnná pro kontrolu přítomnosti hledané osoby pro volbu 3, když zůstane "None", osoba není v seznamu 
        nalezen = None
    
# VOLBA 1 evidence nového pojištěnce, název objektu vytvořen kombinací zadávaných údajů jmeno+telefon (idecko)
# nový objekt je pak přidán do seznamu pojištěnců
        if volba == 1:
            jmeno = (input("Zadejte jméno:\n"))
            prijmeni = (input("Zadejte příjmení:\n"))
            vek = (input("Zadejte věk:\n"))
            telefon = (input("Zadejte telefon:\n"))
            idcko = jmeno+telefon
            idcko = Clovek(jmeno, prijmeni, vek, telefon)
            self.seznam_lidi.append(idcko)
            self.volbyznovu()

# VOLBA 2 výpis seznamu pojištěnců
        elif volba == 2:
            self.vypis_seznamu()
            self.volbyznovu()

# VOLBA 3 vyhledávání podle jména a příjmení
        elif volba == 3:
            jmeno = input("Zadejte jméno:\n")
            prijmeni = input("Zadejte příjmení?:\n")

            for pojistenec in self.seznam_lidi:                
                if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:                   
                    print(f"Nalezen záznam: {pojistenec}\a")
                    nalezen = "nalezen"
                    self.volbyznovu()

            if nalezen == None:
                print("Hledaný člověk není v evidenci\n")
                self.volbyznovu()

# VOLBA 4 exit
        elif volba == 4:
            exit()

        else:
            self.nabidka()

# METODA  PRO VOLBU 2 = pro výpis seznamu přidaných lidí 
    def vypis_seznamu(self):
        if len(self.seznam_lidi) == 0:
            print("V evidenci nejsou žádní pojištěnci")
        else:
            for pojistenec in self.seznam_lidi:
                print(f"Výpis z evidence: {pojistenec}")

# metoda pro opětovné zobrazení voleb a načtení Evidence
    def volbyznovu(self):
        pokracuj = input("Pokračujte stiskem klávesy")
        if pokracuj != "":  
            self.nabidka()

