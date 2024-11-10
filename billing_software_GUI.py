import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import re

# Country codes for validation
country_codes = {
    'India': '+91',
    'USA': '+1',
    'UK': '+44',
}

# Currency options
currency_options = ['INR', 'USD', 'GBP']

# Payment modes
payment_modes = ['Cash', 'Credit Card', 'Debit Card', 'UPI']

# Function to validate phone number
def validate_phone_number(phone_number, country):
    if country == 'India':
        return bool(re.match(r'^\d{10}$', phone_number))
    elif country == 'USA':
        return bool(re.match(r'^\d{10}$', phone_number))
    elif country == 'UK':
        return bool(re.match(r'^\d{10}$', phone_number))
    return False

# Function to save transaction to file
def save_transaction(shop_name, purchase_date, customer_name, customer_phone, item_name, unit_price, quantity, total_price, currency, payment_mode, upi_number=None):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("transaction_history.txt", "a") as file:
            file.write("\n" + "="*80 + "\n")
            file.write(f"Transaction Date & Time: {transaction_time}\n")
            file.write(f"Shop Name: {shop_name}\n")
            file.write(f"Purchase Date: {purchase_date.strftime('%Y-%m-%d')}\n")
            file.write(f"Customer Name: {customer_name}\n")
            file.write(f"Phone Number: {customer_phone}\n")
            file.write(f"Item Purchased: {item_name}\n")
            file.write(f"Unit Price: {unit_price:.2f} {currency}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Total Amount: {total_price:.2f} {currency}\n")
            file.write(f"Payment Mode: {payment_mode}\n")
            if payment_mode == 'UPI' and upi_number:
                file.write(f"UPI Number: {upi_number}\n")
            file.write("="*80 + "\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error saving transaction: {e}")
        return False

