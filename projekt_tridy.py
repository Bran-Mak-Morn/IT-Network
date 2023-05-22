# třída pro konstrukci pojištěnců s metodami init, str a se statickou metodou pro výpis seznamu všech pojištěnců
class Clovek:
    seznam_lidi = []

# Statická metoda pro výpis seznamu přidaných lidí 
    @staticmethod
    def vypis_seznamu():
        for i in Clovek.seznam_lidi:
            print(i)


# vytvoří nového člověka s atributy jmeno, prijmeni, vek, telefon
# rovnou jej přidá do seznamu Třídy (statická proměnná)
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        Clovek.seznam_lidi.append(self)

# výpis člověka - pomocí metody str   
    def __str__(self):
        return f"jméno: {self.jmeno}, příjmení: {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"