import numpy as np
import win32api, win32con

screen_size = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

def trigger_check(box_arr):
    print('trigger check')

    # the range the center can be between should increase as the box gets bigger
    x_offset = (box_arr[2] - box_arr[0]) / 2
    y_offset = (box_arr[3] - box_arr[1]) / 2

    print(x_offset)
    print(y_offset)

    # check if box is closes to center of screen
    x_range = (screen_size[0] / 2) - x_offset, (screen_size[0] / 2) + x_offset
    y_range = (screen_size[1] / 2) - y_offset, (screen_size[1] / 2) + y_offset
    box_center = (box_arr[0] + box_arr[2]) / 2, (box_arr[1] + box_arr[3]) / 2

    print(x_range, y_range)
    print(box_center)

    if box_center[0] < x_range[1] and box_center[0] > x_range[0] and box_center[1] < y_range[1] and box_center[1] > y_range[0]:
        print('bang!')
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return True

    
def between(x, y, num):
    return x <= num <= y
