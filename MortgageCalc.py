def get_median_price(state):
    prices = {
        'Arkansas': 234167,
        'Texas': 342400,
        'Oklahoma': 250800
    }
    return prices.get(state, 0)

def choose_state():
    print("Choose a state 1, 2, or 3:")
    print("1. Arkansas\n2. Texas\n3. Oklahoma")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        state = 'Arkansas'
    elif choice == '2':
        state = 'Texas'
    elif choice == '3':
        state = 'Oklahoma'
    else:
        print("Invalid choice.")
        return None, 0
    
    median_price = get_median_price(state)
    print(f"The median house price in {state} is ${median_price:,} according to zillow.")
    return state, median_price

def get_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12 
    monthly_payment = principal * (monthly_rate + monthly_rate / ((1 + monthly_rate)**(12 * years) - 1))
    return monthly_payment


use_median = input("Do you want to use the median home price for Arkansas, Texas, or Oklahoma? (yes/no): ").lower()
if use_median == 'yes':
    state, principal = choose_state()
else:
    state = "Custom"
    principal = float(input("Enter the loan amount without commas: "))

if principal:
    years = float(input('Please enter number of years of loan: '))
    annual_rate = float(input('Please enter the interest rate without "%" sign: '))
    
    monthly_payment = get_monthly_payment(principal, annual_rate, years)
    print(f"Monthly Payment for {state}: ${monthly_payment:.2f}")
else:
    print("An error occurred with the state selection.")