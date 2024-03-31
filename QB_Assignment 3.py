# 1-Python program to check the equality of two lists.
def check_equality(list1, list2):
    if len(list1) != len(list2):
        print("Not Equal!")
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print('Not Equal!')
            return False
    
    print('The two lists are Identical!')
    return True

# 2-Python program to remove duplicates from a list.
def remove_duplicates(list_input):
    list_out = set(list_input)
    
    unique_list = list(list_out)
    
    print(unique_list)
    return unique_list

# 3-Python Recursive Function that calculates Factorial of a number.
def factorial(n):
    if n == 1:
        return 1
    else:
        n = n * factorial(n - 1)
        return n
    
# 4-Write a recursive method that returns the nth power of 10.
def power_of_10(n):
    if n == 0:
        return 1
    else:
        return 10 * power_of_10(n - 1)

# 5- Write recursive function that takes two numbers x and y then return sum of all numbers between include x and y.
def sum_of_numbers_between(x, y):
    if x == y:
        return x
    else:
        return x + sum_of_numbers_between(x + 1, y)