# Initialize a variable for amount owed and a set of valid coins
# Create a loop which runs while the amount owed is greater than 0 where the user is continually asked of inputs
# Check if the entered coin is in the set of valid coins, and then decrease the amount owned by that amount
# After the loop ends, output the negative of amount owed as the change owed to user

def main():
    print("Vending Machine\n----------------")

    amount_due = 50
    valid_coins = {"1", "5", "10", "25"}

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin:\n")
        
        if coin in valid_coins:
            amount_due -= int(coin)

    print(f"Change Owed: {amount_due * -1}")

main()
