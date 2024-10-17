from overvakning import Overvakning  # Importerar övervakningsklassen
import larm  # Importerar larmfunktioner

class HuvudMeny:
    def __init__(self):
        self.overvakning_system = Overvakning()  # Skapar ett objekt av Overvakning
        self.larm_meny = larm.LarmMeny(self.overvakning_system)  # Skapar ett objekt av LarmMeny
        self.overvakning_aktiv = False  # För att övervakningen inte ska starta automatiskt 
        self.overvakning_pa = False  # För att kolla om övervakningen är på eller inte

    def visa_meny(self):  # Visar huvudmenyn och hanterar val
        while True:
            print("HUVUDMENY")
            print("1. Aktivera övervakningen")
            print("2. Lista aktiv övervakning")
            print("3. Skapa larm")
            print("4. Visa larm")
            print("5. Starta övervakningsläge")  
            print("6. Stoppa övervakning")
            print("7. Avsluta")

            val = input("Ange ditt val här (1-7): ")
            self.hantera_val(val)

    def hantera_val(self, val):  # Hanterar de olika valen från menyn
        if val == "1":
            self.overvakning_system.aktivera_overvakning()  #Aktivera övervakning
        elif val == "2":
            print("Aktuell övervakning:")
            self.overvakning_system.print_cpu_usage()
            self.overvakning_system.print_memory_usage()
            self.overvakning_system.print_disk_usage()
        elif val == "3":
            print("Du har valt att skapa ett larm.")
            self.larm_meny.alarm_menu()  # Anropa alarmmenyn
        elif val == "4":
            print("Du har valt att visa larm.")
            self.larm_meny.show_alarms()  # Anropar funktionen för att visa larm
        elif val == "5":
            self.overvakning_system.starta_overvakningslage()
            self.overvakning_system.trigger_alarms()
        elif val == "6":
            self.overvakning_system.stoppa_overvakning()
        elif val == "7":
            print("Avslutar programmet...")
            self.overvakning_system.stoppa_overvakning()
            exit() # Avslutar programmet *
        else:
            print("Ogiltigt val, försök igen.")

#------ HuvudMeny-klassen 
if __name__ == "__main__":
    meny = HuvudMeny()
    meny.visa_meny()
