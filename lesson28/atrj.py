from tkinter import *


def hell_0(event):
    # print("Очередной хеллоу ворлд")
    message = ent.get() #приём значений из ent
    ent.delete(0, END)
    print(message)

    message2 = txt.get(1.0, END)
    txt.delete(0.0, END)
    print(message2)


root = Tk() # создание/инициализация
root.title("Моё первое окно") # название окна
root.geometry("400x500") # размер


lab = Label(root, text="С пасхой!") # привязка к окну, размещение текста
# lab['background'] = "pink" # задать цвет ключевым словом или хекс кодом
# lab['foreground'] = "silver"
# lab["bg"] = "#ad54cc" # сокращение + хекс код
lab.pack() # Размещение


# lab["font"] = 30 # когда стоит 1 значение, воспринимается как размер
# lab["font"] = " Arial 20 italic" # мультзначение строкой
lab["font"] = ("Times New Roman", 30, 'bold', "italic", "overstrike", "underline")  #шрифт, размер, наклон, зачёркнутый, подчёркнутый


btn = Button(root, text="Моя первая кнопка",
             font=20,        # размер текста
             width=20,       # широта
             height=10,      # высота
             borderwidth=10, # ширина рамки bd
            ) # выпуск функции


btn.pack()
btn.bind("<Button-1>", hell_0)
#Button-1 = ЛКМ
#Button-3 = ПКМ
#Double-Button-2 = 2x ЛКМ


ent = Entry(root, bd=10, font=20)
ent.pack()


txt = Text(root, width=20, height=5)
txt.pack()


root.mainloop()  #отобразить окно