def main():
    my_name = "nathaniel"

    # Capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # Make a string uppercase
    print(f"My name uppercase: {my_name.upper()}")

    # Make a string lowercase
    last_name = "BIAN"
    print(f"My full name lowercase: {my_name.lower()} {last_name.lower()}")

    # Compare two strings
    my_name_title_case = "Nathaniel"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal")
    else:
        print("The strings are not equal")

    print("\nUsing the Startswith() Method\n--------------")
    # Determine if a string starts with a set of characters
    print(f"{my_name} starts with a N or n: {my_name.startswith("N") or my_name.startswith("n")}")

    if not my_name.startswith("Nath") and not my_name.startswith("nath"):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    if my_name.lower().startswith("nath"):
        print(f"You spelled {my_name} correctly")
    else:
        print(f"You spelled {my_name} incorrectly")

    print("\nUsing the Endswith() Method\n--------------")
    print(f"{my_name} ends with \"iel\": {my_name.endswith("iel")}")

    print("\nUsing the Find() Method\n--------------")
    # Find the i in Nathaniel
    search_letter = "i"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"The {search_letter} is at index {index_of_substring}")
    else: 
        print(f"There is no {search_letter} in {my_name}")

    print("\nLooping Through a String\n--------------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} characters")
    # Print letters in a string with index positions
    for letter_index, letter in enumerate(my_name):
        print(f"Letter {letter_index + 1}: {letter}")

    print("\nSearch a String\n--------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    # Write code that counts the number of occurences of the word dog in the sentence
    # Expected output: 3

    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    
    while (pos := sentence.find(search_word, start_index)) != -1:
        number_of_dogs += 1
        start_index = pos + 1

    print(f"There are {number_of_dogs} {search_word}(s) in the sentence")

    # Using the split() method
    print("\nUsing Split\n--------------")
    # Format: make, model, year, price, engine_size
    car_info = "Ferrari,F-50,2025,500000,4.8\n"
    car_data = car_info.split(",")
    
    print(f"Car data: {car_data}")

    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price: ${price:,.2f} - Engine Size: {engine_size}")

    # Use substring
    start_index = 0
    index_of_comma = car_info.find(",")

    substring = car_info[start_index: index_of_comma]
    print(f"Make: {substring}")

main()
