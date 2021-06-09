from tkinter import Tk, Canvas, PhotoImage, mainloop
from PIL import ImageGrab
import time

height = 1080
width = 1920

window = Tk()
canvas = Canvas(window, bg="#c3cace", height=height, width=width)
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")
window.overrideredirect(1)


def recaman():
    arr = []
    result = 0

    for i in range(0, width):
        if (result - i) > 0:
            result -= i
        else:
            result += i
        arr.append(result)

    return arr


def paint():
    arr_x = recaman()
    for i in range(0, len(arr_x)):
        if arr_x[i] % 7 == 0:
            for j in range(0, 30):
                img.put("#ce9695", (i + j, (250 + arr_x[i]) % height))
                img.put("#9b7882", (i + j, (242 + arr_x[i]) % height))
                img.put("#9b7882", (i + j, (236 + arr_x[i]) % height))
                img.put("#ce9695", (i + j, (214 + arr_x[i]) % height))
        elif arr_x[i] % 5 == 0:
            for k in range(0, 12):
                img.put("#57586c", (i + k, (320 + arr_x[i]) % height))
                img.put("#57586c", (i + k, (336 + arr_x[i]) % height))
                img.put("#57586c", (i + k, (380 + arr_x[i]) % height))
                img.put("#57586c", (i + k, (388 + arr_x[i]) % height))
        elif arr_x[i] % 3 == 0:
            img.put("#a39caa", (i, (490 + arr_x[i]) % height))
        else:
            for m in range(0, 8):
                img.put("#9b7882", (i + m, (118 + arr_x[i]) % height))

    for a in range(len(arr_x)-1, -1, -1):
        for b in range(20, 30):
            img.put("#9b7882", ((a + arr_x[a]) % width, ((a * b) % height)))
        for c in range(10, 20):
            img.put("#a39caa", ((a + arr_x[a]) % width, ((a * c) % height)))


paint()
canvas.update()
time.sleep(1)

#ImageGrab.grab((0, 0, width, height)).save('gen_art.jpg')
window.mainloop()


