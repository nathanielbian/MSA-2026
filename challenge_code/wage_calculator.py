def collect_data(property, max):
    while True:
        try:
            value = float(input(f"Enter {property}: "))

            if value < 0 or value > max:
                print(f"ERROR: Please enter a valid {property}!\n")
                continue

            return value
        except:
            print(f"ERROR: Please enter a valid number!\n")

def main():
    hours_worked_daily = collect_data("hours worked daily", 24)
    hourly_wage = collect_data("hourly wage", float("inf"))

    tax_rate = .12
    days_worked = 350

    wages_before_taxes = hours_worked_daily * hourly_wage * days_worked
    tax_amount = wages_before_taxes * tax_rate
    annual_wages_after_taxes = wages_before_taxes - tax_amount

    print("\nPay Advice\n------------------")
    print(f"Hours worked: {hours_worked_daily:,.2f} hours")
    print(f"Hourly wage: ${hourly_wage:,.2f}")
    print(f"Wages before taxes: ${wages_before_taxes:,.2f}")
    print(f"Tax amount: ${tax_amount:,.2f}")
    print(f"Annual Wages After Taxes: ${annual_wages_after_taxes:,.2f}")
    
main()
