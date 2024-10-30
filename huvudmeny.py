from overvakning import Overvakning  # Importerar övervakningsklassen
from larm import LarmMeny  # Importerar larmfunktioner
from larm_hantering import LarmHantering #Importerar larm_hantering 


class HuvudMeny:
    def __init__(self):
        self.larm_hantering = LarmHantering() 
        self.overvakning_system = Overvakning() 
        self.larm_meny = LarmMeny()

# Meny som visas för användaren
    def visa_meny(self):  
        while True:
            print("HUVUDMENY")
            print("1. Aktivera övervakningen")
            print("2. Lista aktiv övervakning")
            print("3. Skapa larm")
            print("4. Visa larm")
            print("5. Ta bort larm")
            print("6. Starta övervakningsläge")  
            print("7. Stoppa övervakning")
            print("8. Avsluta")

            val = input("Ange ditt val här (1-8): ")
            self.hantera_val(val)

# Här nedan hanteras användarens val
    def hantera_val(self, val):  # Hanterar de olika valen från menyn
        if val == "1":
            self.overvakning_system.aktivera_overvakning()  #Aktivera övervakning
        elif val == "2":
            if not self.overvakning_system.overvakning_pa:
                print("Du måste först aktivera övervakningen")
            else:
                self.overvakning_system.print_usage()
                print("Aktuell övervakning:")
        elif val == "3":
            print("Du har valt att skapa ett larm.")
            self.larm_meny.alarm_menu()  # Anropa alarmmenyn
        elif val == "4":
            print("Du har valt att visa larm.")
            self.larm_meny.show_alarms()  # Anropar funktionen för att visa larm 
        elif val == "5":
            self.larm_meny.show_alarms()
            try:
                index = int(input("Ange index för larmet att ta bort:")) - 1
                self.larm_hantering.remove_alarm(index)
                print("Du har tagit bort larm")
            except (ValueError, IndexError):
                print("Ogiltigt index, larm tas inte bort")
        elif val == "6":
            if not self.overvakning_system.overvakning_pa:   # Startar övervakningsläge
                print("Du måste först aktivera övervakningen")
            else:
                self.overvakning_system.starta_overvakningslage()
        elif val == "7":
            self.overvakning_system.stoppa_overvakning()
        elif val == "8":
            print("Avslutar programmet...")
            self.overvakning_system.stoppa_overvakning()
            exit() # Avslutar programmet
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    meny = HuvudMeny()  # Skapar en instans av HuvudMeny
    meny.visa_meny()  # Detta startar menyn där användaren kan interagera
