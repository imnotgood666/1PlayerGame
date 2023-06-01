import tkinter as tk
import random

class SlotMachine(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Slot Machine")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建显示数字的标签
        self.numbers_label = tk.Label(self, font=("Arial", 40), text="0 0 0")
        self.numbers_label.pack(pady=20)

        # 创建拉杆按钮
        self.spin_button = tk.Button(self, text="拉杆", font=("Arial", 16), command=self.spin)
        self.spin_button.pack(pady=10)

    def spin(self):
        # 随机生成三个数字
        nums = [random.randint(1, 9) for i in range(3)]
        # 显示生成的数字
        self.numbers_label.config(text=" ".join(map(str, nums)))

        # 如果其中所有数字都是 6，则显示获得特殊奖励的消息框
        if all(num == 6 for num in nums):
            tk.messagebox.showinfo("Congratulations!", "您获得了特殊奖励！")

# 创建主窗口
root = tk.Tk()
# 创建 SlotMachine 对象并运行
app = SlotMachine(master=root)
app.mainloop()
