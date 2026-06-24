import os

LOG_FILE = "logs/app.log"

keywords = ["error", "warning", "info"]

result = {"app.log": {k: 0 for k in keywords}}

try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            line = line.lower()

            for k in keywords:
                if k in line:
                    result["app.log"][k] += 1

except FileNotFoundError:
    print("log file not found")
    exit()

print("\n=== LOG REPORT ===")
print(result)

total = sum(result["app.log"].values())
error = result["app.log"]["error"]

if total > 0:
    rate = error / total * 100
    print(f"\nERROR RATE: {rate:.2f}%")

if error > 5:
    print("🚨 ALERT: HIGH ERROR RATE")
