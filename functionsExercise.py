#1. Madlib Function
def make_formal_greeting(name, game):
    return ("%s's favorite video game is %s" % (name, game))
def ask_for_user_info():
    name = input("What is your name? ")
    game = input("What is favorite video game? ")
    if len(name) < 1 or len(game) < 1:
        print("Terminating since you don't want to play along >:(")
    else:
        print(make_formal_greeting(name, game))
#ask_for_user_info()

#2. Celsius to Fahrenheit conversion
def celsiusToFahrenheit():
    num = input("Enter temperature in Celsius: ")
    return print((float(num) * 9/5) + 32)
#celsiusToFahrenheit()

#3. Fahrenheit to Celcius conversion
def fahrenheitToCelsius():
    num = input("Enter temperature in Fahrenheit: ")
    return print((float(num) - 32) * 5/9)
#fahrenheitToCelsius()

#4. is_even function
def is_even():
    num = input("Enter a number to find out if even: ")
    if int(num) % 2 == 0:
        return print("True")
    else:
        return print("False")
is_even()

#5. is_odd function, first one is ez second one uses is_even()
def is_odd():
    num = input("Enter a number to find out if odd: ")
    number = is_even(num)
    if int(number) % 2 != 0:
        return print("True")
    else: 
        return print ("False")
is_odd()

#6. only_evens function using is_even
#def only_evens()
#def only_evens(list):
    #new_list = []
    #for num in list:
        #if num % 2 == 0:
            #new_list.append(num)
    #return print()

#only_evens([11, 20, 42, 97, 23, 10])

#7. only_odds function using is_odd
#def only_odds()