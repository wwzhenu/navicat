from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
from manageDb import connectTest
from manageSqlite import *


class manageWindow:

    # root = None
    # connectName = None
    # connectHost = None
    # connectPort = None
    # connectUsername = None
    # connectPwd = None
    # testResult = None
    # test = None

    def showCreateConnect(self):
        self.root = Toplevel()
        self.root.title("新建连接")
        self.root.iconbitmap("resource\img\ico.ico")
        self.center_window(self.root, 400, 400)
        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=5, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=2)
        mainframe.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="连接名").grid(column=1, row=1, sticky=(W, E))
        self.connectName = ttk.Entry(mainframe)
        self.connectName.grid(column=2, row=1)

        ttk.Label(mainframe, text="主机名或IP地址").grid(column=1, row=2, sticky=(W, E))
        self.connectHost = ttk.Entry(mainframe)
        self.connectHost.grid(column=2, row=2)

        ttk.Label(mainframe, text="端口").grid(column=1, row=3, sticky=(W, E))
        self.connectPort = ttk.Entry(mainframe)
        self.connectPort.grid(column=2, row=3)

        ttk.Label(mainframe, text="用户名").grid(column=1, row=4, sticky=(W, E))
        self.connectUsername = ttk.Entry(mainframe)
        self.connectUsername.grid(column=2, row=4)

        ttk.Label(mainframe, text="密码").grid(column=1, row=5, sticky=(W, E))
        self.connectPwd = ttk.Entry(mainframe, show="*")
        self.connectPwd.grid(column=2, row=5)

        ttk.Button(mainframe, text="测试", command=self.testConnect).grid(column=1, row=6, sticky=(W, E))
        self.testResult = ttk.Label(mainframe)
        self.testResult.grid(column=2, row=6, sticky=(W, E))

        ttk.Button(mainframe, text="确定", command=self.saveConnect).grid(column=3, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="取消", command=self.root.destroy).grid(column=4, row=6, sticky=(W, E))

        self.root.mainloop()

    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def testConnect(self):
        host = self.connectHost.get()
        port = self.connectPort.get()
        if port is None:
            port = 3306
        if len(port) == 0:
            port = 3306
        username = self.connectUsername.get()
        pwd = self.connectPwd.get()
        result = connectTest(host, port, username, pwd)
        if result is True:
            result = "连接成功"
        else:
            result = "连接失败"
        self.testResult.configure(text=result)

    def saveConnect(self):
        name = self.connectName.get()
        host = self.connectHost.get()
        port = self.connectPort.get()
        if port is None:
            port = 3306
        if len(port) == 0:
            port = 3306
        username = self.connectUsername.get()
        pwd = self.connectPwd.get()
        result = connectTest(host, port, username, pwd)
        port = int(port)
        if result is True:
            ms = manageSqlite()
            ms.addConnect(name, host, port, username, pwd)
        else:
            result = "连接失败"
            self.testResult.configure(text=result)
