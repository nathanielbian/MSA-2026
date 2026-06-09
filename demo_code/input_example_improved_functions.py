#Program to Convert Pounds to Kilos

#INPUT (getting the data to be processed)
#Loop
def get_positive_float_input():
    while True:
        #Validate input: Ensure the data is a number type
        try:
            #Prompt user to enter weight in lbs
            user_weight = float(input("Enter weight in lbs: "))
            #Check if weight is less than 0 output error message and reprompt the user
            if user_weight <= 0:
                print("ERROR: Enter a number greater than 0\n")
                continue
            return user_weight
        except:
            print("ERROR: Please enter a number\n")
        #If input is invalid, then reprompt the user until the data is valid
    
def main():
    #INPUT (getting the data to be processed)
    user_weight = get_positive_float_input()
    #PROCESSING
    #use a conversion factor to convert lbs to kgs (2.205 lbs = 1 kg)
    lbs_to_kg = 2.205
    user_weight_in_kg = user_weight / lbs_to_kg

    #OUTPUT
    #Print the output to the user
    print(f"You weigh {user_weight_in_kg:.2f} kgs")

main()
