import systeminfo #importerar nya filen med funktionerna

def print_huvud_meny():
    while True:
        print("HUVUDMENY")
        print("1. Aktivera övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Avsluta")


        val = input("Ange ditt val här (1-6)")

        if val == "1": 
            print("Du har aktiverat övervakning")

        elif val == "2":
            print("Du har listat aktiv övervakning")
            systeminfo.print_cpu_usage()    #anropar funktionen för CPU-användningen
            systeminfo.print_memory_usage()  #anropar funktionen för minnesanvändingen
            systeminfo.print_disk_usage()    #anropar funktionen för diskanvändningen

        elif val == "3":
            print("Du har skapat larm")
        
        elif val == "4":
            print("Du har visat larm")
        
        elif val == "5":
            print("Du har startat övervakningsläge")

        elif val == "6":
            print("Avslutar")
            break
        else: 
            print("Ogiltigt val, försök igen")


        
