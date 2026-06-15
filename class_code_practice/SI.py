principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"Simple interest for the given principal amount {principal}, rate of interest {rate} and time {time} is : {simple_interest:.2f}")