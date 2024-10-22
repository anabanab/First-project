import json
import os
from logg import Logger 

class LarmHantering:
    def __init__(self):
        self.larm_fil = "konfigurerade_larm.json"  # Filnamn för larmen
        self.configured_alarms = []  # Initierar listan för konfigurerade larm
        self.load_alarms()  # Ladda larm vid initiering
        self.logger = Logger()



    def save_alarm(self, configured_alarms):
        """Spara konfigurerade larm till en JSON-fil."""
        if not self.configured_alarms:  # Kontrollera om det finns larm att spara
            print("Inga larm att spara.")
            return
        with open(self.larm_fil, 'w') as f:
            json.dump(configured_alarms, f)
        print("Larm har sparats.")

    def remove_alarm(self, index):
        #Metod för att ta bort ett specifikt larm."""
        try:
            # index = int(input("Ange numret på larmet du vill ta bort: ")) - 1
            if 0 <= index < len(self.configured_alarms):  # Kontrollera att indexet är giltigt
                removed_alarm = self.configured_alarms.pop(index)  # Ta bort larmet
                self.save_alarm(self.configured_alarms)  # Spara uppdaterade larm
                print(f"Larmet {removed_alarm} har tagits bort.")
                if self.logger:
                    self.logger.log_event(f"Larm {removed_alarm} har tagits bort.")
            else:
                print("Ogiltigt val. Ange ett giltigt index.")
        except ValueError:
            print("Ogiltigt val. Ange ett giltigt index.")


    def load_alarms(self):
        #Ladda larm från JSON-fil."""
        print("Laddar tidigare konfigurerade larm...")  # Inladdningsmeddelande
        if os.path.exists(self.larm_fil):
            with open(self.larm_fil, 'r') as f:
                self.configured_alarms = json.load(f)
                print(f"{len(self.configured_alarms)} larm har laddats.")
        else:
            print("Ingen konfigurerad larmfil hittades.")

larm_hantering = LarmHantering()
