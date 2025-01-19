import tkinter as tk
from tkinter import messagebox

booked_tables = [False] * 20  

discount = 0
bill = None
billnet = None
discount_label = None

def enable_order():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.config(state=tk.NORMAL)

def disable_order():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.config(state=tk.DISABLED)

def clear_entries():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
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
        'Aloo Paratha': [entry1, 30],
        'Samosa': [entry2, 15],
        'Pizza': [entry3, 150],
        'Gulab Jamun': [entry4, 35],
        'Chowmein': [entry5, 70],
        'Churma': [entry6, 200]
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
    
    bill = tk.Label(root, text="Total Bill: Rs. " + str(total), font=('arial', 14))
    bill.pack(pady=5)
    
    
    discount_label = tk.Label(root, text="Discount: " + str(discount) + "%", font=('arial', 14))
    discount_label.pack(pady=5)
   

    net = total - (total * discount) / 100
    
    
    billnet = tk.Label(root, text="Net Amount: Rs. " + str(net), font=('arial', 16), fg="blue")
    billnet.pack(pady=5)
    
def leave_table():
    global booked_tables, table_buttons
    last_booked_table = None
    for idx, booked in enumerate(reversed(booked_tables)):
        if booked:
            last_booked_table = 19 - idx
            break

    if last_booked_table is None:
        messagebox.showinfo(title="No Tables Booked", message="No tables are currently booked.")
    else:
        booked_tables[last_booked_table] = False
        table_buttons[last_booked_table].config(bg="green")
        enable_order()
        clear_entries()
        messagebox.showinfo(title="Table Freed", message=f"Table {last_booked_table + 1} has been freed.")

def book_table(table_idx):
    global booked_tables
    if booked_tables[table_idx]:
        messagebox.showinfo(title="Table Already Booked", message="The table is already booked!")
    else:
        table_buttons[table_idx].config(bg="red")
        booked_tables[table_idx] = True
        enable_order()  
        clear_entries()

root = tk.Tk()
root.configure(background="lightgrey")
root.geometry('600x1500')

root.title("Naveen Restaurant")


tables_frame = tk.Frame(root)
tables_frame.pack(pady=5)

table_buttons = []
for t in range(1, 21):
    table_button = tk.Button(tables_frame, text=f"Table {t}", width=7, height=2, bg="green")
    table_button.grid(row=(t-1)//5, column=(t-1)%5, padx=10, pady=4)
    table_buttons.append(table_button)
    if t != 20: 
        table_button.config(command=lambda idx=t-1: book_table(idx))
        

table_buttons[-1].config(command=lambda: book_table(19))


label1 = tk.Label(root, text="Menu", bg="lightgreen", font=("arial", 24))
label1.pack(padx=10, pady=2)


menu_frame = tk.Frame(root, bg="lightgreen")
menu_frame.pack(pady=2)

menu_items = [
    ("Aloo Paratha", 30),
    ("Samosa", 15),
    ("Pizza", 150),
    ("Gulab Jamun", 35),
    ("Chowmein", 70),
    ("Churma", 200)
]

for item, price in menu_items:
    label = tk.Label(menu_frame, bg="lightgreen", text=f"{item} - Rs. {price}", font=("arial", 16))
    label.pack()

asking = tk.Label(root, text="Select your order", font=("arial", 18))
asking.pack(pady=2)


entry1 = tk.Entry(root, state=tk.DISABLED)
entry1.pack(pady=2)
entry2 = tk.Entry(root, state=tk.DISABLED)
entry2.pack(pady=2)
entry3 = tk.Entry(root, state=tk.DISABLED)
entry3.pack(pady=2)
entry4 = tk.Entry(root, state=tk.DISABLED)
entry4.pack(pady=2)
entry5 = tk.Entry(root, state=tk.DISABLED)
entry5.pack(pady=2)
entry6 = tk.Entry(root, state=tk.DISABLED)
entry6.pack(pady=2)


generate_bill_btn = tk.Button(root, text="Generate Bill", font=("arial", 18), command=calculate)
generate_bill_btn.pack(pady=2)
leave_table_btn = tk.Button(root, text="Leave the Table", font=("arial", 16), command=leave_table)
leave_table_btn.pack(pady=2)

root.mainloop()