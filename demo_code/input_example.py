#Program to Convert Pounds to Kilos

#INPUT (getting the data to be processed)
#Prompt user to enter weight in lbs
user_weight = float(input("Enter weight in lbs: "))

#PROCESSING
#use a conversion factor to convert lbs to kgs (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

#OUTPUT
#Print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kgs")
