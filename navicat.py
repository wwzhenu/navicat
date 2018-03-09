from tkinter import *
from manageWindow import showCreateConnect

root = Tk()
root.title("Mysql管理工具")
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
menu_file.add_command(label='新建连接', command=showCreateConnect)

root['menu'] = menus

root.mainloop()
