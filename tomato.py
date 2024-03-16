from datetime import datetime, timedelta

# input
now = datetime.now()
print(now)
stop_hour = int(input("Enter your stopping hour: "))
stop_minute = int(input("Enter your stopping minute: "))
current_hour = now.hour

# Calculating minutes and hours in session and in 12 hour format
if current_hour > 12:
    current_hour = current_hour - 12
now_total_minutes = (current_hour * 60) + now.minute
end_total_minutes = (stop_hour * 60) + stop_minute

if now_total_minutes < end_total_minutes:
    work_minutes = end_total_minutes - now_total_minutes
else:
    work_minutes = (720 - now_total_minutes) + end_total_minutes

end_time = datetime(now.year, now.month, now.day, stop_hour, stop_minute, now.second)

# testing
print(end_time)
# print("Minutes leftover from 30 minutes ", work_minutes%30)
# print("Minutes leftover from 28 minutes - end break", ((work_minutes-5)%28))
# print("Minutes leftover from 29 minutes - end break", ((work_minutes-5)%29))
print("Minutes leftover from 30 minutes - end break", ((work_minutes - 5) % 30))
print("Minutes leftover from 31 minutes - end break", ((work_minutes - 5) % 31))
print("Minutes leftover from 32 minutes - end break", ((work_minutes - 5) % 32))
print("Minutes leftover from 33 minutes - end break", ((work_minutes - 5) % 33))
print("Minutes leftover from 34 minutes - end break", ((work_minutes - 5) % 34))
print("Minutes leftover from 35 minutes - end break", ((work_minutes - 5) % 35))
# print("Minutes leftover from 36 minutes - end break", ((work_minutes-5)%36))
print("Minutes leftover from 35 minutes ", work_minutes % 35)
print("30 minute sections", work_minutes / 30)
print("35 minute sections", work_minutes / 35)
print("hours ", work_minutes // 60)
print("minutes ", work_minutes % 60)

# make method to select session splits
# there will not be a break needed at the end for example: 25work 5break 25work 5break 25work done
# work sessions between 25-30mins and breaks around 5 mins
thirty_minute_leftover = (work_minutes - 5) % 30
thirty_one_minute_leftover = (work_minutes - 5) % 31
thirty_two_minute_leftover = (work_minutes - 5) % 32
thirty_three_minute_leftover = (work_minutes - 5) % 33
thirty_four_minute_leftover = (work_minutes - 5) % 34
thirty_five_minute_leftover = (work_minutes - 5) % 35

least_leftover_time = (work_minutes - 5) % 30
for i in range(30, 35):
    if least_leftover_time >= ((work_minutes - 5) % (i+1)):
        least_leftover_time = (work_minutes - 5) % (i+1)
        best_section_time = (i+1)

print(least_leftover_time)
print(best_section_time)

# method that takes the time sections and puts them in to timed events
work_section = timedelta(minutes = (best_section_time-5))
break_section = timedelta(minutes = best_section_time)
end_section = now + work_section
print("work section time", end_section)



# method that prints the times and alerts
