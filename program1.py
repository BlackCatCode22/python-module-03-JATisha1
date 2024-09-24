def total_count_average():
    total = 0
    count = 0

    while True:
        user_input = input("Enter an integer or 'done' to finish: ")

        if user_input.lower() == 'done':
            break

        try:
            num = int(user_input)
            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average}")


total_count_average()
