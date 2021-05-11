from tkinter import *
import threading
import time
from tkinter import messagebox
import pyautogui
import numpy as np
import cv2

class Tracker(threading.Thread):

  def __init__(self, *args, **kwargs):
    super(Tracker, self).__init__(*args, **kwargs)
    self.__flag = threading.Event() # The flag used to pause the thread
    self.__flag.set() # Set to True
    self.__running = threading.Event() # Used to stop the thread identification
    self.__running.set() # Set running to True

  def run(self):
    while self.__running.isSet():
      self.__flag.wait() # return immediately when it is True, block until the internal flag is True when it is False
      #print(time.time())
      img = pyautogui.screenshot()
      cv_img = np.array(img)
      cv_img = cv_img[:, :, ::-1].copy()
      cv2.imshow('ok', cv_img)
      cv2.waitKey(10)
      #time.sleep(0.01)

  def pause(self):
    self.__flag.clear() # Set to False to block the thread

  def resume(self):
    self.__flag.set() # Set to True, let the thread stop blocking

  def stop(self):
    self.__flag.set() # Resume the thread from the suspended state, if it is already suspended
    self.__running.clear() # Set to False


def clicked():
  if btn['text'] == 'Start Tracker':
    x.pause()
    btn['text'] = 'Stop Tracker'
  else:
    x.resume()
    btn['text'] = 'Start Tracker'

def onClose():
  if messagebox.askokcancel("Quit", "Do you want to quit?"):
    x.stop()
    time.sleep(1)
    window.destroy()

if __name__ == "__main__":

  window = Tk()
  window.title("Tracking App")
  window.geometry('350x200')
  window.protocol("WM_DELETE_WINDOW", onClose)
  btnText = 'Start Tracker'
  # status = True
  x = Tracker()
  x.start() #x.start, pause, resume, stop
  btn = Button(window, text=btnText, command=clicked)
  btn.grid(column=0,row=0)

  window.mainloop()
