while True:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    
    if second_number == 0:
        print("Error: Cannot divide by zero!")
        continue
    
    result = first_number / second_number
    print(f"Result of division: {result}")
    
    continue_choice = input("Do you want to continue? (yes/no): ").lower()
    
    if continue_choice == "no":
        break
    
print("Program ended. Thank you!")