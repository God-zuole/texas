import tkinter as tk

def check_frame_exists(frame):
    try:
        # 尝试访问frame的一个属性，如果frame存在，这不会引发异常
        frame.winfo_exists()
        return True
    except AttributeError:
        # 如果frame已经被销毁，访问其属性会引发AttributeError
        return False

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

# 检查frame是否存在
print(check_frame_exists(frame))  # 输出: True

# 销毁frame
frame.destroy()

# 再次检查frame是否存在
print(check_frame_exists(frame))  # 输出: False