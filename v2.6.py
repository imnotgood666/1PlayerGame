import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk , Image

class SlotMachine(tk.Frame):
    r=0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Slot Machine")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.numbers_label = tk.Label(self, font=("Arial", 40), text="0 0 0")
        self.numbers_label.pack(pady=20)
        self.imgpath = "C:\\Users\\phant\\OneDrive\\文件\\GitHub\\1PlayerGame\\Gambling_chips.gif"
        self.img = Image.open(self.imgpath)
        self.photo = ImageTk.PhotoImage(self.img)

        

        #self.canvas = tk.Canvas(root, width=20, height=700,bd=0,highlightthickness=0)
        #self.canvas.create_image(700, 500, image=self.photo)
        #self.canvas.pack()
        #self.entry = tk.Entry(root, insertbackground='blue',highlightthickness=2)
        #self.entry.pack()
        #self.canvas.create_window(100, 50 , width = 100, height = 20, window = self.entry)



        self.spin_button = tk.Button(self, text="拉霸", font=("Arial", 16), command=self.spin)
        self.spin_button.pack(pady=20)
    def spin(self):
            a=  random.randint(1, 9)
            b=  random.randint(1, 9)
            c=  random.randint(1, 9)
            nums = [a,b,c]
            
            self.numbers_label.config(text=" ".join(map(str, nums)))
            if SlotMachine.r < 40:

                self.after(35, self.spin)            
                SlotMachine.r=SlotMachine.r+1        
            else:
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
                SlotMachine.r=0


root = tk.Tk()
root.geometry('400x400')
app = SlotMachine(master=root)
app.mainloop()