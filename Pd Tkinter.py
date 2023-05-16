import tkinter as tk
from tkinter import *
from datetime import datetime

class AgeCalculator:
    def __init__(self, datums):
        self.master = datums
        datums.title("Vecuma Kalkulators")


        self.birthdate_label = tk.Label(datums, text="Ievadi dzimšanas datumu (gggg.mm.dd):")
        self.birthdate_label.grid(row=0, column=0, padx=5, pady=5)
        self.birthdate_entry = tk.Entry(datums)
        self.birthdate_entry.grid(row=0, column=1, padx=5, pady=5)


        self.display_options_label = tk.Label(datums, text="Izvēlies kā parādīt vecumu:")
        self.display_options_label.grid(row=1, column=0, padx=5, pady=5)
        self.display_option = tk.StringVar()
        self.display_option.set("years")

        self.years_radio = tk.Radiobutton(datums, text="Gadi", variable=self.display_option, value="years")
        self.years_radio.grid(row=1, column=1, padx=5, pady=5)

        self.days_radio = tk.Radiobutton(datums, text="Dienas", variable=self.display_option, value="days")
        self.days_radio.grid(row=2, column=1, padx=5, pady=5)

        self.seconds_radio = tk.Radiobutton(datums, text="Sekundes", variable=self.display_option, value="seconds")
        self.seconds_radio.grid(row=3, column=1, padx=5, pady=5)


        self.calculate_button = tk.Button(datums, text="Aprēķini vecumu", command=self.calculate_age)
        self.calculate_button.grid(row=4, column=0, columnspan=4, padx=4, pady=4)


        self.age_label = tk.Label(datums, text="")
        self.age_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def calculate_age(self):
        birthdate_str = self.birthdate_entry.get()
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y.%m.%d").date()
            today = datetime.now().date()
            age = today - birthdate
            if self.display_option.get() == "years":
                age_str = str(age.days // 365) + " years"
            elif self.display_option.get() == "days":
                age_str = str(age.days) + " days"
            else:
                age_str = str(age.total_seconds()) + " seconds"
            self.age_label.config(text=age_str)
        except ValueError:
            self.age_label.config(text="Nepareizs datuma formāts. Lūdzu ievadiet gggg.mm.dd formātā.")

root = tk.Tk()
app = AgeCalculator(root)
root.mainloop()