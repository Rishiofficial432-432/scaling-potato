import time
import sys
import platform
import re
from datetime import datetime, timedelta

# Function for loading animation
def loading_animation(message):
    print(message, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" Done!\n")

# Function to simulate server connection and encryption process
def server_connection_simulation():
    loading_animation("Connecting to secure server")
    print("Connection established!\n")
    time.sleep(1)
    loading_animation("Encrypting data")
    print("Data encryption successful!\n")
    time.sleep(1)

# Function to display system and version info
def display_system_info():
    print("\n--- SYSTEM INFORMATION ---")
    loading_animation("Initializing system information")
    os_info = platform.system()
    os_version = platform.version()
    python_version = platform.python_version()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date and Time: {time_now}")
    print(f"Operating System: {os_info} {os_version}")
    print(f"Python Version: {python_version}\n")
    time.sleep(1)

# Country codes for phone number validation
country_codes = {
    'India': '+91',
    'USA': '+1',
    'UK': '+44',
    # Add more country codes as needed
}

# Function to save transaction to file
def save_transaction(purchase_date, customer_name, customer_phone, item_name, unit_price, quantity, total_price):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("transaction_history.txt", "a") as file:
            file.write("\n" + "="*80 + "\n")
            file.write(f"Transaction Date & Time: {transaction_time}\n")
            file.write(f"Purchase Date: {purchase_date.strftime('%Y-%m-%d')}\n")
            file.write(f"Customer Name: {customer_name}\n")
            file.write(f"Phone Number: {customer_phone}\n")
            file.write(f"Item Purchased: {item_name}\n")
            file.write(f"Unit Price: ${unit_price:.2f}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Total Amount: ${total_price:.2f}\n")
            file.write("="*80 + "\n")
        loading_animation("Saving transaction to database")
        return True
    except Exception as e:
        print(f"Error saving transaction: {e}")
        return False

# Function to search transaction history
def search_transactions():
    print("\n--- SEARCH TRANSACTIONS ---")
    print("1. Search by Customer Phone")
    print("2. Search by Customer Name")
    print("3. Search by Date")
    choice = input("Select search option (1/2/3): ")

    search_term = ""
    if choice == "1":
        search_term = input("Enter customer phone number: ")
    elif choice == "2":
        search_term = input("Enter customer name: ")
    elif choice == "3":
        search_term = input("Enter date (YYYY-MM-DD): ")
    else:
        print("Invalid choice!")
        return

    try:
        with open("transaction_history.txt", "r") as file:
            content = file.read()
            transactions = content.split("="*80)
            found = False

            for transaction in transactions:
                if search_term.lower() in transaction.lower():
                    found = True
                    print("\nFound Transaction:")
                    print("="*80)
                    print(transaction)
                    print("="*80)

            if not found:
                print("No transactions found matching your search.")
    except FileNotFoundError:
        print("No transaction history found.")

# Function to validate and get purchase date
def get_purchase_date():
    while True:
        print("\n--- PURCHASE DATE ---")
        print("1. Today")
        print("2. Custom date")
        choice = input("Select option (1/2): ")

        if choice == "1":
            return datetime.now()

        elif choice == "2":
            try:
                date_str = input("Enter date (YYYY-MM-DD): ")
                purchase_date = datetime.strptime(date_str, "%Y-%m-%d")

                if purchase_date > datetime.now():
                    print("Error: Purchase date cannot be in the future!")
                    continue

                if purchase_date < datetime.now() - timedelta(days=30):
                    confirm = input("Warning: Date is more than 30 days old. Proceed? (y/n): ")
                    if confirm.lower() != 'y':
                        continue

                return purchase_date

            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD")
                continue

# Function to get customer details
def get_customer_details():
    print("--- CUSTOMER INFORMATION ---")
    customer_name = input("Enter customer's name: ")
    print("\nSelect country code:")
    for country, code in country_codes.items():
        print(f"{country}: {code}")
    country = input("Enter country name: ")
    if country not in country_codes:
        print("Invalid country. Please restart.")
        return None, None
    phone_code = country_codes[country]
    phone_number = input("Enter customer's phone number: ")
    if not validate_phone_number(phone_number, country):
        print("Invalid phone number format. Please restart.")
        return None, None
    return customer_name, phone_code + phone_number

# Function to validate phone numbers based on country
def validate_phone_number(phone_number, country):
    if country == 'India':
        return bool(re.match(r'^\d{10}$', phone_number))
    elif country == 'USA':
        return bool(re.match(r'^\d{10}$', phone_number))
    elif country == 'UK':
        return bool(re.match(r'^\d{10}$', phone_number))
    return False

# Function to get item details and calculate total price
def get_item_details():
    print("\n--- ITEM INFORMATION ---")
    item_name = input("Enter item name: ")
    unit_price = float(input("Enter per unit price: "))
    quantity = int(input("Enter quantity bought: "))
    total_price = unit_price * quantity
    print(f"Total price for {item_name}: {total_price:.2f}")
    return item_name, unit_price, quantity, total_price

# Main function to tie everything together
def main():
    while True:
        print("\n=== FUTURISTIC BILLING SYSTEM ===")
        print("1. New Transaction")
        print("2. Search Transaction History")
        print("3. Exit")

        choice = input("\nSelect option (1/2/3): ")

        if choice == "1":
            # Display loading and system information
            loading_animation("Loading futuristic billing software")
            server_connection_simulation()
            display_system_info()

            # Get purchase date
            purchase_date = get_purchase_date()

            # Gather customer information
            customer_name, customer_phone = get_customer_details()
            if customer_name and customer_phone:
                print(f"\nCustomer Name: {customer_name}, Phone: {customer_phone}")

                # Get item details and calculate total
                item_name, unit_price, quantity, total_price = get_item_details()

                # Save transaction
                if save_transaction(purchase_date, customer_name, customer_phone, 
                                 item_name, unit_price, quantity, total_price):

                    # Display futuristic final output
                    print("\n" + "="*40)
                    print("--- TRANSACTION SUMMARY ---")
                    print("="*40)
                    print(f"Date of Purchase: {purchase_date.strftime('%Y-%m-%d')}")
                    print(f"Customer: {customer_name}")
                    print(f"Phone: {customer_phone}")
                    print("-"*40)
                    print(f"Item: {item_name}")
                    print(f"Unit Price: ${unit_price:.2f}")
                    print(f"Quantity: {quantity}")
                    print(f"Total Purchase Amount: ${total_price:.2f}")
                    print("="*40)
                    print("Thank you for shopping with us. Secure Transaction Complete.")
                    loading_animation("Logging transaction securely")

        elif choice == "2":
            search_transactions()

        elif choice == "3":
            print("\nThank you for using IRON LEGION Billing System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
