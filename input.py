
import csv
import os
from datetime import datetime

CSV_FILE = "expenses.csv"


def initialize_csv():
    """Initialize the expense CSV file."""

    # Check whether the file does not exist or is empty
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Write column names
            writer.writerow([
                "date",
                "amount",
                "category",
                "notes"
            ])

        print("Expense file initialized successfully!")


def add_expense():
    print("\n===== Add Expense =====")

    # 1. Input date
    while True:
        date = input("Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter YYYY-MM-DD.")

    # 2. Input amount
    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # 3. Input category
    while True:
        category = input("Category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # 4. Input notes (optional)
    notes = input("Notes (optional): ").strip()

    # 5. Save expense to CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            date,
            amount,
            category,
            notes
        ])

    print("\nExpense added successfully!")


def main():
    initialize_csv()

    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. Exit")

        choice = input("Please select: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()