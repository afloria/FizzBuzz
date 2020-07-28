for i in range(1, 101):  # this range counts from 1 to 100

    if i % 3 == 0 and i % 5 == 0:  # this if statement checks if the number is divisible by 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # this if statement checks if the number is divisible by 3
        print("Fizz")
    elif i % 5 == 0:  # this if statement checks if the number is divisible by 5
        print("Buzz")
    else:             # a number will print out if the above statements are false
        print(i)