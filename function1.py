#def whatName():
    #inputName = input("What is your name? ")
#whatName()

#def square(num):
    #return num * num
#print(square(2))

global_variable_example = "Foo"
def localScopeFunction():
    local_variable_example = "Bar"
    print(global_variable_example + " is Global")
    print(local_variable_example + " is Local")
#print(local_variable_example + " Is this real?")
def secondLocalScopeFunction():
    local_variable_example = "Baz"
    print(local_variable_example + " is Local")
localScopeFunction()
secondLocalScopeFunction()
