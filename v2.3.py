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
        self.numbers_label = tk.Label(self, font=("Arial", 40), text="0 0 0")
        self.numbers_label.pack(pady=20)
        self.spin_button = tk.Button(self, text="拉杆", font=("Arial", 16), command=self.spin)
        self.spin_button.pack(pady=10)

    def spin(self):
        nums = [random.randint(1, 9) for i in range(3)]
        self.numbers_label.config(text=" ".join(map(str, nums)))

        
        if 6 in nums:
            tk.messagebox.showinfo("Congratulations!", "特殊獎！")


root = tk.Tk()

app = SlotMachine(master=root)
app.mainloop()
