
import csv

# File name
FILE_NAME = "expenses.csv"

# Empty list to store expenses
expenses = []

# Load previous expenses
try:
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

    print("Previous expenses loaded successfully!")

except FileNotFoundError:
    print("No previous expense file found. Starting a new record.")


# Function to save expenses
def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "item", "category", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved successfully!")


# Main menu
while True:

    print("\n===== INSTITUTE EXPENSE TRACKER =====")
    print("1. Add New Expense")
    print("2. Show All Expenses")
    print("3. Calculate Total Expenses by Category")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add new expense
    if choice == "1":

        date = input("Enter expense date (DD-MM-YYYY): ")
        item = input("Enter item name: ")
        category = input("Enter expense category: ")

        # Validate amount
        while True:
            try:
                amount = float(input("Enter expense amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                break

            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        # Store expense in dictionary
        expense = {
            "date": date,
            "item": item,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        # Save expenses in CSV file
        save_expenses()

    # Show all expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses available.")

        else:
            print("\n===== ALL EXPENSES =====")

            for expense in expenses:
                print(
                    "Date:", expense["date"],
                    "| Item:", expense["item"],
                    "| Category:", expense["category"],
                    "| Amount: Rs.", expense["amount"]
                )

    # Calculate category-wise expenses
    elif choice == "3":

        if len(expenses) == 0:
            print("No expenses available.")

        else:
            # Get unique categories using set
            categories = set(
                expense["category"] for expense in expenses
            )

            print("\n===== EXPENSES BY CATEGORY =====")

            for category in categories:

                total = sum(
                    expense["amount"]
                    for expense in expenses
                    if expense["category"] == category
                )

                print(category, ": Rs.", total)

            print("\nUnique Categories:", categories)

    # Exit program
    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
