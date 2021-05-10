def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))
#mustard = make_formal_greeting("Mustard", "Colonel")
#print(mustard)

def ask_for_user_info():
    name = input("What is your name? ")
    title = input("What is your title? ")
    print(make_formal_greeting(name, title))
            #^^^This is a call back (calls back to another function)
ask_for_user_info()
