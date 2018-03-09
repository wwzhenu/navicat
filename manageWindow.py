from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
from manageDb import connectTest

connectName = StringVar()
connectHost = StringVar()
connectPort = StringVar()
connectUsername = StringVar()
connectPwd = StringVar()
testResult = StringVar()


def showCreateConnect():
    root = Tk()
    root.title("新建连接")
    root.iconbitmap("resource\img\ico.ico")
    center_window(root, 400, 400)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=5, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=2)
    mainframe.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="连接名").grid(column=1, row=1, sticky=(W, E))
    ttk.Entry(mainframe, textvariable=connectName).grid(column=2, row=1)

    ttk.Label(mainframe, text="主机名或IP地址").grid(column=1, row=2, sticky=(W, E))
    ttk.Entry(mainframe, textvariable=connectHost).grid(column=2, row=2)

    ttk.Label(mainframe, text="端口").grid(column=1, row=3, sticky=(W, E))
    ttk.Entry(mainframe, textvariable=connectPort).grid(column=2, row=3)

    ttk.Label(mainframe, text="用户名").grid(column=1, row=4, sticky=(W, E))
    ttk.Entry(mainframe, textvariable=connectUsername).grid(column=2, row=4)

    ttk.Label(mainframe, text="密码").grid(column=1, row=5, sticky=(W, E))
    ttk.Entry(mainframe, textvariable=connectPwd, show="*").grid(column=2, row=5)

    ttk.Button(mainframe, text="测试", command=testConnect).grid(column=1, row=6, sticky=(W, E))
    ttk.Label(mainframe, textvariable=testResult).grid(column=2, row=6, sticky=(W, E))

    root.mainloop()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


def testConnect(*args):
    host = connectHost.get()
    port = connectPort.get()
    username = connectUsername
    pwd = connectPwd
    connectTest(host, port, username, pwd)
    testResult.set('成功啦')
