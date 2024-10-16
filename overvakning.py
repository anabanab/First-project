import psutil  # Importerar psutil-biblioteket för att hämta systemanvändning (CPU, minne och disk)
import threading  # För att kunna köra övervakningen i bakgrunden med trådar
import time  # För att pausa mellan varje övervakningscykel     

class Overvakning:
    def __init__(self):
        self.overvakning_pa = False # För att kolla om övervakningen är på eller inte
        self.overvakning_aktiv = False  # Övervakningen är inte aktiv vid start
        self.overvakning_thread = None  # Trådobjekt för övervakningen
        self.configured_alarms = []  #  Lista för att lagra konfigurerade larm

    def aktivera_overvakning(self):
        if not self.overvakning_pa:    # Kollar om övervakningen inte redan är på
            print("Övervakningen är aktiverad och kan starta")
            self.overvakning_pa = True  # Aktiverar övervakning
        else:
            print("Övervakning är redan aktiverad")

    def starta_overvakningslage(self):
        if not self.overvakning_aktiv:  # Kollar att övervakningen inte redan är aktiv 
            self.overvakning_aktiv = True  # Sätter övervakning till aktiv
    #----- Startar en separat tråd för att köra övervakningen i bakgrunden
            self.overvakning_thread = threading.Thread(target=self.overvaka_system)
            self.overvakning_thread.start()  # Startar tråden
            print("Övervakningen har startats.")
        else:
            print("Övervakningen är redan aktiv.")

    def stoppa_overvakning(self):
        if self.overvakning_aktiv:  # Endast om övervakningen är aktiv
            self.overvakning_aktiv = False  # Avaktiverar övervakningen
            if self.overvakning_thread: # Kollar om tråden existerar  ***
                self.overvakning_thread.join()  # Vänta tills tråden avslutas
            print("Övervakningen har stoppats.")
        else:
            print("Ingen övervakning är aktiv.")

    def overvaka_system(self):
        while self.overvakning_aktiv:
            print("Kontinuerlig övervakning är aktiv...")
            self.print_cpu_usage()  # Anropar funktionen för CPU-användning
            self.print_memory_usage()  # Anropar funktionen för minnesanvändning
            self.print_disk_usage()  # Anropar funktionen för diskanvändning
            self.trigger_alarms()  # Kontrollerar och utlöser larm
            time.sleep(5)  # Väntar 5 sekunder mellan varje övervakningscykel
        print("Övervakningen har stoppats.")

    # ------------Funktionerna för att hämta och skriva ut CPU, minne- och diskanvändningen i procent
    def print_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)  
        print(f"CPU Usage: {cpu_usage}%")  # Skriver ut CPU-användningen

    def print_memory_usage(self):
        memory_usage = psutil.virtual_memory()  
        print(f"Memory Usage: {memory_usage.percent}% used")  # Skriver ut hur stor del av minnet som används

    def  print_disk_usage(self):
        disk_usage = psutil.disk_usage('/')  
        print(f"Disk Usage: {disk_usage.percent}% used")  # Skriver ut hur stor del av disken som används

# *-------------------------------Lägger till larm för konfiguerade larm ***
    def add_alarm(self, alarm):
        self.configured_alarms.append(alarm)  # Lägger till ett nytt larm i listan

    def trigger_alarms(self):  # Fråga FELIX, varför larm inte utlöses
        # Hämtar aktuell användning för respektive system
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        # Kontrollerar alla konfigurerade larm och skriver ut ett meddelande om något larm utlöses   *
        for alarm_type, level in self.configured_alarms:
            if alarm_type == "CPU" and cpu_usage > level:
                print(f"***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER {level}%***")
            elif alarm_type == "Minne" and memory_usage > level:
                print(f"***VARNING, LARM AKTIVERAT, MINNESANVÄNDNING ÖVERSTIGER {level}%***")
            elif alarm_type == "Disk" and disk_usage > level:
                print(f"***VARNING, LARM AKTIVERAT, DISKANVÄNDNING ÖVERSTIGER {level}%***")

#------- Overvakning-klassen  
if __name__ == "__main__":
    overvakning = Overvakning()
    
    # Larm utlöses när det överstiger nivån: 
    overvakning.configured_alarms.append(("CPU", 80))  # Larm för CPU > 80%
    overvakning.configured_alarms.append(("Minne", 70))  # Larm för minne > 70%
    overvakning.configured_alarms.append(("Disk", 90))  # Larm för disk > 90%
    
    # Startar övervakningen och anropar funktionerna så att de körs i en seperat tråd
    overvakning.starta_overvakningslage()
    time.sleep(5)  # pausar programmet i 5 sek, övervakningen pågår fortf
    overvakning.stoppa_overvakning()  
