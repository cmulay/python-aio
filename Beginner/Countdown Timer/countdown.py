import time


def countdown(_t):
    while _t:
        minutes, seconds = divmod(_t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        _t -= 1
    print('Time\'s Up!!')


t = input("Enter the time in seconds: ")

countdown(int(t))
