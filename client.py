import requests

BASE_URL = "http://localhost:5000"

while True:
    print("\n1. Health Check")
    print("2. View Cadets")
    print("3. Exit")
    
    choice = input("Select option: ")

    if choice == "1":
        r = requests.get(f"{BASE_URL}/health")
        print(r.json())

    elif choice == "2":
        r = requests.get(f"{BASE_URL}/cadets")
        print(r.json())

    elif choice == "3":
        break

