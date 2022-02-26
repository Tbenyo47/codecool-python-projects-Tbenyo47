def get_hello_message(name):
   if not name:
      name = "World"
   return f'Hello, {name}!'

def get_user_name():
    userName = input("What's your name? ")
    return userName.capitalize()

 
 
def say_hello():
   outputName = get_user_name()
   answer = get_hello_message(outputName)
   print (answer) 


say_hello()