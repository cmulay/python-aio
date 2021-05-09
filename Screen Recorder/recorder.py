import datetime
import numpy as np
import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics

get_width = GetSystemMetrics(0)
get_height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (get_width, get_height))

webcam = cv2.VideoCapture(0)

while True:
    capture_screen = ImageGrab.grab(bbox=(0, 0, get_width, get_height))
    img_np = np.array(capture_screen)
    main_capture = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    main_capture[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
    cv2.imshow('Secret Capture', main_capture)

    captured_video.write(main_capture)
    if cv2.waitKey(10) == ord('q'):
        break
