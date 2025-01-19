import tkinter as tk
from tkinter import messagebox

booked_tables = [False] * 20  

discount = 0
bill = None
billnet = None
discount_label = None

def enable_order():
    for entry in entries:
        entry.config(state=tk.NORMAL)

def disable_order():
    for entry in entries:
        entry.config(state=tk.DISABLED)

def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

def clear_bill_labels():
    global bill, billnet, discount_label
    if bill:
        bill.destroy()
    if discount_label:
        discount_label.destroy()
    if billnet:
        billnet.destroy()

def calculate():
    global discount, bill, discount_label, billnet
    
    dic = {
        'Aloo Paratha': [entries[0], 30],
        'Samosa': [entries[1], 15],
        'Pizza': [entries[2], 150],
        'Gulab Jamun': [entries[3], 35],
        'Chowmein': [entries[4], 70],
        'Churma': [entries[5], 200]
    }
    total = 0
    net = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total = total + int(val[0].get()) * val[1]
    if total >= 1000:
        discount = 10
    elif total >= 500:
        discount = 5
    
    else:
        discount = 1
    
    
    clear_bill_labels()
    
    bill = tk.Label(bill_frame, text="Total Bill: Rs. " + str(total), font=('Arial', 14), bg='lightgrey')
    bill.pack(pady=5)
    
    
    discount_label = tk.Label(bill_frame, text="Discount: " + str(discount) + "%", font=('Arial', 14), bg='lightgrey')
    discount_label.pack(pady=5)
   

    net = total - (total * discount) / 100
    
    
    billnet = tk.Label(bill_frame, text="Net Amount: Rs. " + str(net), font=('Arial', 16), fg="blue", bg='lightgrey')
    billnet.pack(pady=5)
    
def leave_table(table_idx=None):
    global booked_tables, table_buttons
    if table_idx is None:
        last_booked_table = None
        for idx, booked in enumerate(reversed(booked_tables)):
            if booked:
                last_booked_table = 19 - idx
                break

        if last_booked_table is None:
            messagebox.showinfo(title="No Tables Booked", message="No tables are currently booked.")
            return
        else:
            table_idx = last_booked_table
    
    booked_tables[table_idx] = False
    table_buttons[table_idx].config(bg="green")
    enable_order()
    clear_entries()
    messagebox.showinfo(title="Table Freed", message=f"Table {table_idx + 1} has been freed.")

def book_specific_table(table_idx):
    global booked_tables
    if booked_tables[table_idx]:
        messagebox.showinfo(title="Table Already Booked", message="The table is already booked!")
    else:
        booked_tables[table_idx] = True
        table_buttons[table_idx].config(bg="red")
        enable_order()  
        clear_entries()
        messagebox.showinfo(title="Table Booked", message=f"Table {table_idx + 1} has been booked.")

def book_table():
    specific_table_idx = specific_table_entry.get()
    if specific_table_idx:
        specific_table_idx = int(specific_table_idx) - 1
        if specific_table_idx < 0 or specific_table_idx >= 20:
            messagebox.showinfo(title="Invalid Table", message="Please enter a valid table number (1-20).")
        else:
            book_specific_table(specific_table_idx)
    else:
        for i, booked in enumerate(booked_tables):
            if not booked:
                book_specific_table(i)
                return
        messagebox.showinfo(title="No Tables Available", message="All tables are currently booked.")

root = tk.Tk()
root.configure(background="lightgrey")
root.geometry('800x600')

root.title("Naveen Restaurant")

table_frame = tk.Frame(root, bg='lightgrey')
table_frame.pack(side=tk.TOP, padx=10, pady=10)

table_buttons = []
for t in range(1, 21):
    table_button = tk.Button(table_frame, text=f"Table {t}", width=7, height=2, bg="green")
    if t <= 10:
        row = 0
        col = t - 1
    else:
        row = 1
        col = t - 11
    table_button.grid(row=row, column=col, padx=5, pady=5)
    table_buttons.append(table_button)

menu_frame = tk.Frame(root, bg='lightgrey')
menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

menu_label = tk.Label(menu_frame, text="Menu", bg='lightgreen', font=('Arial', 24))
menu_label.pack(padx=10, pady=10)

menu_items = [
    ("Aloo Paratha", 30),
    ("Samosa", 15),
    ("Pizza", 150),
    ("Gulab Jamun", 35),
    ("Chowmein", 70),
    ("Churma", 200)
]

entries = []
for item, price in menu_items:
    label = tk.Label(menu_frame, text=f"{item} - Rs. {price}", bg='lightgrey', font=('Arial', 14))
    label.pack(pady=2, padx=10, anchor="w")
    entry = tk.Entry(menu_frame, state=tk.DISABLED, bg='#f0f0f0', fg='black', font=('Arial', 12), relief=tk.FLAT)
    entry.pack(pady=2, padx=10, ipadx=20)
    entries.append(entry)

bill_frame = tk.Frame(root, bg='lightgrey')
bill_frame.pack(side=tk.LEFT, padx=10, pady=10)

generate_bill_btn = tk.Button(bill_frame, text="Generate Bill", font=('Arial', 18), command=calculate, bg='lightgreen')
generate_bill_btn.pack(pady=2)

specific_table_label = tk.Label(root, text="Go to Table number:", font=('Arial', 14), bg='lightgrey')
specific_table_label.pack(side=tk.BOTTOM, pady=(0, 5))

specific_table_entry = tk.Entry(root, font=('Arial', 14), width=5)
specific_table_entry.pack(side=tk.BOTTOM, pady=(0, 5))

specific_table_button = tk.Button(root, text="Leave", font=('Arial', 14), command=lambda: leave_table(int(specific_table_entry.get()) - 1), bg='red', fg='white')
specific_table_button.pack(side=tk.BOTTOM, pady=(0, 10))

book_table_button = tk.Button(root, text="Book Table", font=('Arial', 14), command=book_table, bg='orange')
book_table_button.pack(side=tk.BOTTOM, pady=(0, 10))

root.mainloop()
