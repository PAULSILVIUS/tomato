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
print("Minutes leftover from 30 minutes - end break", ((work_minutes + 5) % 30))
print("Minutes leftover from 31 minutes - end break", ((work_minutes + 5) % 31))
print("Minutes leftover from 32 minutes - end break", ((work_minutes + 5) % 32))
print("Minutes leftover from 33 minutes - end break", ((work_minutes + 5) % 33))
print("Minutes leftover from 34 minutes - end break", ((work_minutes + 5) % 34))
print("Minutes leftover from 35 minutes - end break", ((work_minutes + 5) % 35))

print("30 minute sections", work_minutes / 30)
print("25 minute sections", work_minutes / 35)
print("hours ", work_minutes // 60)
print("minutes ", work_minutes % 60)

# make method to select session splits
# there will not be a break needed at the end for example: 25work 5break 25work 5break 25work done
# work sessions between 25-30mins and breaks around 5 mins
least_leftover_time = (work_minutes +5) % 30
best_section_time = 30
for i in range(30, 35):
    if least_leftover_time >= ((work_minutes + 5) % (i+1)):
        least_leftover_time = (work_minutes + 5) % (i+1)
        best_section_time = (i+1)

print("least leftover time: ",least_leftover_time)
print("Best Section Time: ", best_section_time)

# method that takes the time sections and puts them in to timed events
work_section = timedelta(minutes = (best_section_time-5))
break_section = timedelta(minutes = best_section_time)
end_section = now + work_section

print("work section time", work_section)
print("break section time", break_section)
print("work_minutes :", work_minutes)
print("Work Sections :", (work_minutes - least_leftover_time + 5)/best_section_time)
total_work_sections = (work_minutes - least_leftover_time + 5)/best_section_time
total_break_sections = int(total_work_sections - 1)
best_break_time = best_section_time - 5


pomodoro_array = []
pomodoro_array.append(0)
temp = 0
#add_min=least_leftover_time//total_work_sections
#remaining_time =  least_leftover_time % total_work_sections
#print(add_min, " ", remaining_time)
for i in range(total_break_sections):
    pomodoro_array.append(best_break_time+temp)
    pomodoro_array.append(best_section_time+temp)
    temp = best_section_time + temp
pomodoro_array.append(work_minutes)


print(pomodoro_array)
# if least_leftover_time != 0:
# if least_leftover_time > total_break_sections:
#  least_leftover_time // total_break_sections


# loop that takes the times and puts them into an array for break and work times
# DO NOT FORGET TO ADD THE REMAINING TIME ONTO THE BREAKS


# use a loop that takes in the starting time and uses wait function in time to time it out an

# method that prints the times and alerts
