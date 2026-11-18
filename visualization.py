
import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def read_expenses(filename="expenses.csv"):
    expenses = defaultdict(float)

    try:
        with open(filename, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                category = row["category"].strip()
                amount = float(row["amount"])

                if category and amount > 0:
                    expenses[category] += amount

    except FileNotFoundError:
        print("Error: expenses.csv not found.")
        return {}

    except (ValueError, KeyError) as error:
        print("Error reading expense data:", error)
        return {}

    return dict(expenses)


def create_pie_chart(expenses):
    if not expenses:
        print("No expense data available.")
        return

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
    plt.savefig("pie_chart.png")
    plt.show()

    print("Pie chart created successfully!")


def main():
    expenses = read_expenses()
    create_pie_chart(expenses)


if __name__ == "__main__":
    main()
