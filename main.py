import tkinter as tk
from tkinter import ttk
import pygame
from tkinter import *
import time as t

def arr_check():
    next(gen)

def clear():
    entry.delete(0, END)
 
def display():  
    global n
    n = entry.get()
    clear()
    next(gen)

def arrange():
    arr = entry.get()
    clear()
    return arr


def prog():
    global n
    print(n)
    for k in range(int(n)):
        if k != 0:
            yield
            arr = lst
            list1 = [str(inp) for inp in arrange().split()]
            print(list1)
            lst = list(set(list1) & set(arr))
        else:
            yield
            list1 = [str(inp) for inp in arrange().split()]
            print(list1)
            lst = list1
    
    ans = ' '.join(lst)
    print(f"Вот пересечение всех множеств: {{{ans}}}")


num = 1
check = False
in_arr = ''
gen = prog()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Cyberpunk 2077 Unreleased OST – The Rebel Path (Cello Version).mp3")
pygame.mixer.music.play()



window = tk.Tk()
window.title('Cyberpunk code generator')
window.geometry('1165x300') #1165x645
bg_img = tk.PhotoImage(file='Johny.png')

label_pic = tk.Label(window, image=bg_img)
label_pic.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.65, anchor='center')







lbl_result = tk.Label(frame, text = f'Введите элементы множества {num} (через пробелы)', font=('Comic Sans MS', 15))
lbl_result.grid(column=1, row=1, padx=10, pady=10)

entry = ttk.Entry()
entry.pack(anchor=CENTER, padx=6, pady=6)

btn_start = tk.Button(frame, text='Done', command=display, font=('Comic Sans MS', 10))
btn_start.grid(column=0, row=3, padx=10, pady=10)

btn_start = tk.Button(frame, text='Arr', command=arr_check, font=('Comic Sans MS', 10))
btn_start.grid(column=2, row=3, padx=10, pady=10)


window.mainloop()