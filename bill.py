def calculate_due_amount(bill_amount, amount_paid):
  due_amount = bill_amount - amount_paid
  return due_amount


total_bill = float(input("Enter the total bill amount: "))
paid = float(input("Enter the amount paid by the customer: "))

remaining = calculate_due_amount(total_bill, paid)

print(f"The customer's due amount is: ${remaining:.2f}")