import tkinter as tk


def Print_min(Medicine_name):
    window = tk.Tk()
    window.title("לשים לב")

    Result_label = tk.Label(window, text = "הגיע למינימום", font=("calibre",18, "bold"))
    Result_label.grid(row=0,column=1)

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=2,column=0)

    window.mainloop()

def Print_Expired(Medicine_name):
    window = tk.Tk()
    window.title("לשים לב")

    Result_label = tk.Label(window, text = "פג תוקף", font=("calibre",18, "bold"))
    Result_label.grid(row=0,column=1)

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=2,column=0)

    window.mainloop()

def Print_Executed():
    window = tk.Tk()
    window.title("בוצע")

    Executed_label = tk.Label(window, text = "בוצע", font=("calibre",18, "bold"))
    Executed_label.grid(row=0,column=1)

    window.mainloop()

