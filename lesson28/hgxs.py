from tkinter import *

# root = Tk()
# root.geometry("250x500")
# lab = Label(root, text="zuila", font=20)
# lab.pack()
#
# ent = Entry(root, font=20, width=24)
# ent.pack()
#
# btn1 = Button(root, width=30, bg="red")
# btn1.pack()
# btn2 = Button(root, width=30, bg="orange")
# btn2.pack()
# btn3 = Button(root, width=30, bg="yellow")
# btn3.pack()
# btn4 = Button(root, width=30, bg="green")
# btn4.pack()
# btn5 = Button(root, width=30, bg="azure")
# btn5.pack()
# btn6 = Button(root, width=30, bg="blue")
# btn6.pack()
# btn7 = Button(root, width=30, bg="violet")
# btn7.pack()
#
# root.mainloop()


#2

# def udalyalka(event):
#     message=ent.get()
#     ent.delete(0, END)
#     print(message)
#
#     message2 = txt.get(1.0, END)
#     txt.delete(0.0, END)
#     print(message2)
#
# root = Tk()
# root.geometry("300x300")
# root["bg"] = "#C0C0C0"
# lab = Label(root,text="Ваш адрес: ", bg="#FFDAB9")
# lab.pack()
#
# ent= Entry(root, width=30,bd=5)
# ent.pack()
#
# lab1 = Label(root,text="комментарий: ")
# lab1.pack()
#
# txt = Text(root, width=25, bd=5, height=5)
# txt.pack()
#
# btn = Button(root, text="Отправить", bg="azure", width=30,bd=5)
# btn.pack()
#
#
# btn.bind("<Button-1>", udalyalka)

# root.mainloop()

#3

def jirnyi(event):
    lab["font"] = "Arial 15 bold"

def dushni(event):
    lab['font'] = ("Times New Roman", 30, 'bold', "italic")

def jirnyi1(event):
    lab['font'] = ("Times New Roman", 30, "overstrike", "underline")

root = Tk()
root.geometry("300x300")
root["bg"] = "#C0C0C0"


lab = Label(root, text=" С пасхой, пупсик")
lab.pack()

lab.bind("<Button-1>", jirnyi)
lab.bind("<Double-Button-1>",jirnyi1)
lab.bind("<Button-3>", dushni)


root.mainloop()







