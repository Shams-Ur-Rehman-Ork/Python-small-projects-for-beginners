from datetime import datetime, time
from playsound import playsound

alarm_time = input("Enter time of alarm:HH:MM:SS\n")

alarm_hour = alarm_time[:2]
alarm_minutes = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting Up Alarm")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minutes == current_minutes:
                if alarm_seconds == current_seconds:
                    print("Wake Up")
                    playsound('1.mp3')
                    break



