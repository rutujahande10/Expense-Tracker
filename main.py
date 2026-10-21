import json
from pathlib import Path


FILE_PATH = Path(__file__).with_name("expenses.json")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if FILE_PATH.exists():
            try:
                with open(FILE_PATH, "r", encoding="utf-8") as file:
                    self.expenses = json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Could not read expenses.json.")
                self.expenses = []

    def save_expenses(self):
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        description = input("Enter description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return

        try:
            amount = float(input("Enter amount:- "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return

        next_id = max(
            (expense["id"] for expense in self.expenses),
            default=0
        ) + 1

        expense = {
            "id": next_id,
            "description": description,
            "amount": amount,
            "category": category
        }

        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense added successfully! ID: {next_id}")

    def view_expenses(self, category=None):
        if category:
            results = [
                expense for expense in self.expenses
                if expense["category"].casefold() == category.casefold()
            ]
        else:
            results = self.expenses

        if not results:
            print("No expenses found.")
            return

        for expense in results:
            print(
                f'ID: {expense["id"]} | '
                f'Description: {expense["description"]} | '
                f'Amount: {expense["amount"]:.2f} | '
                f'Category: {expense["category"]}'
            )

    def delete_expense(self):
        try:
            expense_id = int(input("Enter expense ID to delete: "))
        except ValueError:
            print("Please enter a valid ID.")
            return

        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                print("Expense deleted successfully.")
                return

        print("Expense ID not found.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter category: ").strip()
            if category:
                tracker.view_expenses(category)
            else:
                print("Category cannot be empty.")

        elif choice == "4":
            tracker.delete_expense()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()