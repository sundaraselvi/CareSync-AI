import schedule
import time
import json
import os
from plyer import notification

def remind(medicine_name):
    notification.notify(
        title="💊 CareSync AI - Medicine Reminder",
        message=f"Time to take your medicine: {medicine_name}",
        timeout=10
    )

last_time = None
last_medicine = None

print("Reminder system running... (keep this window open)")

while True:
    if os.path.exists("reminder_data.json"):
        with open("reminder_data.json", "r") as f:
            data = json.load(f)
        
        medicine = data["medicine"]
        reminder_time = data["time"]

        # Only re-schedule if the time/medicine actually changed
        if reminder_time != last_time or medicine != last_medicine:
            schedule.clear()
            schedule.every().day.at(reminder_time).do(remind, medicine)
            print(f"Reminder updated: {medicine} at {reminder_time} daily.")
            last_time = reminder_time
            last_medicine = medicine

    schedule.run_pending()
    time.sleep(10)
