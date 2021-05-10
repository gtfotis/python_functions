def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

def ask_for_user_info():
    name = input("What is your name? ")
    title = input("What is your title? ")
    return [name, title]

def ask_for_user_info_dictionary():
    name = input("What is your name? ")
    title = input("What is your title? ")
    return {
        "name": name,
        "title": title
    }

#print(ask_for_user_info())
user_info = ask_for_user_info_dictionary()
greeting = make_formal_greeting(user_info['name'], user_info['title'])
print(greeting)