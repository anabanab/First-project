from logg import Logger
from larm_hantering import LarmHantering
from overvakning import Overvakning  # Importerar övervakningsklassen


class LarmMeny:
    def __init__(self):
        # Listan för att lagra konfigurerade larm
        self.overvakning_system = Overvakning()
        self.larm_hantering = LarmHantering()  
        self.logger = Logger()
        self.configured_alarms = self.overvakning_system.configured_alarms  # Ladda larm vid start

    def alarm_menu(self):
        while True:
            print("Skapa larm")
            print("1. CPU-användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("4. Visa konfigurerade larm")
            print("5. Spara larm")
            print("6. Ta bort larm")
            print("7. Gå tillbaka till huvudmenyn")

            val = input("Ange ditt val här (1-7): ")

            if val == "1":
                self.set_alarms("CPU")
            elif val == "2":
                self.set_alarms("Minne")
            elif val == "3":
                self.set_alarms("Disk")
            elif val == "4":
                self.show_alarms()  
            elif val == "5":
                self.larm_hantering.save_alarm(self.configured_alarms)  # Spara larm
                self.logger.log_event("Larm har sparats.")  # Loggar sparande
            elif val == "6":
                self.show_alarms()
                index = int(input("Ange index för larmet att ta bort:")) - 1
                self.larm_hantering.remove_alarm(index)
            elif val == "7":
                break
            else:
                print("Ogiltigt val, försök igen.")

    # Funktion för att konfigurera larm
    def set_alarms(self, typ):
        while True:
            try:
                # Tar emot och försöker konvertera användarens input till en int
                nivå = int(input(f"Ställ in nivå för {typ} -användning (0-100): "))
                # Kontrollera att nivån ligger mellan 0 och 100
                if 0 <= nivå <= 100:
                    # Skapar ett larm som en tuple med typ och nivå
                    alarm = (typ, nivå)
                    # Lägger till larmet i övervakningssystemet
                    self.overvakning_system.add_alarm(alarm)
                    # Bekräftelsemeddelande till användaren
                    print(f"Larm för {typ} satt till {nivå}%.")
                    self.logger.log_event(f"Larm för {typ} satt till {nivå}%.")  # Loggar händelsen
                    break  # Avbryter loopen när ett giltigt larm har satts
                else:
                    print("Nivån måste vara mellan 0 och 100. Försök igen.")  # Felhantering för ogiltigt värde
            except ValueError:
                # Felhantering om användaren anger ett icke-numeriskt värde
                print("Ogiltigt svar. Ange en siffra mellan 0-100.")
            finally:
                print("Koden körs oavsett")
                
    def show_alarms(self):
        #Visa alla konfigurerade larm.
        self.configured_alarms = self.overvakning_system.configured_alarms  # Hämta de senaste larmen
        if not self.configured_alarms:
            print("Inga konfigurerade larm att visa.")  # Om inga larm finns, visa detta meddelande
            input("Tryck valfri tangent för att gå tillbaka till huvudmenyn.")
            return  # Avslutar funktionen om inga larm finns
        # Sorterar och skriver ut alla larm som är konfigurerade ***
        for alarm_type, level in sorted(self.configured_alarms):
            print(f"{alarm_type} larm {level}%")  # Skriver ut typ och nivå för varje larm
        input("Tryck Enter för att gå tillbaka till huvudmenyn.")


# Om programmet körs direkt, startas larmmenyn (detta körs inte vid import)
if __name__ == "__main__":
    # LarmMeny = LarmMeny()
    pass  # Det kan implementeras senare
