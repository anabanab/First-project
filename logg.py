from datetime import datetime 

class Logger:
    def __init__(self):
        self.log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    
    def log_event(self, event):
        # Loggar händelser i en seperat fil
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as log:
            log.write(f"{timestamp} - {event}\n")
if __name__ == "__main__":
    logger = Logger()
    logger.log_event("Övervakning startad.")  # Loggar när övervakningen startas