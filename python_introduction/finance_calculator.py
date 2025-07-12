monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


Monthly_savings = monthly_income - monthly_expenses

projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${Monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
