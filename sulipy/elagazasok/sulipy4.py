def is_pos_or_not():
    num = int(input("Please give me a number: "))
    if num > 0 and num % 2 == 0:
        print("Thats a positive even number")
    elif num < 0 and num % 2 != 0:
        print ("That's a negative odd number")
    else:
        print("error")

is_pos_or_not()