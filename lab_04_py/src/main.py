from tkinter import *
from tkinter.messagebox import showinfo

def main():
    root = Tk()
    root.geometry("700x700+200+200")
    root.title("Построение треугольника с максимальной площадью")
    root.resizable(False, False)
    
    # _______________________Взаимодействие на холсте_______________________________
    
    coord = []
    
    def delete_all():
        coord.clear()
        canvas.delete("all")
    
    def dots_building():
        try:
            x_a = entry_x_array.get().split()
            y_a = entry_y_array.get().split()
            
            if len(x_a) != len(y_a):
                privet = mir
                
            for i in range(len(x_a)):
                coord.append([int(x_a[i]), int(y_a[i])])
                canvas.create_oval(int(x_a[i]), int(y_a[i]),\
                int(x_a[i])+7, int(y_a[i])+7, fill="black")
        except:
            showinfo(message = "Проверьте правильность координат точек!")
            delete_all()
            
    def triange_building():
        if len(coord) < 3:
            showinfo(message = "Указано меньше трех точек!")
        else:
            s_coord = []
            for i in range(len(coord)):
                for j in range(i + 1, len(coord)):
                    for k in range(j + 1, len(coord)):
                        x1 = coord[i][0]
                        x2 = coord[j][0]
                        x3 = coord[k][0]
                        y1 = coord[i][1]
                        y2 = coord[j][1]
                        y3 = coord[k][1]
                        s = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
                        s_coord.append([s, [x1, x2, x3], [y1, y2, y3]])
            ind = 0
            max = s_coord[ind][0]
            
            for i in range(len(s_coord)):
                if s_coord[i][0] > max:
                    max = s_coord[i][0]
                    ind = i
                    
            if max != 0:
                canvas.create_line(s_coord[ind][1][0], s_coord[ind][2][0],\
                s_coord[ind][1][1], s_coord[ind][2][1])
                canvas.create_line(s_coord[ind][1][1], s_coord[ind][2][1],\
                s_coord[ind][1][2], s_coord[ind][2][2])
                canvas.create_line(s_coord[ind][1][2], s_coord[ind][2][2],\
                s_coord[ind][1][0], s_coord[ind][2][0])
            else:
                showinfo(message = "Проверьте правильность координат точек!")
                delete_all()
                
    canvas = Canvas(root, width=694, height=494, bg = "gray", cursor = "pencil")
    canvas.place(x = 0, y = 200)
    
    def click(event):
        x = event.x
        y = event.y
        coord.append([x,y])
        r = 2
        canvas.create_oval(x-r, y-r, x+r, y+r, width=4)
     
    canvas.bind('<1>',click)
                
    # __________________________________________________________________________
    
    #______________________________Расположение кнопок__________________________
            
    x_array = Label(root,text = "Координаты x ( через пробел )").place(x = 130, y = 10)
    y_array = Label(root,text = "Координаты y ( через пробел )").place(x = 130, y = 50)

    entry_x_array = Entry(root)
    entry_y_array = Entry(root)
    
    dots_button = Button(text="Построить точки",font="20",pady="20",\
    command = dots_building).place(x = 130, y = 110)
    building_triangle_button = Button(text="Нарисовать треугольник",font="20",pady="20",\
    command = triange_building).place(x = 255, y = 110)
    clear_button = Button(text="Очистить холст",font="20",pady="20",\
    command = delete_all).place(x = 430, y = 110)

    entry_x_array.place(height = 25, x = 350, y = 10)
    entry_y_array.place(height = 25, x = 350, y = 50)
    
    # __________________________________________________________________________
    
    root.mainloop()

main()

