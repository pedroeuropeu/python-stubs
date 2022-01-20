#Import tkinter library
from tkinter import *
from pynput import mouse


def on_click(x, y, button, pressed):
   if button == mouse.Button.left:
      print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
      return False  # Returning False if you need to stop the program when Left clicked.
   else:
      print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))


listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()

#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("1920x1080")
def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
win.bind('<Motion>',callback)
win.mainloop()