# quest 3 odd and even numbers 
for attempt in range(4):
    try:
        number = int(input("Enter any number: "))
    except ValueError:
        print("Invalid input - please enter an integer.")
        continue

    if number < 0:
        print("Invalid input - negative number not allowed.")
    elif number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
