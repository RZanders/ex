# import requests

# response = requests.get('http://universities.hipolabs.com/search?country=Latvia')

# response = response.json()

# names = []
# for school in response:
#     names.append(school["name"])

# names.sort()
# print(names)

# from tkinter import *

# def func():
#     value = inputField.get()
#     outputField.config(text=value)

# window = Tk()
# window.geometry("400x400")
# window.title("Gay")
# window.config(background="brown")
# window.resizable(False, False)

# inputField = Entry(window, font = ("Calibri", 20))
# inputField.place(x=10, y=10)

# Button = Button(text = "Print", command=lambda:func())
# Button.place(x=10, y=50)

# outputField = Label(text = "Izvade")
# outputField.place(x=10, y=80)

# window.mainloop()

# import sqlite3

# conn = sqlite3.connect("datasheet.db")
# cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, name VARCHAR, surname VARCHAR)")
# conn.commit()

# name = input("vards: ")
# surname = input("uzvards: ")

# cursor.execute("INSERT INTO persons (name, surname) VALUES(?, ?)", (name, surname))
# conn.commit()