
# třída pro konstrukci pojištěnců s metodami init, str a se statickou metodou pro výpis seznamu všech pojištěnců

class Clovek:

# vytvoří nového člověka s atributy jmeno, prijmeni, vek, telefon

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        
# výpis člověka - pomocí metody str   
    def __str__(self):
        return f"jméno: {self.jmeno}, příjmení: {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"


