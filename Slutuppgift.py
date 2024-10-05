import användning  # Importerar filen med funktionerna för användning
import larm   # Importerar larmfunktioner för CPU, minne och disk

def print_huvud_meny():
    while True:
        print("\nHUVUDMENY")
        print("1. Aktivera övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Avsluta")

        # Användarens val
        val = input("Ange ditt val här (1-6): ")

        # Hantera användarens val
        if val == "1": 
            print("Du har aktiverat övervakning")

        elif val == "2":
            print("Du har listat aktiv övervakning")
            användning.print_cpu_usage()    # Anropar funktionen för CPU-användning
            användning.print_memory_usage()  # Anropar funktionen för minnesanvändning
            användning.print_disk_usage()    # Anropar funktionen för diskens användning

        elif val == "3":
            print("Du har skapat larm")
            larm.print_alarm_menu()     # Visar menyn för larm
            
           
        elif val == "4":
            print("Du har visat larm")
            larm.show_alarms()   # Anropar funktionen för att visa larm
            

        elif val == "5":
            print("Du har startat övervakningsläge")  # Övervakningen är startad
            
        elif val == "6":
            print("Avslutar")
            break  # Avsluta loopen
        else: 
            print("Ogiltigt val, försök igen")

print_huvud_meny()
