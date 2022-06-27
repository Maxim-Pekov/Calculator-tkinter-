import tkinter as tk

win = tk.Tk()
win.title('КАЛЬКУЛЯТОР')

win.geometry('300x300+1520+100')
win.config(bg='black')
win.grid_columnconfigure(0, minsize=80)
win.grid_columnconfigure(1, minsize=80)
win.grid_columnconfigure(2, minsize=80)
win.grid_columnconfigure(3, minsize=60)
win.grid_rowconfigure(0, minsize=80)
entry1 = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20, 'bold'), bg='black', fg='yellow')
entry1.insert(0, '0')
entry1.grid(row=0, column=0, sticky='wens', columnspan=4)


def entry_insert(digit):
    if entry1.get() == '0':
        entry1.delete(0, tk.END)
    lenght_entry = len(entry1.get())

    entry1.insert(lenght_entry, digit)

def entry_insert_event(digit):
    lenght_entry = len(entry1.get())
    x = entry1.get()
    if lenght_entry == 1 and x == digit:
        entry1.delete(0, tk.END)

    entry1.delete(lenght_entry-1, tk.END)
    entry1.insert(lenght_entry, digit)

def entry_simbol(simbol):
    value = entry1.get()
    if value[-1].isdigit():
        entry1.delete(0, tk.END)
        try:
            entry1.insert(0, round(eval(value)))
        except (ZeroDivisionError, TypeError, SyntaxError):
            entry1.delete(0, tk.END)
            entry1.insert((0, 0))
    if value[-1] in '+-*/':
        value = value[:-1]
        entry1.delete(len(value), tk.END)
    entry1.insert(len(value), simbol)

def entry_simbol_event(simbol):
    value = entry1.get()
    entry1.delete(len(value)-1, tk.END)
    val = entry1.get()
    if val[-1] in '+-*/':
        val = val[:-1]
        entry1.delete(len(val), tk.END)
    v  = entry1.get()
    entry1.delete(0, tk.END)
    entry1.insert(0, str(eval(v))+simbol)

def result():
    value = entry1.get()
    entry1.delete(0, tk.END)
    try:
        entry1.insert(0, round(eval(value)))
    except (ZeroDivisionError, TypeError, SyntaxError):
        entry1.delete(0, tk.END)
        entry1.insert((0, '0'))


def c():
    entry1.delete(0, tk.END)
    entry1.insert(0, '0')


def create_btn(digi):
    return tk.Button(win, text=digi, bd=5, font=('Arial', 15, 'bold'), activebackground="yellow",
                     command=lambda: entry_insert(digi))


def add_simbol(simbol):
    value = entry1.get()
    return tk.Button(win, text=simbol, bd=5, activebackground="yellow", font=('Arial', 15, 'bold'), bg='green',
                     command=lambda: entry_simbol(simbol))


def create_btn_result(digi):
    return tk.Button(win, text=digi, font=('Arial', 15, 'bold'), bd=5, fg='green', activebackground="yellow",
                     command=lambda: result())


def create_btn_c(digi):
    return tk.Button(win, text=digi, font=('Arial', 15, 'bold'), bd=5, bg='red', fg='white', activebackground="yellow",
                     command=lambda: c())


def press_key(event):
    c = entry1.get()
    if event.char.isdigit():
        g = event.char
        entry_insert_event(g)
    elif event.char in '+-*/':
        entry_simbol_event(event.char)
    elif event.char in '\r':
        result()

def LKM(event):
    if entry1.get() == '0' or ntry1.get() == 0:
        entry1.delete(0, tk.END)
win.bind('<Key>', press_key)

entry1.bind('<Button-1>', LKM)

create_btn(1).grid(row=1, column=0, sticky='we', padx=8, pady=2)
create_btn(2).grid(row=1, column=1, sticky='we', padx=8, pady=2)
create_btn(3).grid(row=1, column=2, sticky='we', padx=8, pady=2)
create_btn(4).grid(row=2, column=0, sticky='we', padx=8, pady=2)
create_btn(5).grid(row=2, column=1, sticky='we', padx=8, pady=2)
create_btn(6).grid(row=2, column=2, sticky='we', padx=8, pady=2)
create_btn(7).grid(row=3, column=0, sticky='we', padx=8, pady=2)
create_btn(8).grid(row=3, column=1, sticky='we', padx=8, pady=2)
create_btn(9).grid(row=3, column=2, sticky='we', padx=8, pady=2)
create_btn(0).grid(row=4, column=0, sticky='we', padx=8, pady=2)
add_simbol('+').grid(row=1, column=3, sticky='we', padx=8, pady=2)
add_simbol('-').grid(row=2, column=3, sticky='we', padx=8, pady=2)
add_simbol('*').grid(row=3, column=3, sticky='we', padx=8, pady=2)
add_simbol('/').grid(row=4, column=3, sticky='we', padx=8, pady=2)
create_btn_c('C').grid(row=4, column=1, sticky='we', padx=8, pady=2)
create_btn_result('=').grid(row=4, column=2, sticky='we', padx=8, pady=2)

win.mainloop()
