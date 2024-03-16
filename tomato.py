from datetime import datetime

now = datetime.now()
print (now)

stop_hour = int(input("Enter your stopping hour"))
stop_minute = int(input("Enter your stopping minute"))

current_hour = now.hour
if current_hour > 12:
    current_hour = current_hour - 12
now_total_minutes = (current_hour * 60) + now.minute
end_total_minutes = (stop_hour * 60) + stop_minute

if now_total_minutes < end_total_minutes:
    work_minutes = end_total_minutes - now_total_minutes
else:
    work_minutes = (720 - now_total_minutes) + end_total_minutes

end_time = datetime(now.year, now.month, now.day, stop_hour, stop_minute ,now.second)

print(end_time)
print(work_minutes%30)
print(work_minutes/30)
print(work_minutes/35)