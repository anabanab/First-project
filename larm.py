import larm
# Skapa larm
def print_alarm_menu():
    while True:
        print("Skapa larm")
        print("1. CPU-användning")
        print("2. Minnesanvändning")
        print("3. Diskanvänding")
        print("4. Gå tillbaka till huvudmenyn")

        val = input("Ange ditt väl här (1-4): ")

        if val == "1":
            set_alarm("CPU")
        elif val == "2":
            set_alarm("Minne")
        elif val == "3":
            set_alarm("Disk")
        elif val == "4":
            print("Återgå till huvudmenyn")
            break #loopen avbryts
        else:
            print("Ogiltigt val, försök igen")

# Funktion för att ställa in nivån på larmen
configured_alarms = [()]
def set_alarm(typ):  
    while True:
    
            nivå = int(input(f"Ställ in nivå för {typ} -användning (0-100): "))
            # Kontrollera att intevallet ligger mellan 0 och 100
            if 0 <= nivå <= 100:
                print(f"Larm för {typ} satt till {nivå}%.")
                break
            else: 
                print("Nivån måste vara mellan 0 och 100. Försök igen.")
    
# Funktionen för att visa larm
def show_alarms():
    if not configured_alarms:
        print("Inga konfigurerade larm att visa.")
        input("Tryck valfri tangent för att gå tillbaka till huvudmenyn.")
        return
    else:
        # Funktionen för att sortera och skriva ut alla larm
        for alarm_type, level in sorted(configured_alarms):
            print(f"{alarm_type} larm {level}%")
    
    input("Tryck Enter för att gå tillbaka till huvudmenyn.")

configured_alarms = ([
("CPU", 70), 
("Disk", 95), 
("Minne", 80),
("Minne", 90)
])
    
show_alarms()
print_alarm_menu()
