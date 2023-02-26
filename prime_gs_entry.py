import tkinter as tk
import mysql.connector
from datetime import datetime

window = tk.Tk()
window.title("Prime GS")
window.geometry("300x300")

name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

units_label = tk.Label(window, text="Units Purchased:")
units_label.pack()
units_entry = tk.Entry(window)
units_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

mode_label = tk.Label(window, text="Mode of Payment:")
mode_label.pack()
mode_entry = tk.Entry(window)
mode_entry.pack()

#  MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="linuxsucks",
    database="prime_gs"
)
mycursor = mydb.cursor()


# save the data to the database
def save_data():
    name = name_entry.get()
    units = units_entry.get()
    amount = amount_entry.get()
    mode = mode_entry.get()

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    sql = "INSERT INTO prime_gs (name, units_purchased, amount, mode_of_payment, datetime) VALUES (%s, %s, %s, %s, %s)"
    val = (name, units, amount, mode, dt_string)
    mycursor.execute(sql, val)
    mydb.commit()

    name_entry.delete(0, tk.END)
    units_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    mode_entry.delete(0, tk.END)
    confirmation_label.config(text="Data saved successfully!")


# save the data
save_button = tk.Button(window, text="Save", command=save_data)
save_button.pack()


# erase all entries from the database
def erase_all():
    # Delete all rows from the table
    sql = "DELETE FROM prime_gs"
    mycursor.execute(sql)
    mydb.commit()
    confirmation_label.config(text="All entries erased!")


erase_all_button = tk.Button(window, text="Erase All", command=erase_all)
erase_all_button.pack()

confirmation_label = tk.Label(window, text="")
confirmation_label.pack()

# Run the Tkinter event loop
window.mainloop()
