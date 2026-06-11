# Create a variable for amount owed and a list of valid coins
# Create a continual loop where the user is asked to input a coin
# Check if the entered coin is valid, and then decrease the amount owned by that amount and continue the loop
# Once the amount owed is less than or equal to 0, break the loop and take the negative of amount owed as the change owed to user

def main():
    print("Vending Machine\n----------------")

    amount_due = 50
    valid_coins = ["1", "5", "10", "25"]

    while True:
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin:\n")
        
        if coin in valid_coins:
            amount_due -= int(coin)

            if amount_due <= 0:
                break

    print(f"Change Owed: {amount_due * -1}")

main()
