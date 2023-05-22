"""

    Aplikace - pojištěné osoby, např. "Jan Novák")

    1. DONE Vytvoření pojištěného

    2. DONE Evidujte jméno, příjmení, věk a telefonní číslo
    
    3. DONE Zobrazení seznamu všech pojištěných
    
    4. DONE Vyhledání pojištěného podle jména a příjmení objektu, jenž je uložen v kolekci v paměti

       - Využívejte konstruktory pro inicializaci objektů
       - toString() pro jejich výpis
       - Oddělujte kód do samostatných tříd a souborů
"""

"""
---------------------------------- vlastní program Evidence ----------------------------------
"""

from projekt_tridy import Clovek

def evidence():

    print("Vítejte v evidenci")
    print(""" 
    Proveďte volbu:
    1. Nový pojištěnec
    2. Výpis pojištěnců
    3. Vyhledat pojištěného
    4. Konec""")

# proměnná pro kontrolu přítomnosti hledané osoby pro volbu 3, když zůstane "None", osoba není v seznamu 
    nalezen = None
    

# ukládání volby do proměnné
    volba = int(input("Vaše volba?\n"))

# evidence nového pojištěnce, název objektu vytvořen kombinací zadávaných údajů jmeno+telofon (idecko)
    if volba == 1:
        jmeno = (input("Zadejte jméno:\n"))
        prijmeni = (input("Zadejte příjmení:\n"))
        vek = (input("Zadejte věk:\n"))
        telefon = (input("Zadejte telefon:\n"))
        idcko = jmeno+telefon
        idcko = Clovek(jmeno, prijmeni, vek, telefon)
        nabidka()

# výpis seznamu pojištěnců
    elif volba == 2:
        Clovek.vypis_seznamu()
        nabidka()

# vyhledávání podle jména a příjmení
    elif volba == 3:
        jmeno = input("Zadejte jméno:\n")
        prijmeni = input("Zadejte příjmení?:\n")

        for i in Clovek.seznam_lidi:
            if i.jmeno == jmeno and i.prijmeni == prijmeni:
                print(f"Nalezen záznam: {i}\a")
                nalezen = "nalezen"
                nabidka()

            elif nalezen == None:
                print("Hledaný člověk není v evidenci\n")
                nabidka()

    elif volba == 4:
        exit()

    else:
        evidence()

# funkce pro opětovné zobrazení voleb a načtení Evidence
def nabidka():
    pokracuj = input("Pokračujte stiskem klávesy")
    if pokracuj != "":  
        evidence()

# ----------------------------------START programu ----------------------------------
evidence()



""" pomocné příkazy pro ověřování funkčnosti """

# Clovek.vypis_seznamu()
# print(Clovek.seznam_lidi)

# x = Clovek("John", "Rambo", 39, 123456789)
# y = Clovek("Ali", "Ace", 49, 951357741)
# c = Clovek("Jane", "Doe", 29, 348166941)