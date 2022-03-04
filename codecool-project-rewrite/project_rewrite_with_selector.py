#GLOBÁLIS LISTA 
values_list = [1, 4, 11, 2, 7, 10,]


#MIN FÜGGVÉNY -> KÉSZ
def min(x, y):
   if int(x) > int(y):
    answer = y
    return y
    
   else:
    answer = x
    return x
    





#MAX FÜGGVÉNY -> KÉSZ
def max(values_list):
    biggest = values_list[0]
    for x in values_list:
        if biggest < x:
            biggest = x
    return biggest




#LEN FÜGGVÉNY -> KÉSZ
def len(values_list):
    lenght = 0
    for item in values_list :
        lenght = lenght+1
    return(lenght)
    




#MULTIPLY FÜGGVÉNY -> KÉSZ
def multiply(x, y):
    i = 1
    xbasic = x
    while i < y:
        x = x + xbasic
        i += 1
    return x
    



#POW FÜGGVÉNY -> KÉSZ
def pow(x, y):
    i = 1
    xbasic = x
    while i < y:
        x = x * xbasic
        i += 1
    return x
    


#DIVMOD FÜGGVÉNY -> KÉSZ
def divmod(x, y):
    i = 0
    while y <= x:
        x -= y
        i += 1
    answer = [i, x]
    return answer
   

selector = int(input('Please select a function to try: 1-min() 2-max() 3-len() 4-multiply() 5-pow() 6-divmod()'))

if selector == 1:
    print("Please give me 2 numbers and I will tell you the lesser")
    print(min(input("Set first number: "), input("Set second number: ")))
elif selector == 2:
    print("I will tell you the greatest number in my list! It's: ")
    print(max(values_list))
elif selector == 3:
    print("I will tell you how long my list is! It's:")
    print(len(values_list))
elif selector == 4:
    print("Give me 2 numbers so I can multiply them for you!")
    print(multiply(int(input("Set first number: ")), int(input("Set second number: "))))
elif selector == 5:
    print("If you give me 2 numbers I will do my best impression of python's pow() function! Yeeey!")
    print(pow(int(input("Set first number: ")), int(input("Set second number: "))))
elif selector == 6:
    print("If you give me 2 numbers I will do my impression of python's divmod function. My creator is still not really sure how this is works")
    print(divmod(int(input("Set first number: ")), int(input("Set second number: "))))
else:
    print("Please choose a valid option! Thats all I can do so far... :(")
