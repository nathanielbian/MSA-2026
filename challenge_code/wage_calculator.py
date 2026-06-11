# General function to collect a float
def collect_data(property, max):
    # Loop to collect data
    while True:
        try:
            # Gather data
            value = float(input(f"Enter {property}: "))

            # Return the value if it is valid
            if 0 < value <= max:
                return value

            # Print error statement
            print(f"ERROR: Please enter a valid {property}!\n")
        except:
            # Print error statement
            print("ERROR: Please enter a valid number!\n")

def main():
    # Call function to gather values
    hours_worked_daily = collect_data("hours worked daily", 24)
    hourly_wage = collect_data("hourly wage", float("inf"))

    # Initialize other variables
    tax_rate = .12
    days_worked = 350

    # Calculate values
    wages_before_taxes = hours_worked_daily * hourly_wage * days_worked
    tax_amount = wages_before_taxes * tax_rate
    annual_wages_after_taxes = wages_before_taxes - tax_amount

    # Output values
    print("\nPay Advice\n------------------")
    print(f"Hours worked: {hours_worked_daily:,.2f} hours")
    print(f"Hourly wage: ${hourly_wage:,.2f}")
    print(f"Wages before taxes: ${wages_before_taxes:,.2f}")
    print(f"Tax amount: ${tax_amount:,.2f}")
    print(f"Annual Wages After Taxes: ${annual_wages_after_taxes:,.2f}")

# Call the main function
main()
