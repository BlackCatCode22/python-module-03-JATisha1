def max_min_numbers():
    numbers = []

    while True:
        user_input = input("Enter an integer or 'done' to finish: ")

        if user_input.lower() == 'done':
            break

        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if len(numbers) == 0:
        print("No numbers were entered.")
    else:
        print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")

max_min_numbers()
