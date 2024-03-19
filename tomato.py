from datetime import datetime


def twelveHour(stop_hour, stop_minute):
    now = datetime.now()
    print(now)
    current_hour = now.hour
    if current_hour > 12:
        current_hour = current_hour - 12
    now_total_minutes = (current_hour * 60) + now.minute
    end_total_minutes = (stop_hour * 60) + stop_minute

    if now_total_minutes < end_total_minutes:
        work_minutes = end_total_minutes - now_total_minutes
    else:
        work_minutes = (720 - now_total_minutes) + end_total_minutes
    return work_minutes


def sectionTime(work_minutes):
    least_leftover_time = (work_minutes + 5) % 30
    best_section_time = 30
    for i in range(30, 35):
        if least_leftover_time >= ((work_minutes + 5) % (i + 1)):
            least_leftover_time = (work_minutes + 5) % (i + 1)
            best_section_time = i + 1

    print("least leftover time: ", least_leftover_time)
    print("Best Section Time: ", best_section_time)
    return least_leftover_time, best_section_time


def totalSections(work_minutes, least_leftover_time, best_section_time):
    total_work_sections = (work_minutes - least_leftover_time + 5) / best_section_time
    return total_work_sections


def fillArray(
    work_minutes, least_leftover_time, best_section_time, total_work_sections
):
    # does not add the on the time if least_leftover_time//total_work_sections > 1
    total_break_sections = int(total_work_sections - 1)
    best_break_time = best_section_time - 5
    pomodoro_array = []
    pomodoro_array.append(0)
    temp = 0
    # add_min=least_leftover_time//total_work_sections
    remaining_time = least_leftover_time % total_work_sections
    # print(add_min, " ", remaining_time)
    for i in range(total_break_sections):
        if remaining_time == 0:
            pomodoro_array.append(best_break_time + temp)
            pomodoro_array.append(best_section_time + temp)
            temp = best_section_time + temp
        else:
            pomodoro_array.append(best_break_time + temp + 1)
            pomodoro_array.append(best_section_time + temp + 1)
            temp = best_section_time + temp + 1
            remaining_time = remaining_time - 1
    pomodoro_array.append(work_minutes)
    return pomodoro_array


def main():
    stop_hour = int(input("Enter your stopping hour: "))
    stop_minute = int(input("Enter your stopping minute: "))
    work_time = twelveHour(stop_hour, stop_minute)
    least_leftover_time, best_section_time = sectionTime(work_time)
    print(work_time)
    total_work_sections = totalSections(
        work_time, least_leftover_time, best_section_time
    )
    pomodoro_array = fillArray(
        work_time, least_leftover_time, best_section_time, total_work_sections
    )
    print(pomodoro_array)

    # print("Minutes leftover from 30 minutes - end break", ((work_time + 5) % 30))


# print("Minutes leftover from 31 minutes - end break", ((work_time + 5) % 31))
# print("Minutes leftover from 32 minutes - end break", ((work_time + 5) % 32))
# print("Minutes leftover from 33 minutes - end break", ((work_time + 5) % 33))
# print("Minutes leftover from 34 minutes - end break", ((work_time + 5) % 34))
# print("Minutes leftover from 35 minutes - end break", ((work_time + 5) % 35))

if __name__ == "__main__":
    main()
