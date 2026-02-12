import requests
import tkinter as tk
from tkinter import filedialog

BASE_URL = "http://localhost:5000"


def health_check():
    r = requests.get(f"{BASE_URL}/health")
    print(r.json())


def view_cadets():
    r = requests.get(f"{BASE_URL}/cadets/")
    print(r.json())


def add_cadet():
    first = input("First name: ")
    last = input("Last name: ")
    company = input("Company: ")
    year = int(input("Class year: "))

    payload = {
        "first_name": first,
        "last_name": last,
        "company": company,
        "class_year": year
    }

    r = requests.post(f"{BASE_URL}/cadets/", json=payload)
    print(r.json())


def view_items():
    r = requests.get(f"{BASE_URL}/items/")
    print(r.json())


def add_item():
    name = input("Item name: ")
    price = float(input("Price: "))
    qty = int(input("Stock quantity: "))

    payload = {
        "name": name,
        "price": price,
        "in_stock_qty": qty
    }

    r = requests.post(f"{BASE_URL}/items/", json=payload)
    print(r.json())


def upload_csv():
    root = tk.Tk()
    root.withdraw()  # hide main window
    filepath = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not filepath:
        print("No file selected.")
        return

    with open(filepath, "rb") as f:
        files = {"file": f}
        r = requests.post(f"{BASE_URL}/items/upload", files=files)
        print(r.json())


def view_orders():
    r = requests.get(f"{BASE_URL}/orders/")
    print(r.json())


def create_order():
    cadet_id = int(input("Cadet ID: "))
    items = []

    while True:
        item_id = input("Item ID (or blank to finish): ")
        if not item_id:
            break
        quantity = int(input("Quantity: "))
        items.append({
            "item_id": int(item_id),
            "quantity": quantity
        })

    payload = {
        "cadet_id": cadet_id,
        "items": items
    }

    r = requests.post(f"{BASE_URL}/orders/", json=payload)
    print(r.json())


def reset_database():
    confirm = input("Are you sure you want to reset the database? (yes/no): ")
    if confirm.lower() != "yes":
        print("Cancelled.")
        return

    r = requests.post(f"{BASE_URL}/admin/reset")
    print(r.json())


while True:
    print("\n===== Company Store Client =====")
    print("1. Health Check")
    print("2. View Cadets")
    print("3. Add Cadet")
    print("4. View Items")
    print("5. Add Item")
    print("6. Upload Items via CSV")
    print("7. View Orders")
    print("8. Create Order")
    print("9. Reset Database")
    print("10. Exit")

    choice = input("Select option: ")

    if choice == "1":
        health_check()
    elif choice == "2":
        view_cadets()
    elif choice == "3":
        add_cadet()
    elif choice == "4":
        view_items()
    elif choice == "5":
        add_item()
    elif choice == "6":
        upload_csv()
    elif choice == "7":
        view_orders()
    elif choice == "8":
        create_order()
    elif choice == "9":
        reset_database()
    elif choice == "10" or choice == "Exit":
        break
    else:
        print("Invalid option.")
