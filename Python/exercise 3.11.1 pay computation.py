print(f' == Lets Calculate Your Payble Salary ==\n')
hrs = int(input("Enter Hours (e.g. 50): "))
rate = int(input("Enter Rate per hrs (e.g. 12): "))
overtime_rate_increase = float(input(f"Change in rate of overtime per hour. How much times is the increase in rate of regular rate is given under overtime rate per hour? (e.g. 1.6, etc."))
overtime_hrs = int(input(f"Maximum regular work hours after which overtime hours starts which should be less than (<) the point of overtime work hour: "))

print(f'\n=== your pay ===\n')

if hrs >= overtime_hrs:
    ot_pay = ((hrs - overtime_hrs) * rate) * overtime_rate_increase
    r_pay = overtime_hrs * rate
    pay = ot_pay + r_pay
    print(f" Your salary is: {pay} INR.")
else:
    pay = hrs * rate
    print = (f"Your slalary is: {pay} INR.")