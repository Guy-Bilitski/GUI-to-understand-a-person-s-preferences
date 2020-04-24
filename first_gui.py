from tkinter import *
from tkinter import messagebox
import sqlite3


class Person:
    def __init__(self, master):
        # Likes

        # Frame creation
        self._top_frame = Frame(master)
        self._top_frame.pack(side=TOP, anchor=W)
        self._bottom_frame = Frame(master)
        self._bottom_frame.pack(side=LEFT, anchor=S)

        # Headline preferences
        self._preferences_head_line = Label(
            self._top_frame, text="Person's preferences", bg="light salmon", fg="firebrick")
        self._preferences_head_line.grid(row=0, column=1)

        # liked_food
        self._liked_food_label = Label(self._top_frame, text="Liked food")
        self._liked_food_label.grid(row=2)
        self._entry_liked_food = Entry(self._top_frame)
        self._entry_liked_food.grid(row=3)
        self._button_insert_liked_food = Button(self._top_frame, text="Insert",
                                                command=lambda: self.insert_to_table(table="liked_food"))
        self._button_insert_liked_food.grid(row=4)
        self._button_delete_liked_food = Button(self._top_frame, text="Delete",
                                                command=lambda: self.delete_from_table(table="liked_food"))
        self._button_delete_liked_food.grid(row=5)
        self._button_query_liked_food = Button(self._top_frame, text="Show food",
                                               command=lambda: self.query_table(table="liked_food"))
        self._button_query_liked_food.grid(row=6)

        # liked_flowers
        self._liked_flowers_label = Label(self._top_frame, text="Liked flowers")
        self._liked_flowers_label.grid(row=2, column=1)
        self._entry_liked_flowers = Entry(self._top_frame)
        self._entry_liked_flowers.grid(row=3, column=1)
        self._button_insert_liked_flower = Button(self._top_frame, text="Insert",
                                                  command=lambda: self.insert_to_table(table="liked_flowers"))
        self._button_insert_liked_flower.grid(row=4, column=1)
        self._button_delete_liked_flower = Button(self._top_frame, text="Delete",
                                                  command=lambda: self.delete_from_table(table="liked_flowers"))
        self._button_delete_liked_flower.grid(row=5, column=1)
        self._button_query_liked_flowers = Button(self._top_frame, text="Show flowers",
                                                  command=lambda: self.query_table(table="liked_flowers"))
        self._button_query_liked_flowers.grid(row=6, column=1)

        # liked_animals
        self._liked_animals_label = Label(self._top_frame, text="Liked animals")
        self._liked_animals_label.grid(row=2, column=2)
        self._entry_liked_animals = Entry(self._top_frame)
        self._entry_liked_animals.grid(row=3, column=2)
        self._button_insert_liked_animals = Button(self._top_frame, text="Insert",
                                                   command=lambda: self.insert_to_table(table="liked_animals"))
        self._button_insert_liked_animals.grid(row=4, column=2)
        self._button_delete_liked_animals = Button(self._top_frame, text="Delete",
                                                   command=lambda: self.delete_from_table(table="liked_animals"))
        self._button_delete_liked_animals.grid(row=5, column=2)
        self._button_query_liked_animals = Button(self._top_frame, text="Show animals",
                                                  command=lambda: self.query_table(table="liked_animals"))
        self._button_query_liked_animals.grid(row=6, column=2)

        # Showing the tables
        self._liked_flowers_table = StringVar()
        self._liked_food_table = StringVar()
        self._liked_animals_table = StringVar()
        self._liked_food_query_label = Label(self._top_frame, textvariable=self._liked_food_table)
        self._liked_food_query_label.grid(row=8, column=0)
        self._liked_flowers_query_label = Label(self._top_frame, textvariable=self._liked_flowers_table)
        self._liked_flowers_query_label.grid(row=8, column=1)
        self._liked_animals_query_label = Label(self._top_frame, textvariable=self._liked_animals_table)
        self._liked_animals_query_label.grid(row=8, column=2)

        # Unlikes

        # Headline Unlike
        self._unlike_head_line = Label(self._bottom_frame, text="person's unliked", bg="light salmon", fg="firebrick")
        self._unlike_head_line.grid(row=0, column=1)

        # unliked_food
        self._unliked_food_label = Label(self._bottom_frame, text="Food")
        self._unliked_food_label.grid(row=2)
        self._entry_unliked_food = Entry(self._bottom_frame)
        self._entry_unliked_food.grid(row=3)
        self._button_insert_unliked_food = Button(self._bottom_frame, text="Insert",
                                                  command=lambda: self.insert_to_table(table="unliked_food"))
        self._button_insert_unliked_food.grid(row=4)
        self._button_delete_unliked_food = Button(self._bottom_frame, text="Delete",
                                                  command=lambda: self.delete_from_table(table="unliked_food"))
        self._button_delete_unliked_food.grid(row=5)
        self._button_query_unliked_food = Button(self._bottom_frame, text="Show food",
                                                 command=lambda: self.query_table(table="unliked_food"))
        self._button_query_unliked_food.grid(row=6)

        # liked_flowers
        self._unliked_flowers_label = Label(self._bottom_frame, text="Flowers")
        self._unliked_flowers_label.grid(row=2, column=1)
        self._entry_unliked_flowers = Entry(self._bottom_frame)
        self._entry_unliked_flowers.grid(row=3, column=1)
        self._button_insert_unliked_flower = Button(self._bottom_frame, text="Insert",
                                                    command=lambda: self.insert_to_table(table="unliked_flowers"))
        self._button_insert_unliked_flower.grid(row=4, column=1)
        self._button_delete_unliked_flower = Button(self._bottom_frame, text="Delete",
                                                    command=lambda: self.delete_from_table(table="unliked_flowers"))
        self._button_delete_unliked_flower.grid(row=5, column=1)
        self._button_query_unliked_flowers = Button(self._bottom_frame, text="Show flowers",
                                                    command=lambda: self.query_table(table="unliked_flowers"))
        self._button_query_unliked_flowers.grid(row=6, column=1)

        # liked_animals
        self._unliked_animals_label = Label(self._bottom_frame, text="Animals")
        self._unliked_animals_label.grid(row=2, column=2)
        self._entry_unliked_animals = Entry(self._bottom_frame)
        self._entry_unliked_animals.grid(row=3, column=2)
        self._button_insert_unliked_animals = Button(self._bottom_frame, text="Insert",
                                                     command=lambda: self.insert_to_table(table="unliked_animals"))
        self._button_insert_unliked_animals.grid(row=4, column=2)
        self._button_delete_unliked_animals = Button(self._bottom_frame, text="Delete",
                                                     command=lambda: self.delete_from_table(table="unliked_animals"))
        self._button_delete_unliked_animals.grid(row=5, column=2)
        self._button_query_unliked_animals = Button(self._bottom_frame, text="Show animals",
                                                    command=lambda: self.query_table(table="unliked_animals"))
        self._button_query_unliked_animals.grid(row=6, column=2)

        # Showing the tables
        self._unliked_flowers_table = StringVar()
        self._unliked_food_table = StringVar()
        self._unliked_animals_table = StringVar()
        self._unliked_food_query_label = Label(self._bottom_frame, textvariable=self._unliked_food_table)
        self._unliked_food_query_label.grid(row=8, column=0)
        self._unliked_flowers_query_label = Label(self._bottom_frame, textvariable=self._unliked_flowers_table)
        self._unliked_flowers_query_label.grid(row=8, column=1)
        self._unliked_animals_query_label = Label(self._bottom_frame, textvariable=self._unliked_animals_table)
        self._unliked_animals_query_label.grid(row=8, column=2)



    def insert_to_table(self, table):
        conn = sqlite3.connect('person.db')
        c = conn.cursor()
        if table == "liked_food":
            if not is_in_table(table=table, name=self._entry_liked_food.get()):
                if self._entry_liked_food.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_liked_food.get()})
                    self._entry_liked_food.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_liked_food.get(), table))
                self._entry_liked_food.delete(0, END)

        if table == "liked_flowers":
            if not is_in_table(table=table, name=self._entry_liked_flowers.get()):
                if self._entry_liked_flowers.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_liked_flowers.get()})
                    self._entry_liked_flowers.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_liked_flowers.get(), table))
                self._entry_liked_flowers.delete(0, END)

        if table == "liked_animals":
            if not is_in_table(table=table, name=self._entry_liked_animals.get()):
                if self._entry_liked_animals.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_liked_animals.get()})
                    self._entry_liked_animals.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_liked_animals.get(), table))
                self._entry_liked_animals.delete(0, END)

        if table == "unliked_food":
            if not is_in_table(table=table, name=self._entry_unliked_food.get()):
                if self._entry_unliked_food.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_unliked_food.get()})
                    self._entry_unliked_food.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_unliked_food.get(), table))
                self._entry_unliked_food.delete(0, END)

        if table == "unliked_flowers":
            if not is_in_table(table=table, name=self._entry_unliked_flowers.get()):
                if self._entry_unliked_flowers.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_unliked_flowers.get()})
                    self._entry_unliked_flowers.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_unliked_flowers.get(), table))
                self._entry_unliked_flowers.delete(0, END)

        if table == "unliked_animals":
            if not is_in_table(table=table, name=self._entry_unliked_animals.get()):
                if self._entry_unliked_animals.get() not in ["", " "]:
                    sql_string = "INSERT INTO " + table + " VALUES (:table)"
                    c.execute(sql_string, {"table": self._entry_unliked_animals.get()})
                    self._entry_unliked_animals.delete(0, END)
            else:
                messagebox.showinfo("Error", "You already have {} in {}".format(self._entry_liked_animals.get(), table))
                self._entry_unliked_animals.delete(0, END)

        conn.commit()
        conn.close()


    def query_table(self, table):
        conn = sqlite3.connect('person.db')
        c = conn.cursor()
        sql_string = "SELECT * FROM " + table
        c.execute(sql_string)
        print_records = ""
        ok = True
        for i, record in enumerate(c.fetchall()):
            if i % 2 != 0:
                print_records += ", " + str(record[0]) + "\n"
            else:
                print_records += "," + str(record[0])
        if table == "liked_food":
            self._liked_food_table.set(print_records)
        if table == "liked_flowers":
            self._liked_flowers_table.set(print_records)
        if table == "liked_animals":
            self._liked_animals_table.set(print_records)
        if table == "unliked_food":
            self._unliked_food_table.set(print_records)
        if table == "unliked_flowers":
            self._unliked_flowers_table.set(print_records)
        if table == "unliked_animals":
            self._unliked_animals_table.set(print_records)

        conn.commit()
        conn.close()


    def delete_from_table(self, table):
        conn = sqlite3.connect('person.db')
        c = conn.cursor()
        sql_string = "DELETE FROM " + table + " WHERE Name == (:entry)"
        if table == "liked_food":
            c.execute(sql_string, {"entry": self._entry_liked_food.get()})
            self._entry_liked_food.delete(0, END)

        if table == "liked_flowers":
            c.execute(sql_string, {"entry": self._entry_liked_flowers.get()})
            self._entry_liked_flowers.delete(0, END)

        if table == "liked_animals":
            c.execute(sql_string, {"entry": self._entry_liked_animals.get()})
            self._entry_liked_animals.delete(0, END)

        if table == "unliked_food":
            c.execute(sql_string, {"entry": self._entry_unliked_food.get()})
            self._entry_unliked_food.delete(0, END)

        if table == "unliked_flowers":
            c.execute(sql_string, {"entry": self._entry_unliked_flowers.get()})
            self._entry_unliked_flowers.delete(0, END)

        if table == "unliked_animals":
            c.execute(sql_string, {"entry": self._entry_unliked_animals.get()})
            self._entry_unliked_animals.delete(0, END)

        conn.commit()
        conn.close()


def is_in_table(table, name):
    conn = sqlite3.connect("person.db")
    c = conn.cursor()
    sql_string = "SELECT * FROM " + table
    c.execute(sql_string)
    for flower in c.fetchall():
        if flower[0] == name:
            conn.close()
            return True
    conn.close()
    return False
