from tkinter import *
from tkinter import messagebox
import tkinter
import item
import view

main = Tk()
main.title('Calculator')
main.geometry('600x500')

items = []

frame1 = LabelFrame(main, text='Add to the list', padx=5, pady=5)
frame2 = LabelFrame(main, text='List', padx=5, pady=5)

def addToList():
    name = clicked.get()
    count = num.get()
    try: 
        int(count)
        i = item.getItem(name, count)
        if i:
            items.append(i)
        res = str(count) + ' ' + name + '\n'
        textField.insert(END, res)
    except ValueError:
        messagebox.showerror('Error!', 'Invalid quantity!')
    
def clearOutput():
    textField.delete('1.0', 'end')
    items.clear()

def run():
    view.start(items)

options = item.getItemList()

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(frame1, clicked, *options)


num = Entry(frame1)
textField = Text(frame2)

addButton = Button(frame1, text='Add', command=addToList)
delButton = Button(frame2, text='Clear', command=clearOutput)
scr=Scrollbar(frame2, orient=VERTICAL, command=textField.yview)
printButton = Button(frame2, text='Generate', command=run)

num.grid(row=0, column=0)
drop.grid(row=0, column=1)
addButton.grid(row=0, column=2)
frame1.grid(row=0, column=0)
delButton.pack(side=BOTTOM)
printButton.pack(side=BOTTOM)
textField.pack(side = LEFT, fill = BOTH)
scr.pack(side = RIGHT, fill = Y)

frame2.grid(row=1, column=0)

main.mainloop()