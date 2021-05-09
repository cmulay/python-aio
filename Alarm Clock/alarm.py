import math
import tkinter
import beepy

print('Classic Beepy Timer')


def counter(count):
    secs = math.floor(count % 60)
    mins = math.floor((count / 60) % 60)
    hrs = math.floor((count / 3600))
    label['text'] = f'Hours: {str(hrs)} Minutes: {str(mins)} Seconds: {str(secs)}'

    if count >= 0:
        gui_window.after(1000, counter, count - 1)
    else:
        for _ in range(3):
            beepy.beep(sound=1)
            print('Alarm Ringing')
        label['text'] = 'Time is up!'


def button():
    hours, minutes, seconds = get_hours.get(), get_minutes.get(), get_seconds.get()
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        counter(time)


# GUI
gui_window = tkinter.Tk()
gui_window.title('Classic Beepy Timer')
gui_window.geometry('400x300')

label_hours = tkinter.Label(gui_window, text='Hours:')
get_hours = tkinter.Entry(gui_window)
label_minutes = tkinter.Label(gui_window, text='Minutes:')
get_minutes = tkinter.Entry(gui_window)
label_second = tkinter.Label(gui_window, text='Seconds:')
get_seconds = tkinter.Entry(gui_window)

label_hours.grid(row=1, column=1)
get_hours.grid(row=1, column=2)
label_minutes.grid(row=2, column=1)
get_minutes.grid(row=2, column=2)
label_second.grid(row=3, column=1)
get_seconds.grid(row=3, column=2)

label = tkinter.Label(gui_window)
label.grid(row=5, column=2)

button = tkinter.Button(gui_window, text='Set Timer', command=button)
button.grid(row=4, column=2)

gui_window.mainloop()
