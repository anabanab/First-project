import psutil  # Importerar psutil-biblioteket för att hämta systemanvändning (CPU, minne och disk)
import threading  # För att kunna köra övervakningen i bakgrunden med trådar
import time  # För att pausa mellan varje övervakningscykel   
from logg import Logger 
from larm_hantering import global_configured_alarms, LarmHantering

class Overvakning:
    def __init__(self):
        self.overvakning_pa = False 
        self.overvakning_aktiv = False  
        self.overvakning_thread = None  # Trådobjekt för övervakningen
        self.logger = Logger()
        self.configured_alarms = global_configured_alarms

# Aktiverar övervakningen så inte det startar vid start
    def aktivera_overvakning(self):
        if not self.overvakning_pa:    # Kollar om övervakningen inte redan är på
            print("Övervakningen är aktiverad och kan starta")
            self.overvakning_pa = True  # Aktiverar övervakning
            self.logger.log_event("Övervakningen har aktiverats")
        else:
            print("Övervakningen är redan aktiv")

# Startar övervakningsläge och använder tråd för kontinuerlig övervaking utan block
    def starta_overvakningslage(self):
        if not self.overvakning_aktiv:  # Kollar att övervakningen inte redan är aktiv 
            self.overvakning_aktiv = True  # Sätter övervakning till aktiv
#Startar en separat tråd för att köra övervakningen i bakgrunden
            self.overvakning_thread = threading.Thread(target=self.overvaka_system)
            self.overvakning_thread.start()  # Startar tråden
            print("Övervakningen har startats.")
            self.logger.log_event("Övervakningsläge har startats.")
        else:
            print("Övervakningsläge är redan aktiv.")

# Funktion för att övervakningen avslutas korrekt
    def stoppa_overvakning(self):
        if self.overvakning_aktiv:  # Endast om övervakningen är aktiv
            self.overvakning_aktiv = False  # Avaktiverar övervakningen
            if self.overvakning_thread: # Kollar om tråden existerar  
                self.overvakning_thread.join()  # Vänta tills tråden avslutas
            print("Övervakningen har stoppats.")
            self.logger.log_event("Övervakningen har stoppats.")
        else:
            print("Ingen övervakning är aktiv.")

# Loopar medan övervakningen är aktiv
    def overvaka_system(self):
        while self.overvakning_aktiv:
            print("Kontinuerlig övervakning är aktiv...") # Här nedan anropas funktionen för cpu, minne och disk
            self.print_usage()   
            self.trigger_alarms()  # Kontrollerar och utlöser larm
            time.sleep(5)  # Väntar 5 sekunder mellan varje övervakningscykel
        print("Övervakningen har stoppats.")
        self.logger.log_event("Övervakningen har stoppats.")
        

# Funktionen för att hämta och skriva ut CPU, minne- och diskanvändningen i procent
    def print_usage(self):
        print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}% used")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}% used")

# Lägger till nytt larm i konfiguerade listan
    def add_alarm(self, alarm):
        self.configured_alarms.append(alarm)  # Lägger till ett nytt larm i listan
        self.logger.log_event(f"Larm tillagt: {alarm}")

# Lägger till funktion för att trigga alarm 
    def trigger_alarms(self):  
        if not self.configured_alarms:
            print("Inga larm är konfiguerade")
            return
        # Hämtar aktuell användning för respektive system
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
    
    # För att hålla reda på det högsta aktiverade larmet
        highest_triggeredcpu_alarm = None  
        highest_triggeredmemory_alarm = None
        highest_triggereddisk_alarm = None
        alarm_triggered = False  # För att hålla reda på om något larm har aktiverats
    
    # Kontrollera och utlös larm
        for alarm_type, level in sorted(self.configured_alarms, key=lambda x: x[1], reverse=True):
            if alarm_type == "CPU" and cpu_usage > level:
                if not highest_triggeredcpu_alarm or level > highest_triggeredcpu_alarm:
                    highest_triggeredcpu_alarm = level
                    alarm_triggered = True
                    print(f"***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER {level}%***")
                    self.logger.log_event(f"***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER {level}%***")
            if alarm_type == "Minne" and memory_usage > level:
                if not highest_triggeredmemory_alarm or level > highest_triggeredmemory_alarm:
                    highest_triggeredmemory_alarm = level
                    alarm_triggered = True
                    print(f"***VARNING, LARM AKTIVERAT, MINNESANVÄNDNING ÖVERSTIGER {level}%***")
                    self.logger.log_event(f"***VARNING, LARM AKTIVERAT, MINNESANVÄNDNING ÖVERSTIGER {level}%***")
            if alarm_type == "Disk" and disk_usage > level:
                if not highest_triggereddisk_alarm or level > highest_triggereddisk_alarm:
                    highest_triggereddisk_alarm = level
                    alarm_triggered = True
                    print(f"***VARNING, LARM AKTIVERAT, DISKANVÄNDNING ÖVERSTIGER {level}%***")
                    self.logger.log_event(f"***VARNING, LARM AKTIVERAT, DISKANVÄNDNING ÖVERSTIGER {level}%***")
        if not alarm_triggered:
            print("Inga larm aktiverade den här gången.")        

if __name__ == "__main__":
    overvakning = Overvakning()
# Larm utlöses när det överstiger nivån: ******
    overvakning.configured_alarms.append(("CPU", 80))  # Larm för CPU överstiger 80%
    overvakning.configured_alarms.append(("Minne", 70))  # Larm för minne överstiger 70%
    overvakning.configured_alarms.append(("Disk", 90))  # Larm för disk överstiger 90%
# Startar övervakningen och anropar funktionerna så att de körs i en seperat tråd
    overvakning.starta_overvakningslage()
    time.sleep(15)  # pausar programmet i 15 sek, övervakningen pågår fortf
    overvakning.stoppa_overvakning() 
#----- Skapad av Anab Mohamed Abdullahi