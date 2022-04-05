while True:
    try:
        first_number = int(input("What is the first number you would like to add?"))
        second_number = int(input("What is the second number you would like to add?"))
        sum = first_number + second_number
        print("The sum of your two numbers is", sum)
        break
    except:
        print("Silly one. This is not an interger...")