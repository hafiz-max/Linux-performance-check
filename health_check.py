import psutil

def check_system_health():
    print("========== System Health Report ========")

#cpu usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

#memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

#disk usage
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

#Running Processes (Top 5 by Memory) 
print("\n--- Top 5 Memory -consuming processes ---")
#get all processes and sort by memory usage
processes = sorted( 
    psutil.process_iter(['name', 'memory_percent', 'pid']),
    key = lambda p: p.info['memory_percent'],
    reverse=True
)
for i, p in enumerate(processes[:5]):
    try:
        print(f"PID: {p.info['pid']}, Name: {p.info['name']}, Memory %: {p.info['memory_percent']:.2f}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

if __name__ == "__main__":
    check_system_health()