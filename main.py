import tkinter as tk
from utils import login_util as lu
from views import login_page
from views import main_page

global root
root = tk.Tk()
root.geometry("730x360")  # 设置窗口大小为300x200
root.resizable(False, False)  # 禁止用户改变窗口的大小
root.title("Texas Hold’em poker")

global login_status
login_status=False



login_frame = tk.Frame(root, width=730, height=360)
login_frame.place(x=0, y=0)


main_frame = tk.Frame(root, width=730, height=360)
# main_frame.place(x=0, y=0)

Login_Page = login_page.Login_Page(root, login_frame, main_frame)
Login_Page.login_ui_show((200,60))

# Main_Page = main_page.Main_Page(main_frame)
# Main_Page.table_ui_show()




root.mainloop()