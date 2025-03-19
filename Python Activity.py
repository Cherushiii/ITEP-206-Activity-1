def detect_letter_type():
    while True:
        letter = input("Enter a letter (or type 'exit' to go back): ")
        if letter.lower() == "exit":
            return
        if len(letter) == 1 and letter.isalpha():
            if letter in "AEIOUaeiou":
                print(f"{letter} is a Vowel.")
            else:
                print(f"{letter} is a Consonant.")
        else:
            print("Invalid input! Please enter a single letter.")


def check_odd_even():
    while True:
        number = input("Enter a number (or type 'exit' to go back): ")
        if number.lower() == "exit":
            return
        try:
            num = int(number)
            if num % 2 == 0:
                print(f"{num} is Even.")
            else:
                print(f"{num} is Odd.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def detect_special_character():
    while True:
        char = input("Enter a character (or type 'exit' to go back): ")
        if char.lower() == "exit":
            return
        if len(char) == 1:
            if not char.isalnum():
                print(f"{char} is a Special Character.")
            else:
                print(f"{char} is NOT a Special Character.")
        else:
            print("Invalid input! Please enter only one character.")


def analyze_string():
    while True:
        user_input = input("Enter a string to analyze (or type 'exit' to go back): ")
        if user_input.lower() == "exit":
            return
        if user_input:
            for char in user_input:
                if char.isalpha():
                    print(f"{char} is a Vowel.") if char in "AEIOUaeiou" else print(f"{char} is a Consonant.")
                elif char.isdigit():
                    print(f"{char} is Even.") if int(char) % 2 == 0 else print(f"{char} is Odd.")
                else:
                    print(f"{char} is a Special Character.")
        else:
            print("Please enter at least one character!")


# Main Program Loop
while True:
    print("\nChoose an option:")
    print("1. Detect Letter Type (Vowel/Consonant)")
    print("2. Check if a Number is Odd or Even")
    print("3. Identify Special Characters")
    print("4. Analyze a Full String")
    print("Type 'stop' to exit the program.")

    choice = input("Enter your choice: ")

    if choice.lower() == "stop":
        print("Exiting program... Goodbye!")
        break
    elif choice == "1":
        detect_letter_type()
    elif choice == "2":
        check_odd_even()
    elif choice == "3":
        detect_special_character()
    elif choice == "4":
        analyze_string()
    else:
        print("Invalid selection! Please choose a valid option.")
