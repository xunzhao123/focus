import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up!')
    # 在 Linux/MacOS 中使用
    #os.system('notify-send "Time is up!"')
    # 在 Windows 中使用
    #os.system('msg * Time is up!')

def main():
    print("Welcome to Focus Timer")
    minutes = int(input("Enter the number of minutes to focus: "))
    countdown(minutes)

if __name__ == "__main__":
    main()
