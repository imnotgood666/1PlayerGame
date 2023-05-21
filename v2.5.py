import tkinter as tk
from tkinter import messagebox
import random

class SlotMachine(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Slot Machine")
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.numbers_label = tk.Label(self, font=("Arial", 40), text="0 0 0")
        self.numbers_label.pack(pady=20)


        self.spin_button = tk.Button(self, text="拉霸", font=("Arial", 16), command=self.spin)
        self.spin_button.pack(pady=10)

    def spin(self):
      
        nums = [random.randint(1, 9) for i in range(3)]

        self.numbers_label.config(text=" ".join(map(str, nums)))


        if all(num == 1 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！一元復始")
        if all(num == 2 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！成雙成對")
        if all(num == 3 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！三生三世")
        if all(num == 4 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！四氣大盛")
        if all(num == 5 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！五福臨門")
        if all(num == 6 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！溜溜溜")
        if all(num == 7 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！森戚戚")
        if all(num == 8 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！八寶粥")
        if all(num == 9 for num in nums):
            messagebox.showinfo("Congratulations!", "贏了！ 大贏!天長地久")


root = tk.Tk()
app = SlotMachine(master=root)
app.mainloop()
