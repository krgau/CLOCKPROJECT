import tkinter as tk
from time import strftime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("420x180")
        self.root.configure(bg="#111111")

        self.time_label = tk.Label(
            self.root,
            font=("Arial", 46, "bold"),
            fg="#00ff99",
            bg="#111111",
            text="",
        )
        self.time_label.pack(anchor="center", pady=(30, 5))

        self.date_label = tk.Label(
            self.root,
            font=("Arial", 18),
            fg="#d9d9d9",
            bg="#111111",
            text="",
        )
        self.date_label.pack(anchor="center")

        self.update_clock()

    def update_clock(self):
        current_time = strftime("%H:%M:%S")
        current_date = strftime("%A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
