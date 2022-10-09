from functools import reduce
from tkinter import *
import time
import random

def _file(q):
    for i in q:
        try:
            int(i)
        except ValueError:
            try:
                float(i)
            except ValueError:
                print('Данные некорректны, отредактируйте файл и попробуйте снова!')
                quit()
    if len(q) > 10 ** 6 or len(q) == 0:
        print('Данные некорректны, отредактируйте файл и попробуйте снова!')
        quit()
    return 'Данные корректны, можем продолжать!\n'

def _min(x):
    minimum = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    return minimum

def _max(x):
    maximum = x[0]
    for i in x:
        if i > maximum:
            maximum = i
    return maximum

def _sum(x):
    return reduce(lambda a, b: a + b, x)

def _mult(x):
    return reduce(lambda a, b: a * b, x)

def test(x, y):
    start_time = time.time()
    x(y)
    close_time = time.time()
    return close_time - start_time


def grafic(func):
    lst = []

    tk = Tk()
    tk.configure(bg='white')
    tk.geometry('700x700')

    canvas = Canvas(tk, width=700, height=700, bg="white")
    canvas.pack()

    canvas.create_line(40, 660, 40, 40, width=1, fill="black", arrow=LAST)
    canvas.create_line(40, 660, 660, 660, width=1, fill="black", arrow=LAST)

    canvas.create_oval(50, 100, 50, 100, width=0, fill='black')

    label1 = Label(text='t, миллисекунды', width=13, font=('arial', 8),
            bg='white', fg='black')
    label1.place(x=35, y=10)

    label2 = Label(text='кол-во чисел', width=10, font=('arial', 8),
                   bg='white', fg='black')
    label2.place(x=630, y=640)

    c = 27
    d = 670
    a = 0
    for i in range(13):
        b = 'b' + str(i)

        globals()[b] = Label(text=str(a), width=5, font=('arial', 8), bg='white', fg='black')
        globals()[b].place(x=c, y=d)

        a += 50000
        c += 50
    x = 40

    for i in range(600_000):
        lst.append(i)
        if i % 1_000 == 0:
            x += 1
            start_time = time.time()
            func(lst)
            close_time = time.time()
            y = 640 - (close_time - start_time) * 100000
            canvas.create_oval(x, y, x, y, width=0, fill='black')
            if i % 50_000 == 0 and i < 550_000:
                b = 'b' + str(i)
                globals()[b] = Label(text=str(round((close_time - start_time) * 1_000, 4)), width=5, font=('arial', 8),
                                     bg='white', fg='black')
                globals()[b].place(x=7, y=y)
        if i == 599_999:
            print('Готово!')
    tk.mainloop()
def osip():
    filename = input('Введите имя файла:')
    f = [i for i in open(filename + '.txt', encoding='utf-8').read().split()]
    print(_file(f))
    what_to_do = int(input('Выберите действие:\n1) Применить функцию к входному файлу.\n2) Тест на скорость.\n3) Построить график.\nВвод:'))

    def MinTimeTest():
        return f'10.000 чисел - {test(_min, first_list)}\n500.000 чисел - {test(_min, second_list)}\n10.000.000 чисел - {test(_min, therd_list)}'

    def MaxTimeTest():
        return f'10.000 чисел - {test(_max, first_list)}\n500.000 чисел - {test(_max, second_list)}\n10.000.000 чисел - {test(_max, therd_list)}'

    def SumTimeTest():
        return f'10.000 чисел - {test(_sum, first_list)}\n500.000 чисел - {test(_sum, second_list)}\n10.000.000 чисел - {test(_sum, therd_list)}'

    def MultTimeTest():
        return f'10.000 чисел - {test(_mult, first_list)}\n500.000 чисел - {test(_mult, second_list)}\n10.000.000 чисел - {test(_mult, therd_list)}'
    if what_to_do == 1:
        whatFunc = int(input('Выберите фунцию:\n1) min\n2) max\n3) sum\n4) mult\nВвод:'))
        if whatFunc == 1:
            print(_min(f))
        elif whatFunc == 2:
            print(_max(f))
        elif whatFunc == 3:
            print(_sum(f))
        elif whatFunc == 4:
            print(_mult(f))

    elif what_to_do == 2:
        what_function = int(input('Выберите функцию:\n1) min\n2) max\n3) sum\n4) mult\n\nВвод:'))
        print('Подождите 5 секунд примерно.')
        first_list = []
        second_list = []
        therd_list = []

        for i in range(10_000):
            first_list.append(random.randint(-100, 100))
        for i in range(500_000):
            second_list.append(random.randint(-100, 100))
        for i in range(10_000_000):
            therd_list.append(random.randint(-100, 100))
        if what_function == 1:
            print(MinTimeTest())
        elif what_function == 2:
            print(MaxTimeTest())
        elif what_function == 3:
            print(SumTimeTest())
        elif what_function == 4:
            print(MultTimeTest())

    elif what_to_do == 3:
        what_func = int(input('Выберите функцию:\n1) min\n2) max\n3) sum\n4) mult\nВвод:'))
        print('Нужно немножечко подождать.')
        if what_func == 1:
            grafic(globals()['_min'])
        elif what_func == 2:
            grafic(globals()['_max'])
        elif what_func == 3:
            grafic(globals()['_sum'])
        elif what_func == 4:
            grafic(globals()['_mult'])
if __name__ == '__main__':
    osip()