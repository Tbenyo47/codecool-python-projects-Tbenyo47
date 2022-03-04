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
    

print(min(input("Set first number: "), input("Set second number: ")))



#MAX FÜGGVÉNY -> KÉSZ
def max(values_list):
    biggest = values_list[0]
    for x in values_list:
        if biggest < x:
            biggest = x
    return biggest

print(max(values_list))


#LEN FÜGGVÉNY -> KÉSZ
def len(values_list):
    lenght = 0
    for item in values_list :
        lenght = lenght+1
    return(lenght)
    

print(len(values_list))


#MULTIPLY FÜGGVÉNY -> KÉSZ
def multiply(x, y):
    i = 1
    xbasic = x
    while i < y:
        x = x + xbasic
        i += 1
    return x
    
print(multiply(int(input("Set first number: ")), int(input("Set second number: "))))


#POW FÜGGVÉNY -> KÉSZ
def pow(x, y):
    i = 1
    xbasic = x
    while i < y:
        x = x * xbasic
        i += 1
    return x
    
print(pow(int(input("Set first number: ")), int(input("Set second number: "))))




def divmod(x, y):
    i = 0
    while y <= x:
        x -= y
        i += 1
    answer = [i, x]
    return answer
   
    
print(divmod(int(input("Set first number: ")), int(input("Set second number: "))))

