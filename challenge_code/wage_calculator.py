def collect_data(property, range_min, range_max, hard_max):
    while True:
        try:
            value = float(input(f"Enter {property}: "))

            if value < 0 or value > hard_max:
                print(f"ERROR: Please enter a valid {property}!\n")
                continue

            if value < range_min or value > range_max:
                if input("Are you really sure this value is correct? (y to continue): ") != "y" :
                    continue

            return value
        except:
            print(f"ERROR: Please enter a valid number!\n")

def main():
    hours_worked_daily = collect_data("hours worked daily", 1, 12, 24)
    hourly_wage = collect_data("hourly wage", 7.25, 250, float("inf"))

    wages_before_taxes = hours_worked_daily * hourly_wage * 350
    tax_amount = wages_before_taxes * .12
    annual_wages_after_taxes = wages_before_taxes * .88

    print("\nPay Advice\n------------------")
    print(f"Hours worked: {hours_worked_daily:,.2f} hours")
    print(f"Hourly wage: ${hourly_wage:,.2f}")
    print(f"Wages before taxes: ${wages_before_taxes:,.2f}")
    print(f"Tax amount: ${tax_amount:,.2f}")
    print(f"Annual Wages After Taxes: ${annual_wages_after_taxes:,.2f}")
main()
