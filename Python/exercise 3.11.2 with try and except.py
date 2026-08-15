print(f"=== Your Salary ===")

try:
    hrs_of_work = int(input("Enter Hours: "))
except:
    print("Please enter a numeric value: ")

try:
    rate = int(input("Enter Rate: "))
except:
    print(f"Please enter a numaric value: ")
try:
    if hrs_of_work  > 40:
        regular_pay = 40 * rate
        overtime_pay = ((hrs_of_work - 40) * rate) * 1.5
        pay = regular_pay + overtime_pay
    else:
        pay = hrs_of_work * rate
    print(f'Your salary is {pay} INR')
except:
    print(f'Re-run the program and enter right values next time')
    