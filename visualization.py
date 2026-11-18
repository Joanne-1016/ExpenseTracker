
import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"


def show_pie_chart():
    """Display expense distribution by category."""

    if not os.path.exists(CSV_FILE):
        print("Expense file not found!")
        return

    expenses = {}

    # Read expense data
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["category"].strip()
            amount = float(row["amount"])

            expenses[category] = expenses.get(category, 0) + amount

    # Check whether expense data exists
    if not expenses:
        print("No expense data available!")
        return

    # Draw pie chart
    categories = list(expenses.keys())
    amounts = list(expenses.values())

    plt.figure(figsize=(8, 6))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    show_pie_chart()
