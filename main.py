from tkinter import *
from first_gui import *
import sqlite3

conn = sqlite3.connect('person.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS liked_food (Name text)")
c.execute("CREATE TABLE IF NOT EXISTS liked_flowers (Name text)")
c.execute("CREATE TABLE IF NOT EXISTS liked_animals (Name text)")

c.execute("CREATE TABLE IF NOT EXISTS unliked_food (Name text)")
c.execute("CREATE TABLE IF NOT EXISTS unliked_flowers (Name text)")
c.execute("CREATE TABLE IF NOT EXISTS unliked_animals (Name text)")
conn.commit()
conn.close()

global root
root = Tk()
photo_image = PhotoImage(file=r"<Type your photo path>")
background_label = Label(root, image=photo_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Person(root)


root.mainloop()
