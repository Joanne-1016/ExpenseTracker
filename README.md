# ExpenseTracker

## 1. Project Overview

ExpenseTracker is a Python-based expense tracking system that allows users to record daily expenses and visualize spending by category using a pie chart.

## 2. Features

- **Expense Input:** Add expense records including date, amount, category, and notes.
- **CSV Storage:** Store expense records in `expenses.csv`.
- **Data Validation:** Validate user input, including date format and expense amount.
- **Data Visualization:** Display expense distribution by category using a pie chart.

## 3. Project Structure

```text
ExpenseTracker/
│
├── input.py
├── visualization.py
├── expenses.csv
├── README.md
└── .gitignore
```

## 4. Requirements

- Python 3
- matplotlib

Install the required library:

```bash
pip install matplotlib
```

## 5. How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the input module:

```bash
python input.py
```

4. Follow the menu to add expense records.

5. Run the visualization module:

```bash
python visualization.py
```

## 6. Data Format

Expense records are stored in `expenses.csv`.

| Field | Description |
|---|---|
| date | Expense date |
| amount | Expense amount |
| category | Expense category |
| notes | Expense description |

Example:

```csv
date,amount,category,notes
2026-11-13,80,Transport,Bus
2026-11-15,250,Shopping,Clothes
2026-11-15,200,Food,Brunch
```

## 7. Team Contributions

| Member | Student | Responsibility |
|---|---|---|
| Member A | 1132937 林郁潔 | Expense Input Module |
| Member B | 1132935 李芳儀 | Data Visualization Module |

## 8. Repository

GitHub: https://github.com/Joanne-1016/ExpenseTracker