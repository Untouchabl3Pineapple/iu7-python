from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from random import randint
import time
import matplotlib.pyplot as plt
from dop import *

def main():
    root = Tk()
    root.geometry("570x420+200+200")
    root.title("Сортировка простыми вставками")
    root.resizable(False, False)

    #______________________Demonstration____________________________________________
    dem_array = Label(root,text = "Демонстрационный массив")
    sorted_array = Label(root,text = "Отсортированный массив")

    entry_dem_array = Entry(root)
    entry_output_sort = Entry(root)

    entry_dem_array.insert(0, "2 -1 100 5 39 2 11")

    dem_array.grid(row = 0, column = 0, sticky = W)
    entry_dem_array.grid(row = 0, column = 1, sticky = W)
    sorted_array.grid(row = 1, column = 0, sticky = W)
    entry_output_sort.grid(row = 1, column = 1, sticky = W)

    sort_dem_ar_button=Button(text="Отсортировать",font="16",pady="8",\
    command = lambda: entry_output_sort.insert(0\
            , insertion_sort(entry_dem_array.get().split()))).place(x = 450, y = 10)
    #______________________________________________________________________________

    #______________________Table____________________________________________________
    def table():
        all_res = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        all_res[0][0] = "Упорядоченный массив"
        all_res[1][0] = "Случайный массив"
        all_res[2][0] = "Упорядоченный в обратном порядке"

        n_1 = entry_n1.get()
        n_2 = entry_n2.get()
        n_3 = entry_n3.get()

        # подготовка массивов
        upor_array_n1 = insertion_sort([randint(-50,50) for i in range(int(n_1))])
        upor_array_n2 = insertion_sort([randint(-50,50) for i in range(int(n_2))])
        upor_array_n3 = insertion_sort([randint(-50,50) for i in range(int(n_3))])

        sluch_array_n1 = [randint(-50,50) for i in range(int(n_1))]
        sluch_array_n2 = [randint(-50,50) for i in range(int(n_2))]
        sluch_array_n3 = [randint(-50,50) for i in range(int(n_3))]

        upor_obratno_n1 = insertion_sort([randint(-50,50) for i in range(int(n_1))])[::-1]
        upor_obratno_n2 = insertion_sort([randint(-50,50) for i in range(int(n_2))])[::-1]
        upor_obratno_n3 = insertion_sort([randint(-50,50) for i in range(int(n_3))])[::-1]

        # упорядоченные
        start_time = time.time()
        insertion_sort(upor_array_n1)
        all_res[0][1] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(upor_array_n2)
        all_res[0][2] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(upor_array_n3)
        all_res[0][3] = "%s" % round((time.time() - start_time), 5)

        # случайные
        start_time = time.time()
        insertion_sort(sluch_array_n1)
        all_res[1][1] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(sluch_array_n2)
        all_res[1][2] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(sluch_array_n3)
        all_res[1][3] = "%s" % round((time.time() - start_time), 5)

        # упорядоченные в обратном порядке
        start_time = time.time()
        insertion_sort(upor_obratno_n1)
        all_res[2][1] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(upor_obratno_n2)
        all_res[2][2] = "%s" % round((time.time() - start_time), 5)

        start_time = time.time()
        insertion_sort(upor_obratno_n3)
        all_res[2][3] = "%s" % round((time.time() - start_time), 5)


        window2 = Tk()
        window2.title('Таблица замеров времени сортировки (c)')
        tree = ttk.Treeview(window2, height=5)
        tree.tag_configure('ttk', background='light gray')

        tree['columns'] = ('one', 'two', 'three', 'four')
        tree.column('#0', width=1, minwidth=1, stretch=NO)
        tree.column('one', width=300, minwidth=300, stretch=NO)
        tree.column('two', width=100, minwidth=100, stretch=NO)
        tree.column('three', width=100, minwidth=100, stretch=NO)
        tree.column('four', width=100, minwidth=100, stretch=NO)

        tree.heading('#0', text='', anchor=CENTER)
        tree.heading('one', text=' ', anchor=CENTER)
        tree.heading('two', text='N1', anchor=CENTER)
        tree.heading('three', text='N2', anchor=CENTER)
        tree.heading('four', text='N3', anchor=CENTER)

        for i in all_res:
            tree.insert('','end',values=(i))

        tree.grid()

    title_build_table = Label(root,text = "Построение таблицы").place(x = 200, y = 100)
    n1 = Label(root,text = "N1 = ").place(x = 0, y = 150)
    n2 = Label(root,text = "N2 = ").place(x = 0, y = 180)
    n3 = Label(root,text = "N3 = ").place(x = 0, y = 210)

    entry_n1 = Entry(root)
    entry_n1.place(height = 20, x = 50, y = 150)
    entry_n2 = Entry(root)
    entry_n2.place(height = 20, x = 50, y = 180)
    entry_n3 = Entry(root)
    entry_n3.place(height = 20, x = 50, y = 210)

    building_table_button = Button(text="Построить",font="20",pady="13",\
                                   command = table).place(x = 320, y = 160)

    #___________________________________________________________________________________________________

    #_______________________________Graph_______________________________________________________________
    def graph():
        plt.xlabel("Количество элементов, шт")
        plt.ylabel("Время сортировки, с")
        plt.title("Сортировка простыми вставками")

        left = int(left_limit_entry.get())
        right = int(right_limit_entry.get())
        step = (right - left) // 10

        x_ax = []
        y_ax = []
        while left != right:
            sluch_array = [randint(-50,50) for i in range(left)]
            start_time = time.time()
            insertion_sort(sluch_array)
            y_ax.append("%s" % round((time.time() - start_time), 3))
            x_ax.append(left)

            left += step

        plt.plot(x_ax,y_ax,label="Функция",color="red")

        plt.grid(True)
        plt.legend(loc="upper right")
        plt.show()

    title_build_graph = Label(root,text = "Построение графика").place(x = 200, y = 300)
    left_limit_title = Label(root,text = "Левая граница").place(x = 0, y = 350)
    right_limit_title = Label(root,text = "Правая граница").place(x = 0, y = 380)

    left_limit_entry = Entry(root)
    left_limit_entry.place(height = 20, x = 120, y = 350)
    right_limit_entry = Entry(root)
    right_limit_entry.place(height = 20, x = 120, y = 380)

    building_graph_button = Button(text="Построить",font="20",pady="13",\
                                   command = graph).place(x = 350, y = 350)


    root.mainloop()

main()