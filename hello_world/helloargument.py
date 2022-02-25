def get_hello_message():
 userName = input("What's your name? ")
 if len(userName) != 0:
    return("Hello, " + userName.capitalize() + ("!"))
 else:
    return("Hello, World!")


def say_hello():
 answer = get_hello_message()
 print(answer)

say_hello()