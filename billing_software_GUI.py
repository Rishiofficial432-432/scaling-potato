import tkinter as tk
from tkinter import ttk

# --- Billing Logic (Example) ---

def get_customer_details():
    """Get customer details from GUI elements."""
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    return {"name": name, "phone": phone, "address": address}

def get_item_details():
    """Get item details from GUI elements."""
    item_name = item_name_entry.get()
    price_per_unit = float(price_entry.get())
    quantity = int(quantity_entry.get())
    return {"name": item_name, "price_per_unit": price_per_unit, "quantity": quantity}

def add_item():
    """Add an item to the bill."""
    item = get_item_details()
    items.append(item)
    # Update GUI to display added item (e.g., add item to a listbox)

def generate_bill():
    """Generate and display the bill."""
    customer = get_customer_details()
    total_cost = 0
    print("\n--- BILL ---")
    print(f"Customer Name: {customer['name']}")
    print(f"Phone: {customer['phone']}")
    print(f"Address: {customer['address']}")
    print("\nItemized Bill:")
    for item in items:
        item_total = item["quantity"] * item["price_per_unit"]
        total_cost += item_total
        print(f"{item['name']} - {item['quantity']} - Price: {item['price_per_unit']:.2f}, Total: {item_total:.2f}")
    print(f"\nTotal Cost: {total_cost:.2f}")
    print("\n--- Transaction Complete ---\n")

# --- GUI Setup ---

items = []  # List to store added items

root = tk.Tk()
root.title("Billing System")

# Customer Details
customer_frame = tk.LabelFrame(root, text="Customer Details")
customer_frame.pack(padx=10, pady=10)

name_label = tk.Label(customer_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(customer_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(customer_frame, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(customer_frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

address_label = tk.Label(customer_frame, text="Address:")
address_label.grid(row=2, column=0, padx=5, pady=5)
address_entry = tk.Entry(customer_frame)
address_entry.grid(row=2, column=1, padx=5, pady=5)

# Item Details
items_frame = tk.LabelFrame(root, text="Item Details")
items_frame.pack(padx=10, pady=10)

item_name_label = tk.Label(items_frame, text="Item Name:")
item_name_label.grid(row=0, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(items_frame)
item_name_entry.grid(row=0, column=1, padx=5, pady=5)

price_label = tk.Label(items_frame, text="Price:")
price_label.grid(row=1, column=0, padx=5, pady=5)
price_entry = tk.Entry(items_frame)
price_entry.grid(row=1, column=1, padx=5, pady=5)

quantity_label = tk.Label(items_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(items_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_item_button = tk.Button(root, text="Add Item", command=lambda: add_item())
add_item_button.pack(pady=10)

generate_bill_button = tk.Button(root, text="Generate Bill", command=lambda: generate_bill())
generate_bill_button.pack(pady=10)

root.mainloop()