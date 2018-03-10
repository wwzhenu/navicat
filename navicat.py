from tkinter import *
from tkinter import ttk
from tkinter import Label
from manageWindow import manageWindow
from manageSqlite import *


def test(event,data):
    print(data)


root = Tk()
root.title("Mysql管理工具")
mw = manageWindow()
"""
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size = '%dx%d+%d+%d' % (screenwidth, screenheight, 0, 0)
root.geometry(size)
"""
# 以最大化打开
root.state("zoomed")
root.iconbitmap("resource\img\ico.ico")

menus = Menu()
menu_file = Menu()
menu_edit = Menu()
menus.add_cascade(menu=menu_file, label='文件')
menus.add_cascade(menu=menu_edit, label='编辑')
menu_file.add_command(label='新建连接', command=mw.showCreateConnect)

root['menu'] = menus

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=5, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=1)

ms = manageSqlite()
data = ms.showConnect()
ttk.Label(mainframe, text='test').grid(column=1, row=1, sticky=(W, E))
if data.__len__() == 0:
    pass
else:
    i = 1
    for d in data:
        d = dict(d)
        lb = ttk.Label(mainframe, text=d['name'])
        lb.bind('<Double-Button-1>', lambda event:test(event,d))
        lb.grid(column=1, row=i, sticky=(W, E))
        i = i + 1

root.mainloop()
