class LarmMeny:
    # Konstruktorn __init__ initierar objektets egenskaper
    def __init__(self, overvakning_system):
        # Listan för att lagra konfigurerade larm
        self.configured_alarms = []
        # Övervakningssystemet som ansvarar för att lägga till och hantera larm
        self.overvakning_system = overvakning_system
    
    # Funktion för att visa och hantera larm-menyn
    def alarm_menu(self):
        # En loop som kör menyn tills användaren väljer att avsluta
        while True:
            # Skriver ut alternativen i menyn
            print("Skapa larm")
            print("1. CPU-användning")
            print("2. Minnesanvändning")
            print("3. Diskanvänding")
            print("4. Visa konfigurade larm")
            print("5. Gå tillbaka till huvudmenyn")

            # Tar emot användarens val
            val = input("Ange ditt väl här (1-5): ")

            # Kollar användarens val och kallar på rätt metod
            if val == "1":
                self.set_alarms("CPU")  # Om användaren väljer CPU-användning
            elif val == "2":
                self.set_alarms("Minne")  # Om användaren väljer Minnesanvändning
            elif val == "3":
                self.set_alarms("Disk")  # Om användaren väljer Diskanvändning
            elif val == "4":
                self.show_alarms()  # Om användaren vill visa konfigurerade larm
            elif val == "5":
                print("Återgå till huvudmenyn")
                break  # Avslutar loopen, vilket skickar användaren tillbaka till huvudmenyn
            else:
                print("Ogiltigt val, försök igen")  # Felhantering om ett ogiltigt val görs

    # Funktion för att konfigurera larm
    def set_alarms(self, typ):
        # En loop för att fortsätta tills ett korrekt värde anges
        while True:
            try:
                # Tar emot och försöker konvertera användarens input till en int
                nivå = int(input(f"Ställ in nivå för {typ} -användning (0-100): "))
                # Kontrollera att nivån ligger mellan 0 och 100
                if 0 <= nivå <= 100:
                    # Skapar ett larm som en tuple med typ och nivå
                    alarm = (typ, nivå)
                    # Lägger till larmet i listan av konfigurerade larm
                    self.configured_alarms.append(alarm)
                    # Lägger till larmet i övervakningssystemet
                    self.overvakning_system.add_alarm(alarm)
                    # Bekräftelsemeddelande till användaren
                    print(f"Larm för {typ} satt till {nivå}%.")
                    break  # Avbryter loopen när ett giltigt larm har satts
                else:
                    print("Nivån måste vara mellan 0 och 100. Försök igen.")  # Felhantering för ogiltigt värde
            except ValueError:
                # Felhantering om användaren anger ett icke-numeriskt värde
                print("Ogiltigt svar. Ange en siffra mellan 0-100.")
            finally:
                # Detta block körs alltid, oavsett om ett fel inträffar eller inte
                print("Koden körs alltid oavsett")

    # Funktion för att visa alla konfigurerade larm
    def show_alarms(self):
        # Kontrollera om det finns några larm
        if not self.configured_alarms:
            print("Inga konfigurerade larm att visa.")  # Om inga larm finns, visa detta meddelande
            input("Tryck valfri tangent för att gå tillbaka till huvudmenyn.")
            return  # Avslutar funktionen om inga larm finns
        else:
            # Sorterar och skriver ut alla larm som är konfigurerade
            for alarm_type, level in sorted(self.configured_alarms):
                print(f"{alarm_type} larm {level}%")  # Skriver ut typ och nivå för varje larm
        
        # Väntar på att användaren ska trycka Enter innan den återgår till menyn
        input("Tryck Enter för att gå tillbaka till huvudmenyn.")

# Om programmet körs direkt, startas larmmenyn (detta körs inte vid import)
if __name__ == "__main__":
    # Skapar ett objekt av LarmMeny-klassen
    larm_meny = LarmMeny()  # Övervakningssystemet saknas här och skulle behöva passeras som argument
