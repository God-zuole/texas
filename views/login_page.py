import requests
import tkinter as tk
from utils import image_util 
from utils import login_util
from views import main_page

class Login_Page():
    def __init__(self, root, login_frame, main_frame):
        self.root = root
        self.login_frame = login_frame
        self.main_frame = main_frame

    def hide_label(self, label):
        label.place_forget()

    def login(self, coordinate):
        username = username_entry.get()
        password = password_entry.get()
        if (not username) or (not password):
            login_status_msg = "账号/密码不能为空!"
        else:
            Login_Util = login_util.Login_Util()
            # login_result = Login_Util.login(username, password)
            login_result = "Login s"
            if "Login failed" == login_result:
                login_status = False
                login_status_msg = "登陆失败:账号或密码错误!"
            else:
                login_status = True
                login_status_msg = "登陆成功!"
                self.login_frame.destroy()  # 隐藏登录页面
                # 显示主页面
                main_frame = tk.Frame(self.root, width=730, height=360)
                main_frame.place(x=0, y=0)
                Main_Page = main_page.Main_Page(main_frame)
                Main_Page.table_ui_show()

                # self.main_frame = tk.Frame(self.root)
                # self.main_frame.pack()

                # self.welcome_label = tk.Label(self.main_frame, text="Welcome to the main page!")
                # self.welcome_label.pack()

        if self.login_frame.winfo_exists():
            login_status_label = tk.Label(self.login_frame, text=login_status_msg)
            login_status_label.place(x=coordinate[0], y=coordinate[1])
            self.root.update()
            self.root.after(5000, lambda: self.hide_label(login_status_label))

    def logout(self):
        login_status = False

    def clear_entry(self, username_entry, password_entry):
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)    


    def login_ui_show(self, coordinate):
        canvas = tk.Canvas(self.login_frame, width=250, height=200)
        canvas.place(x=coordinate[0], y=coordinate[1])
        canvas.create_rectangle(4, 4, 230, 180, fill="", width=4)

        login_status_label = tk.Label(self.login_frame, text="登陆系统")
        login_status_label.place(x=coordinate[0]+80, y=coordinate[1]+10)

        logo_size = 30
        ImageUtil = image_util.ImageUtil(self.login_frame)
        ImageUtil.image_show("./icons/user.png", (logo_size,logo_size), "user", (coordinate[0]+20,coordinate[1]+60))
        ImageUtil.image_show("./icons/pwd.png", (logo_size,logo_size), "pwd", (coordinate[0]+20,coordinate[1]+100))
        global username_entry
        global password_entry
        username_entry = tk.Entry(self.login_frame, width=12, font=("Arial", 18))
        username_entry.place(x=coordinate[0]+55, y=coordinate[1]+60)
        password_entry = tk.Entry(self.login_frame, show="*", width=12, font=("Arial", 18))
        password_entry.place(x=coordinate[0]+55, y=coordinate[1]+100)

        # 创建一个按钮，当被点击时删除Entry中的所有输入
        button = tk.Button(self.login_frame, text="清空", command=lambda: self.clear_entry(username_entry, password_entry), width=6, height=1)
        button.place(x=coordinate[0]+30, y=coordinate[1]+140)
        button = tk.Button(self.login_frame, text="登陆", command=lambda: self.login((coordinate[0] + 55, coordinate[1] + 30)), width=6, height=1)
        button.place(x=coordinate[0]+150, y=coordinate[1]+140)