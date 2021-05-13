numberList = [-23,22,1,-34,34,322]

lst2 = []

lst3 = []

lst4 = []

# Medium exercise 1 - Find smallest
def findSmallest(list_of_numbers):
    smallest = list_of_numbers[0]
    for num in list_of_numbers:
        if num < smallest:
            smallest = num
    return smallest
print("The smallest number is: " + str(findSmallest(numberList)))

# Medium exercise 2 - Find largest
def findLargest(list_of_numbers):
    largest = list_of_numbers[0]
    for num in list_of_numbers:
        if num > largest:
            largest = num
    return largest
print("The largest number is: " + str(findLargest(numberList)))

# Medium exercise 3 - Find shortest string
def shortestString(list_of_strings):
    smallestString = list_of_strings[0]
    for string in list_of_strings:
        if  len(smallestString) > len(string):
            smallestString = string
    return smallestString
print("The shortest string is: " + str(shortestString(['foo', 'their', 'binance', 'otis','as','a'])))

# Medium exercise 4 - Find largest string
def largestString(list_of_strings):
    largestString = list_of_strings[0]
    for string in list_of_strings:
        if len(largestString) < len(string):
            largestString = string
    return largestString
print("The largest string is: " + str(largestString(['foo', 'their', 'binance', 'otis','as'])))