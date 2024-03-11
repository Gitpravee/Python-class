income = input("what is ur income? ")
income = int(income)
taxable_income = income - 5_00_000
if taxable_income > 0:
    tax = taxable_income * 10 / 100
    print("your tax is:", tax)
else:
    print("no tax")
