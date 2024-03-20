import datetime
import time

class PomodoroTimer:
    def __init__(self, stop_hour, stop_minute):
        self.stop_hour = stop_hour
        self.stop_minute = stop_minute
        self.current_time = self.calculate_current_time()
        self.pomodoro_array = self.calculate_pomodoro_array()
        self.current_index = 0
        self.is_break = False

    def calculate_current_time(self):
        now = datetime.datetime.now()
        current_hour = now.hour if now.hour <= 12 else now.hour - 12
        now_total_minutes = (current_hour * 60) + now.minute
        end_total_minutes = (self.stop_hour * 60) + self.stop_minute

        if now_total_minutes < end_total_minutes:
            work_minutes = end_total_minutes - now_total_minutes
        else:
            work_minutes = (720 - now_total_minutes) + end_total_minutes

        return work_minutes

    def calculate_pomodoro_array(self):
        work_minutes = self.current_time
        least_leftover_time = (work_minutes + 5) % 30
        best_section_time = 30
        for i in range(30, 35):
            if least_leftover_time >= ((work_minutes + 5) % (i + 1)):
                least_leftover_time = (work_minutes + 5) % (i + 1)
                best_section_time = i + 1

        total_work_sections = (work_minutes - least_leftover_time + 5) // best_section_time
        total_break_sections = int(total_work_sections - 1)
        best_break_time = best_section_time - 5
        pomodoro_array = [0]
        temp = 0
        remaining_time = least_leftover_time % total_work_sections

        for _ in range(total_break_sections):
            if remaining_time == 0:
                pomodoro_array.append(best_break_time + temp)
                pomodoro_array.append(best_section_time + temp)
                temp += best_section_time
            else:
                pomodoro_array.append(best_break_time + temp + 1)
                pomodoro_array.append(best_section_time + temp + 1)
                temp += best_section_time + 1
                remaining_time -= 1

        pomodoro_array.append(work_minutes)
        return pomodoro_array

    def start_timer(self):
        while self.current_index < len(self.pomodoro_array) - 1:
            self.run_pomodoro()

    def run_pomodoro(self):
        start_time = self.pomodoro_array[self.current_index]
        end_time = self.pomodoro_array[self.current_index + 1]
        duration = end_time - start_time

        if self.is_break:
            print(f"Break time! Take a break for {duration} minutes.")
        else:
            print(f"Work time! Focus for {duration} minutes.")

        self.countdown(duration)
        self.is_break = not self.is_break
        self.current_index += 1

    def countdown(self, duration):
        while duration:
            mins, secs = divmod(duration, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(2)
            duration -= 1

        print("Time's up!")
