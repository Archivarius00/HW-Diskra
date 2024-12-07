import tkinter as tk
from tkinter import ttk

def kill():
    window.destroy()

def clear_entry():
    """Очистить поле ввода."""
    entry.delete(0, tk.END)

def clear_lists():
    """Очистить введённые множества."""
    global entered_sets, k, lst
    entered_sets.clear()
    k = 0
    lst = []
    update_display()
    lbl_result.config(text="Пересечение ваших множеств будет отображено здесь")


def algos():
    """Функция для обработки введённых данных и вычисления пересечения."""
    global arr, lst, k, txt
    ar = entry.get()
    if not ar.strip():
        txt = 'Вы ничего не ввели!'
        lbl_result.config(text=txt)
    else:
        clear_entry()
        if k != 0:
            arr = lst
            list1 = [str(inp) for inp in ar.split()]
            lst = list(set(list1) & set(arr))
        else:
            list1 = [str(inp) for inp in ar.split()]
            lst = list1
            k += 1
        update_display(list1)

def fin():
    """Функция для вывода финального пересечения."""
    global lst, nigg
    if lst:
        lst = sorted(lst)
        nigg = f"Пересечение всех множеств:  {{∅, {', '.join(lst)}}}"
    else:
        nigg = "Пересечение всех множеств: {∅}"
    lbl_result.config(text=nigg)

def update_display(current_list=None):
    """Обновляет отображение всех введённых множеств."""
    if current_list is not None:
        entered_sets.append(current_list)
    display_text = "\n".join(
        [f"Множество {i + 1}: {{ {', '.join(map(str, s))} }}" for i, s in enumerate(entered_sets)]
    )
    txt_display.config(state=tk.NORMAL)
    txt_display.delete(1.0, tk.END)
    txt_display.insert(tk.END, display_text)
    txt_display.config(state=tk.DISABLED)


# Глобальные переменные
k = 0
arr = []
lst = []
entered_sets = []  # Список всех введённых множеств

# Создание окна
window = tk.Tk()
window.title('Пересечение множеств')
window.geometry('1280x720')
window.resizable(False, False)


img = tk.PhotoImage(file="flowers2.png")
background_label = tk.Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Фон и интерфейс
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.60, anchor='center')



# Поле для отображения введённых множеств с прокруткой
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

txt_display = tk.Text(window, height=10, width=50, font=('Century Gothic', 12), yscrollcommand=scrollbar.set)
txt_display.pack(pady=10)
txt_display.config(state=tk.DISABLED)
scrollbar.config(command=txt_display.yview)
txt_display.place(relx=0.518, rely=0.3, anchor=tk.CENTER)

# Поле для ввода
entry = ttk.Entry()
entry.pack(anchor=tk.CENTER, padx=6, pady=20)
entry.place(relx=0.518, rely=0.47, anchor=tk.CENTER)

# Кнопки
btn_add = tk.Button(frame, text='Завершить ввод множества', command=algos, font=('Georgia', 10))
btn_add.grid(column=0, row=2, padx=10, pady=10)

btn_calc = tk.Button(frame, text='Посчитать пересечение', command=fin, font=('Georgia', 10))
btn_calc.grid(column=1, row=2, padx=10, pady=10)

btn_clear = tk.Button(frame, text='Очистить множества', command=clear_lists, font=('Georgia', 10))
btn_clear.grid(column=2, row=2, padx=10, pady=10)

btn_exit = tk.Button(frame, text='Выйти', command=kill, font=('Georgia', 10))
btn_exit.grid(column=1, row=4, padx=10, pady=10)

# Поле для вывода результата
lbl_result = tk.Label(frame, text="Пересечение ваших множеств будет отображено здесь", font=('Georgia', 12))
lbl_result.grid(column=1, row=3, padx=10, pady=10)


window.mainloop()
