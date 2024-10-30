from datetime import datetime 

 # Skapar en loggfil med namn baserat på datum och tid
class Logger:
    def __init__(self):            
        self.log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    
    def log_event(self, event):
# Loggar händelser i en seperat fil
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as log:  # Öppnar loggfilen och lägger till nya loggar slutet
            log.write(f"{timestamp} - {event}\n") # Loggar tidsstämpeln och händelser
            
if __name__ == "__main__":
    logger = Logger()
    logger.log_event("Övervakning startad.")  # Loggar när övervakningen startas