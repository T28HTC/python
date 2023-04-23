from tkinter import *

root = Tk()
root.geometry("200x200")

# def get_rb():
#     if rb_vall.get() == 1:
#         label['text'] = start + " " + rb["text"]
#     elif rb_vall.get() == 2:
#         label['text'] = start + " " + rb1["text"]
#
#
# start = "hello"
# label = Label(root, text=start + " " + "...")
# label.pack()
#
#
# rb_vall = IntVar()
# rb = Radiobutton(root, text="piton", variable=rb_vall,
#                  value=1,
#                  command=get_rb)
# rb.pack()
#
# rb_vall1 = IntVar()
# rb1 = Radiobutton(root, text="world", variable=rb_vall,
#                   value=2,
#                   command=get_rb)
# rb1.pack()
#
# rb.bind("<Button-1>")
# rb1.bind("<Button-1>")

def get_button():
    print(btn_vall.get())
    if btn_vall.get()== True:
        btn1["state"]="normal"
        btn1["text"]="Активен"
    else:
        btn1["state"]=DISABLED
        btn1["text"]="Не активен"

btn_vall = BooleanVar()
btn = Checkbutton(root,
             text="Активировать",
             variable=btn_vall,
             onvalue=True,
             offvalue=False,
             command=get_button)
btn.pack()


btn1 = Button(root, text="Не активен", state=DISABLED)
btn1.pack()

root.mainloop()
#/H5qTkEZF