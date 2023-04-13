import pydirectinput
import numpy as np

mouse_sens = 2.11
max_sens = 8

auto_fire_after_snap = False

def aim_check(box_arr, listener):
  # This is similar to trigger bot, but this time we drag the mouse to towards the closest box

  # Get the center of the box
  box_center = (box_arr[0] + box_arr[2]) / 2, (box_arr[1] + box_arr[3]) / 2

  # Mouse pos is always the center of the screen
  mouse_pos = (1920 / 2, 1080 / 2)

  # Calculate the distance between the mouse and the box
  distance = (box_center[0] - mouse_pos[0], box_center[1] - mouse_pos[1])

  # Duration will depend on how far it is
  duration = np.linalg.norm(distance) / 1000

  # If too far, don't move the mouse
  if abs(distance[0]) > 80 and abs(distance[1]) > 80:
    return False
  
  # Multiply distances because mouse sensitivity
  distance = (distance[0] * (max_sens - (mouse_sens + 2)), distance[1] * (max_sens - (mouse_sens + 2)))

  # If the center is close enough, we don't need to move
  if abs(distance[0]) < 20 and abs(distance[1]) < 20:
    return False

  # Supress mouse events so we don't mess up the aiming
  listener.supress = True

  # Move the mouse towards the box
  pydirectinput.moveTo(int(distance[0] + mouse_pos[0]), int(distance[1] + mouse_pos[1]), duration=duration, disable_mouse_acceleration=False)

  if auto_fire_after_snap:
    pydirectinput.mouseDown(button='left')
    pydirectinput.mouseUp(button='left')
  
  # Unsupress mouse events
  listener.supress = False

  return True