import psutil


# Skriver ut CPU-användningen i procent
def print_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

# Skriver ut minnesanvändingen i procent
def print_memory_usage():
    memory_usage = psutil.virtual_memory()
    print(f"Memory Usage: '{memory_usage.percent}% used")

# Skriver ut diskanvändningen i procent
def print_disk_usage():
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}% used")