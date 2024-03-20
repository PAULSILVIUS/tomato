from pomodoroTimer import PomodoroTimer

def main():
    stop_hour = int(input("Enter your stopping hour: "))
    stop_minute = int(input("Enter your stopping minute: "))
    pomodoro_timer = PomodoroTimer(stop_hour, stop_minute)
    print(pomodoro_timer.pomodoro_array)
    print(pomodoro_timer.current_time)
    pomodoro_timer.start_timer()

if __name__ == "__main__":
    main()