# Function to handle form submission
def submit_form():
    shop_name = shop_name_entry.get()
    customer_name = name_entry.get()
    country = country_var.get()
    phone_number = phone_entry.get()
    date_str = date_entry.get()
    item_name = item_entry.get()
    unit_price = price_entry.get()
    quantity = quantity_entry.get()
    currency = currency_var.get()
    payment_mode = payment_mode_var.get()
    upi_number = upi_number_entry.get() if payment_mode == 'UPI' else None

    if not shop_name.strip():
        messagebox.showerror("Error", "Shop name cannot be empty.")
        return
    if not customer_name.strip():
        messagebox.showerror("Error", "Customer name cannot be empty.")
        return
    if country not in country_codes:
        messagebox.showerror("Error", "Invalid country selected.")
        return
    if not validate_phone_number(phone_number, country):
        messagebox.showerror("Error", "Invalid phone number format.")
        return
    try:
        purchase_date = datetime.strptime(date_str, "%Y-%m-%d")
        if purchase_date > datetime.now():
            messagebox.showerror("Error", "Purchase date cannot be in the future.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return
    if not item_name.strip():
        messagebox.showerror("Error", "Item name cannot be empty.")
        return
    try:
        unit_price = float(unit_price)
        quantity = int(quantity)
        total_price = unit_price * quantity
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for price and quantity.")
        return

    customer_phone = country_codes[country] + phone_number

    if payment_mode == 'UPI' and not upi_number.strip():
        messagebox.showerror("Error", "UPI number is required for UPI payment.")
        return

    if save_transaction(shop_name, purchase_date, customer_name, customer_phone, item_name, unit_price, quantity, total_price, currency, payment_mode, upi_number):
        messagebox.showinfo("Transaction Saved", f"Transaction saved successfully!\n\nTotal Price: {total_price:.2f} {currency}\nPayment Mode: {payment_mode}")

# Function to handle printing the bill
def print_bill():
    shop_name = shop_name_entry.get()
    customer_name = name_entry.get()
    country = country_var.get()
    phone_number = phone_entry.get()
    date_str = date_entry.get()
    item_name = item_entry.get()
    unit_price = price_entry.get()
    quantity = quantity_entry.get()
    currency = currency_var.get()
    payment_mode = payment_mode_var.get()
    upi_number = upi_number_entry.get() if payment_mode == 'UPI' else None

    try:
        unit_price = float(unit_price)
        quantity = int(quantity)
        total_price = unit_price * quantity
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for price and quantity.")
        return

    bill_window = tk.Toplevel(root)
    bill_window.title("Generated Bill")

    bill_text = f"Shop Name: {shop_name}\n"
    bill_text += f"Customer: {customer_name}\n"
    bill_text += f"Phone: {phone_number}\n"
    bill_text += f"Purchase Date: {date_str}\n"
    bill_text += f"Item: {item_name}\n"
    bill_text += f"Unit Price: {unit_price:.2f} {currency}\n"
    bill_text += f"Quantity: {quantity}\n"
    bill_text += f"Total: {total_price:.2f} {currency}\n"
    bill_text += f"Payment Mode: {payment_mode}\n"
    if payment_mode == 'UPI' and upi_number:
        bill_text += f"UPI Number: {upi_number}\n"

    bill_label = tk.Label(bill_window, text=bill_text, font=("Arial", 12), justify="left", padx=20, pady=20)
    bill_label.pack()

    print_button = tk.Button(bill_window, text="Print", font=("Arial", 12), bg="#4A90E2", fg="white", command=bill_window.destroy)
    print_button.pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("SmitLogic Billing Hub")
root.geometry("500x700")
root.config(bg="#f5f5f5")

# Title Label
title_label = tk.Label(root, text="SmitLogic Billing Hub", font=("Arial", 20, "bold"), fg="#4A90E2", bg="#f5f5f5")
title_label.pack(pady=10)

# Frame for Shop Name
shop_frame = tk.LabelFrame(root, text="Shop Information", font=("Arial", 12), fg="#333", padx=10, pady=10, bg="#e8f0fe")
shop_frame.pack(fill="both", padx=10, pady=5)

# Shop Name
tk.Label(shop_frame, text="Shop Name:", font=("Arial", 10), bg="#e8f0fe").grid(row=0, column=0, sticky="w", pady=5)
shop_name_entry = tk.Entry(shop_frame, width=30, font=("Arial", 10))
shop_name_entry.grid(row=0, column=1, pady=5)

# Frame for Customer Information
customer_frame = tk.LabelFrame(root, text="Customer Information", font=("Arial", 12), fg="#333", padx=10, pady=10, bg="#e8f0fe")
customer_frame.pack(fill="both", padx=10, pady=5)

# Customer Name
tk.Label(customer_frame, text="Name:", font=("Arial", 10), bg="#e8f0fe").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(customer_frame, width=30, font=("Arial", 10))
name_entry.grid(row=0, column=1, pady=5)

# Country Dropdown
tk.Label(customer_frame, text="Country:", font=("Arial", 10), bg="#e8f0fe").grid(row=1, column=0, sticky="w", pady=5)
country_var = tk.StringVar(value="India")
country_menu = ttk.Combobox(customer_frame, textvariable=country_var, values=["India", "USA", "UK"], state="readonly")
country_menu.grid(row=1, column=1, pady=5)

# Phone Number
tk.Label(customer_frame, text="Phone Number:", font=("Arial", 10), bg="#e8f0fe").grid(row=2, column=0, sticky="w", pady=5)
phone_entry = tk.Entry(customer_frame, width=30, font=("Arial", 10))
phone_entry.grid(row=2, column=1, pady=5)

# Purchase Date
tk.Label(customer_frame, text="Purchase Date (YYYY-MM-DD):", font=("Arial", 10), bg="#e8f0fe").grid(row=3, column=0, sticky="w", pady=5)
date_entry = tk.Entry(customer_frame, width=30, font=("Arial", 10))
date_entry.grid(row=3, column=1, pady=5)

# Frame for Item Information
item_frame = tk.LabelFrame(root, text="Item Information", font=("Arial", 12), fg="#333", padx=10, pady=10, bg="#e8f0fe")
item_frame.pack(fill="both", padx=10, pady=5)

# Item Name
tk.Label(item_frame, text="Item Name:", font=("Arial", 10), bg="#e8f0fe").grid(row=0, column=0, sticky="w", pady=5)
item_entry = tk.Entry(item_frame, width=30, font=("Arial", 10))
item_entry.grid(row=0, column=1, pady=5)

# Unit Price
tk.Label(item_frame, text="Unit Price:", font=("Arial", 10), bg="#e8f0fe").grid(row=1, column=0, sticky="w", pady=5)
price_entry = tk.Entry(item_frame, width=30, font=("Arial", 10))
price_entry.grid(row=1, column=1, pady=5)

# Quantity
tk.Label(item_frame, text="Quantity:", font=("Arial", 10), bg="#e8f0fe").grid(row=2, column=0, sticky="w", pady=5)
quantity_entry = tk.Entry(item_frame, width=30, font=("Arial", 10))
quantity_entry.grid(row=2, column=1, pady=5)

# Currency Dropdown
tk.Label(item_frame, text="Currency:", font=("Arial", 10), bg="#e8f0fe").grid(row=3, column=0, sticky="w", pady=5)
currency_var = tk.StringVar(value="INR")
currency_menu = ttk.Combobox(item_frame, textvariable=currency_var, values=currency_options, state="readonly")
currency_menu.grid(row=3, column=1, pady=5)

# Payment Mode Dropdown
tk.Label(item_frame, text="Payment Mode:", font=("Arial", 10), bg="#e8f0fe").grid(row=4, column=0, sticky="w", pady=5)
payment_mode_var = tk.StringVar(value="Cash")
payment_mode_menu = ttk.Combobox(item_frame, textvariable=payment_mode_var, values=payment_modes, state="readonly")
payment_mode_menu.grid(row=4, column=1, pady=5)

# UPI Number Entry (Initially hidden)
upi_number_label = tk.Label(item_frame, text="Enter UPI Number:", font=("Arial", 10), bg="#e8f0fe")
upi_number_label.grid(row=5, column=0, sticky="w", pady=5)
upi_number_entry = tk.Entry(item_frame, width=30, font=("Arial", 10))
upi_number_entry.grid(row=5, column=1, pady=5)
upi_number_label.grid_forget()
upi_number_entry.grid_forget()

# Show UPI entry if UPI is selected
def show_upi_entry(event=None):
    if payment_mode_var.get() == "UPI":
        upi_number_label.grid(row=5, column=0, sticky="w", pady=5)
        upi_number_entry.grid(row=5, column=1, pady=5)
    else:
        upi_number_label.grid_forget()
        upi_number_entry.grid_forget()

# Bind the show_upi_entry function to changes in the payment mode dropdown
payment_mode_menu.bind("<<ComboboxSelected>>", show_upi_entry)


# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), bg="#4A90E2", fg="white", command=submit_form)
submit_button.pack(pady=10)

# Print Bill Button
print_button = tk.Button(root, text="Print Bill", font=("Arial", 12), bg="#4A90E2", fg="white", command=print_bill)
print_button.pack(pady=10)

root.mainloop()
