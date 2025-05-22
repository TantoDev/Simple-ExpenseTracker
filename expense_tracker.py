# Class to track expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []  # List to store expenses

    # Add a new expense
    def add_expense(self):
        expense_name = input("Enter an expense: ")
        expense_amount = float(input("Enter the amount: "))
        self.expenses.append({'expense': expense_name, 'amount': expense_amount})
        print(f"Successfully added {expense_name} ${expense_amount}")

    # Display all stored expenses
    def display_expenses(self):
        print('\nExpense Summary:')
        for x in self.expenses:
            print(f"-{x['expense']}: ${x['amount']}")

    # Calculate and display the total expenses
    def total_expense(self):
        total = 0
        for i in self.expenses:
            total += i['amount']
        print(f"\nTotal expense = ${total}")


# Create an object and menu to use the functions
personalTracker = ExpenseTracker()
print("A Simple Expense Tracker")
ans = 'yes'
while ans != '4':
    ans = input('''
Select any of the options below to continue.
1. Add an Expense
2. View Expense Summary
3. View Total Expense
4. Exit

Reply: ''')
    if ans == '1':
        personalTracker.add_expense()
    elif ans == '2':
        personalTracker.display_expenses()
    elif ans == '3':
        personalTracker.total_expense()
    elif ans == '4':
        break
    else:
        print("Invalid Option!")
