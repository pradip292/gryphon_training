def ask_question(name):
    print(f"Sanjivani College Of Engineering - Bhushan - Games - 68 - {name}")

    congrats_count = 0

    while True:
        user_answer = input("What is the Square of 22: ")

        if user_answer == "484":
            congrats_count += 1
            print(f"Congratulations {name}!")
        else:
            print("OOPS Message or Try Again")

        if congrats_count == 3 or input("Do you want to continue? (yes/no): ").lower() == "no":
            break

# Get the name from the user
user_name = input("Enter Your Name: ")

# Call the function with the dynamic name
ask_question(user_name)
