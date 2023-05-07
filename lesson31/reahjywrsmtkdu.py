from tkinter import *
x = 0
root = Tk()
root.geometry("400x400")

c = Canvas(root, width=300, height=300, bg="silver")
c.pack(anchor=CENTER, expand=True)
# img = PhotoImage(file="ty.png")
# c.create_text(250, 250, text=x, font="verdana 50")
# c.create_image(245, 230, image=img)
#
#
# def timer():
#     global x
#     x = x+1
#     c.after(1000, timer)
#     c.delete("all")
#     c.create_text(250, 250, text=x, font="verdana 50")
#     c.create_image(245, 230, image=img)
#
# c.after(1000, timer)

btn = Button(root, text="Повернуть адольфика")
btn.pack()

l = None
p = None


def lkm(adolf):
    global l
    l = (adolf.x, adolf.y)

def pkm(adolf):
    global p
    p = (adolf.x, adolf.y)

def cam():
    c.delete('all')
    c.create_line(l[0], l[1],
                  p[0], p[1])

c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)


root.mainloop()