import time
import threading
import tkinter as tk
from tkinter import messagebox

class RestReminder:
    def __init__(self):
        # 初始化主窗口
        self.root = tk.Tk()
        self.root.title("休息提醒程序")
        self.root.geometry("300x150")
        
        # 标签显示倒计时
        self.label = tk.Label(self.root, text="等待启动...", font=('Helvetica', 18))
        self.label.pack(pady=20)
        
        # 按钮启动提醒
        self.start_button = tk.Button(self.root, text="启动提醒", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        # 按钮停止提醒
        self.stop_button = tk.Button(self.root, text="停止提醒", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10)
        
        # 初始化变量
        self.interval = 90 * 60  # 90分钟转换为秒
        self.reminder_time = 20 * 60  # 20分钟转换为秒
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)  # 禁用启动按钮
            self.stop_button.config(state=tk.NORMAL)  # 启用停止按钮
            self.label.config(text="程序已启动，等待90分钟...")
            self.thread = threading.Thread(target=self.remind_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)  # 启用启动按钮
        self.stop_button.config(state=tk.DISABLED)  # 禁用停止按钮
        self.label.config(text="程序已停止...")
        if self.thread is not None:
            self.thread.join()

    def remind(self):
        # 弹出提醒窗口
        messagebox.showinfo("休息提醒", "休息20分钟！")
        # 倒计时显示休息时间
        for i in range(self.reminder_time, -1, -1):
            mins, secs = divmod(i, 60)
            time_format = f"{mins:02}:{secs:02}"
            self.label.config(text=f"休息中... {time_format}")
            self.root.update()
            time.sleep(1)
        self.label.config(text="等待90分钟...")

    def remind_loop(self):
        while self.running:
            # 倒计时显示等待时间
            for i in range(self.interval, -1, -1):
                mins, secs = divmod(i, 60)
                time_format = f"{mins:02}:{secs:02}"
                self.label.config(text=f"等待90分钟... {time_format}")
                self.root.update()
                time.sleep(1)
            self.remind()  # 发出休息提醒

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    reminder = RestReminder()
    reminder.run()
