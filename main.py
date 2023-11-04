import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime


def record_expense():
    date = entry_date.get()
    category = entry_category.get()
    description = entry_description.get()
    amount = entry_amount.get()

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    # Clear input fields
    entry_date.delete(0, 'end')
    entry_category.delete(0, 'end')
    entry_description.delete(0, 'end')
    entry_amount.delete(0, 'end')


def generate_report():
    year = int(entry_year.get())
    month = int(entry_month.get())

    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = [row for row in reader if
                    row and datetime.strptime(row[0], '%Y-%m-%d').year == year and datetime.strptime(row[0],
                                                                                                     '%Y-%m-%d').month == month]

    total_expenses = sum(float(row[3]) for row in expenses)

    result_label.config(text=f"Total Expenses: ${total_expenses:.2f}")


app = tk.Tk()
app.title("Expense Tracker")

# Input fields
label_date = tk.Label(app, text="Date (YYYY-MM-DD):")
label_date.pack()
entry_date = tk.Entry(app)
entry_date.pack()

label_category = tk.Label(app, text="Category:")
label_category.pack()
entry_category = tk.Entry(app)
entry_category.pack()

label_description = tk.Label(app, text="Description:")
label_description.pack()
entry_description = tk.Entry(app)
entry_description.pack()

label_amount = tk.Label(app, text="Amount ($):")
label_amount.pack()
entry_amount = tk.Entry(app)
entry_amount.pack()

record_button = tk.Button(app, text="Record Expense", command=record_expense)
record_button.pack()

# Generate report
label_year = tk.Label(app, text="Year:")
label_year.pack()
entry_year = tk.Entry(app)
entry_year.pack()

label_month = tk.Label(app, text="Month (1-12):")
label_month.pack()
entry_month = tk.Entry(app)
entry_month.pack()

report_button = tk.Button(app, text="Generate Report", command=generate_report)
report_button.pack()

# Display result
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()