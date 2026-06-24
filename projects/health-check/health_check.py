import os
import psutil
import socket

print("=== SYSTEM HEALTH CHECK ===\n")

# =========================
# CPU
# =========================
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

# =========================
# Memory
# =========================
mem = psutil.virtual_memory()
print(f"Memory Usage: {mem.percent}%")

# =========================
# Disk
# =========================
disk = psutil.disk_usage("/")
print(f"Disk Usage: {disk.percent}%")

# =========================
# Port Check (8080)
# =========================
def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", port))
    return result == 0

if check_port(8080):
    print("Port 8080: OK")
else:
    print("Port 8080: DOWN")

print("\n=== END ===")
