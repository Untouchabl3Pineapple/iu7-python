from tkinter import *
from tkinter.messagebox import showinfo
from dop import *

def main():
    root = Tk()
    root.geometry("485x400+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)

    entry = Entry(root)
    entry.place(width = 485, height = 150, x = 0, y = 0)

    def bin_to_dec():
        try:
            for i in entry.get():
                if i != '1' and i != '0' and i != '.' and i != '-':
                    showinfo(message = "Введите корректные данные!")
                    return entry.delete(0, END)

            if '.' in entry.get():
                res = bin_to_deсfloat(entry.get())
            else:
                res = bin_to_decint(entry.get())

            entry.delete(0, END)
            entry.insert(len(entry.get()), res)
        except:
            showinfo(message = "Введите корректные данные!")
            return entry.delete(0, END)

    def dec_to_bin():
        try:
            if '.' in entry.get():
                res = dec_to_binfloat(entry.get())
            else:
                res = dec_to_binint(entry.get())

            entry.delete(0, END)
            entry.insert(len(entry.get()), res)
        except:
            showinfo(message = "Введите корректные данные!")
            return entry.delete(0, END)

    zero_button = Button(text = "0", height = "5", width = "12", command = \
        lambda: entry.insert(len(entry.get()), "0")).place(x = 274, y = 316)
    one_button = Button(text = "1", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "1")).place(x = 0, y = 150)
    two_button = Button(text = "2", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "2")).place(x = 90, y = 150)
    three_button = Button(text = "3", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "3")).place(x = 180, y = 150)
    four_button = Button(text = "4", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "4")).place(x = 0, y = 233)
    five_button = Button(text = "5", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "5")).place(x = 90, y = 233)
    six_button = Button(text = "6", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "6")).place(x = 180, y = 233)
    seven_button = Button(text = "7", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "7")).place(x = 0, y = 316)
    eight_button = Button(text = "8", height = "5", width = "10", command = \
        lambda: entry.insert(len(entry.get()), "8")).place(x = 90, y = 316)
    nine_button = Button(text = "9", height = "5", width = "10", command = \
        lambda : entry.insert(len(entry.get()), "9")).place(x = 180, y = 316)
    bin_to_dec_button = Button(text = "2>>10", height = "5", width = "12", \
                               command = bin_to_dec).place(x = 274, y = 150)
    dec_to_bin_button = Button(text = "10>>2", height = "5", width = "12", \
                               command = dec_to_bin).place(x = 380, y = 150)
    delete_last_el_button = Button(text = "Удаление\nпоследнего\nэлемента", \
            height = "5", width = "12", command = \
    lambda : entry.delete(len(entry.get()) - 1, END)).place(x = 380, y = 316)
    comma_button = Button(text = ",", height = "5", width = "12", command = \
        lambda : entry.insert(len(entry.get()), ".")).place(x = 274, y = 233)
    minus_button = Button(text = "-", height = "5", width = "12", command = \
        lambda : entry.insert(len(entry.get()), "-")).place(x = 380, y = 233)

    menu_bar = Menu(root)
    root.config(menu = menu_bar)
    file_menu = Menu(menu_bar)
    file_menu.add_command(label = "Повтор последнего действия", command = \
        lambda : entry.insert(len(entry.get()), entry.get()[-1]))
    file_menu.add_command(label = "Очистка поля ввода", command = \
        lambda : entry.delete(0, END))
    file_menu.add_command(label = "Информация об авторе", command = \
        lambda : showinfo(message = "Разработчик: Артемьев Илья Олегович ИУ7-23Б"))
    menu_bar.add_cascade(label="File", menu=file_menu)


    root.mainloop()

main()
