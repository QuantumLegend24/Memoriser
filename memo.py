from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.geometry("800x800")
root.title("Memoriser")

def filesave():
    fout=asksaveasfile(defaultextension=".txt")

    if fout is not None:

        for box in listbox.get(0,END):
            print(box.strip(),file=fout)

        listbox.delete(0,END)

def fileadd():
    listbox.insert(END,box.get())
    box.delete(0,END)

def fileopen():
    fin=askopenfile(title="Open file")
    if fin is not None:
        listbox.delete(0,END)

        boxes=fin.readlines()
        for box in boxes:
            listbox.insert(END,box.strip())

def filedelete():
    index=listbox.curselection()
    if index:
        listbox.delete(index)


save=Button(root,text="Save",command=filesave)
save.pack(padx=5,pady=5)

add=Button(root,text="Add",command=fileadd)
add.pack(padx=5,pady=5)

open=Button(root,text="Open",command=fileopen)
open.pack(side=LEFT,padx=5,pady=5)

delete=Button(root,text="Delete",command=filedelete)
delete.pack(side=RIGHT,padx=5,pady=5)

box=Entry(root,width=35)
box.pack(padx=5,pady=5)

frame=Frame(root)

ballscroll=Scrollbar(frame,orient="vertical")
ballscroll.pack(side=RIGHT,fill=Y)

listbox=Listbox(frame,width=70,yscrollcommand=ballscroll.set,bg="red")
for i in range(1,101):
    listbox.insert(END,"LIST"+str(i))

listbox.pack(side=LEFT,padx=5)
ballscroll.config(command=listbox.yview)

frame.pack(side=RIGHT)



root.mainloop()