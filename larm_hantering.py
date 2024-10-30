import json
from logg import Logger 
global_configured_alarms = []  # Globala konfigurerade larm 

class LarmHantering:
    def __init__(self):
        self.larm_fil = "konfigurerade_larm.json"  # Filnamn för larmen
        self.configured_alarms = [] # Initierar listan för konfigurerade larm
        self.load_alarms()  # Ladda larm vid initiering
        self.logger = Logger()
        
# Sparar larm till json fil
    def save_alarms(self):
# Spara konfigurerade larm till en JSON-fil
        if not global_configured_alarms:  # Kontrollera om det finns larm att spara
            print("Inga larm att spara.")
            return
        with open(self.larm_fil, 'w') as f:
            json.dump(global_configured_alarms, f)
        print("Larm har sparats.")

# Funktion för att ta bort ett specifikt larm.
    def remove_alarm(self, index):
        try:
            index = int(input("Ange numret på larmet du vill ta bort: ")) -1
            if 0 <= index < len(global_configured_alarms): # Kontrollera att indexet är giltigt
                removed_alarm = global_configured_alarms.pop(index)  # Ta bort larmet
                self.save_alarms()  # Spara uppdaterade larm
                print(f"Larmet {removed_alarm} har tagits bort.")
                self.logger.log_event(f"Larm {removed_alarm} har tagits bort.")
            else:
                print("Ogiltigt val. Ange ett giltigt index.")
        except ValueError:
            print("Ogiltigt val. Ange ett giltigt index.")

# Laddar larm från json filen
    def load_alarms(self):
        try:
            with open(self.larm_fil, 'r') as f:
                loaded_alarms = json.load(f)
                global_configured_alarms.clear()  # Töm den globala listan först (så alla gamla larm inte visas)
                global_configured_alarms.extend(loaded_alarms)  # Ladda in nya larm
                print(f"{len(global_configured_alarms)} larm har laddats från {self.larm_fil}.")
        except FileNotFoundError:
            print("Inga tidigare larm hittades, skapar en ny lista.")
        except json.JSONDecodeError:
            print("Felaktig filformat, kunde inte läsa larm.")
            
larm_hantering = LarmHantering()


