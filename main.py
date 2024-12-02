import tkinter as tk
from tkinter import ttk
from tkinter import *
import time as t

def kill():
    window.destroy()

def clear():
    entry.delete(0, END)

def algos():
    global arr
    global lst
    global k
    global txt
    ar = entry.get()
    if ar.split() == []:
        txt = 'Вы ничего не ввели!!!'
    else:
        clear()

        if k != 0:
            arr = lst
            list1 = [str(inp) for inp in ar.split()]
            print(list1)
            lst = list(set(list1) & set(arr))
        else:
            list1 = [str(inp) for inp in ar.split()]
            print(list1)
            lst = list1    
            k += 1

def fin():
    global lst
    global nigg
    nigg = f"Вот пересечение всех множеств: {{{lst}, %}}"
    print(f"Вот пересечение всех множеств: {lst} и пустое множество ")

k = 0
txt = 'ПРОЧТИТЕ README'
nigg = '**Пересечение ваших множеств материализуется здесь**'

window = tk.Tk()
window.title('Cyberpunk code generator')
window.geometry('1165x645') #1165x645
bg_img = tk.PhotoImage(file='Johny.png')

label_pic = tk.Label(window, image=bg_img)
label_pic.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.65, anchor='center')



lbl_result = tk.Label(frame, text = txt, font=('Comic Sans MS', 15))
lbl_result.grid(column=1, row=1, padx=10, pady=10)


btn_start = tk.Button(frame, text='Ввести новый массив', command=algos, font=('Comic Sans MS', 10))
btn_start.grid(column=0, row=2, padx=10, pady=10)

btn_start = tk.Button(frame, text='Я съел все массивы', command=fin, font=('Comic Sans MS', 10))
btn_start.grid(column=2, row=2, padx=10, pady=10)

btn_start = tk.Button(frame, text='Кончить', command=kill, font=('Comic Sans MS', 10))
btn_start.grid(column=1, row=4, padx=10, pady=10)


entry = ttk.Entry()
entry.pack(anchor=CENTER, padx=6, pady=50)

lbl_result = tk.Label(frame, text = nigg, font=('Comic Sans MS', 12))
lbl_result.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()





