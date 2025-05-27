# Create a class and List to store Expenses
class ExpenseTracker:
	def __init__(self):
		self.expenses = []

# A fuction to add expense		
	def add_expense(self):
		expense_name = input("Enter an expense: ")
		
# Returns to the menu if the user consistently throws a ValueError

		for attempt in range(2):
			try:
				expense_amount = float(input("Enter the amount: "))
			except ValueError:
				print("\nPlease enter a numerical value for amount!")
			else:
				self.expenses.append({'expense': expense_name, 'amount': expense_amount})
				print(f"Successfully added {expense_name} ${expense_amount}")
				break
		else:
			print("\nFailed to add expense due to Invalid Amount")
			return
					
# Displays the stored expenses		
	def display_expenses(self):
		print('\nExpense Summary:')
		for x in self.expenses:
			print(f"-{x['expense']}: ${x['amount']}")

# Calculates the total expenses		
	def total_expense(self):
		total = 0
		for i in self.expenses:
			total += i['amount']
			ans = total
		print(f"\nTotal expense = ${ans}")

# Deletes an expense 
	
	def delete_expense(self):
		found = False
		name = input("\nInput the name of the expense you want to delete: ")
		for expense in self.expenses:
			
# Handles case sensitivity

			if expense['expense'].lower() == name.lower():
				self.expenses.remove(expense)
				print(f"\nSuccessfully deleted {name} expense")
				found = True
				break
		if not found:
			print(f"There's no {name} expense")
		
				
# create object and simple menu to implement the fuctions
personalTracker = ExpenseTracker()
print("A Simple Expense Tracker")
ans = 'yes'
while ans != '5':
	ans = input('''
Select any of the options below to continue.
1. Add an Expense
2. View Expense Summary
3. View Total Expense
4. Delete an expense
5. Exit

Reply: ''')
	if ans.strip() == '1':
		personalTracker.add_expense()
	elif ans.strip() == '2':
		personalTracker.display_expenses()
	elif ans.strip() == '3':
		personalTracker.total_expense()
	elif ans.strip() == '4':
		personalTracker.display_expenses()
		personalTracker.delete_expense()
	elif ans.strip() == '5':
		break
	else:
		print("Invalid Option!")
		
		
		
		
