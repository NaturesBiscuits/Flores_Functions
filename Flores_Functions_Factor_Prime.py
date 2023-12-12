def smallest_factor(user_input):
    while True:
        if user_input < 2:
            print("Invalid input, Enter a number greater than 2.")
            user_input = int(input("Enter an integer again: "))
        else:
            break

    smallest_factor = None
    for i in range(2, user_input):
        if user_input % i == 0:
            smallest_factor = i
            break

    if smallest_factor:
        print(f"The smallest factor other than 1 for {user_input} is {smallest_factor}.")
    else:
        print(f"The smallest factor other than 1 for {user_input} is {user_input}.")


def intprimes(start, end):
    while start < 1:
        print("Enter a non-negative number")
        start = int(input("\nEnter a number [Start]: "))

    while start > end:
        print(f"Enter a number greater than {start}")
        end = int(input("\nEnter a number [End]: "))

    prime_list = []

    for calPrime in range(start, end + 1):
        if calPrime > 1:
            for posPrime in range(2, calPrime):
                if (calPrime % posPrime) == 0:
                    break
            else:
                prime_list.append(calPrime)

    print(f"Prime numbers between {start} and {end} are:", *prime_list, sep=", ")


def bothonetwo(smallest_value, start_range, end_range):
    smallest_factor(smallest_value)
    intprimes(start_range, end_range)


while True:
    print("\n--------------------------------------------------------------------")
    print("Select what you want to perform, and enter the corresponding digit.")
    print("[1]Find smallest factor other than 1.")
    print("[2]Two integers ranging its Prime Numbers.")
    print("[3]Perform both finding the smallest factor and Identifying Prime Numbers.")
    print("[4]Terminate the program.")
    print("--------------------------------------------------------------------")

    option = int(input("\nEnter your option: "))

    if option == 1:
        print("Finding smallest factor other than 1")
        smallest_factor(int(input("Enter an integer >= 2: ")))
    elif option == 2:
        print("Primes within the scope.")
        start = int(input("Enter starting value: "))
        end = int(input("Enter ending value: "))
        intprimes(start, end)
    elif option == 3:
        print("Finding both smallest factor and identifying the primes of a scope.")
        smallest_value = int(input("Enter Integer you want to have the smallest value: "))
        start_range = int(input("Enter starting value for range: "))
        end_range = int(input("Enter ending value for range: "))
        bothonetwo(smallest_value, start_range, end_range)
    elif option == 4:
        print("\nPROGRAM TERMINATED")
        break
    else:
        print("\nInvalid option, Please select only from the options (1, 2, 3 and 4).")
