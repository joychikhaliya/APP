import csv
import sys

# Check if filename is provided
if len(sys.argv) != 2:
    print("Usage: python sports_inventory.py <filename>")
    sys.exit()

filename = sys.argv[1]

try:
    # Read CSV file
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        equipment = list(reader)

    # Display all equipment
    print("\n===== SPORTS EQUIPMENT INVENTORY =====")

    for item in equipment:
        print("--------------------------------------")
        for key, value in item.items():
            print(f"{key}: {value}")

    # Search using Equipment ID
    search_id = input("\nEnter Equipment ID to search: ")

    found = False

    for item in equipment:
        if item["Equipment ID"] == search_id:
            print("\n===== EQUIPMENT FOUND =====")
            for key, value in item.items():
                print(f"{key}: {value}")
            found = True
            break

    if not found:
        print("Equipment with ID", search_id, "not found.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
