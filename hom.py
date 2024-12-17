from tkinter import *
import random

root = Tk()
root.geometry("800x800")
root.title("Color generator")


def fileadd():
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "teal", "lime", "navy", "indigo", "violet", "turquoise", "gold", "silver", "beige", "maroon", "peach", "amber", "salmon", "plum", "mint", "emerald", "coral", "ruby", "sapphire", "cream", "ivory","blush", "rose", "bronze", "scarlet", "olive", "tan", "black", "mustard", "aquamarine", "chocolate", "white", "charcoal","amethyst", "sand yellow","cherry", "chartreuse","lavender","sunset orange", "sky blue"]
    random_color = random.choice(colors)
    listbox.insert(END, random_color)


def filedelete():
    index = listbox.curselection()
    if index:
        listbox.delete(index)


add = Button(root, text="Add a random color", command=fileadd)
add.pack(padx=5, pady=5)


delete = Button(root, text="Remove color", command=filedelete)
delete.pack(padx=5, pady=5)

frame = Frame(root)

ballscroll = Scrollbar(frame, orient="vertical")
ballscroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=70, yscrollcommand=ballscroll.set, bg="black")
listbox.pack(side=LEFT, padx=5)
ballscroll.config(command=listbox.yview)

frame.pack(side=RIGHT)


root.mainloop()