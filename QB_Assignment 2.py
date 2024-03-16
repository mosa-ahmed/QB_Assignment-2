# 1 ==> Even numbers and odd numbers in a list
def even_odd_numbers():
    try:
        list_1 = eval(input('Enter a list of numbers: '))
        even_list = []
        odd_list = []
        for i in list_1:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        print(f'Even Numbers are ==> {even_list}')
        print(f'Odd Numbers are ==> {odd_list}')
    except:
        print('Please Enter Valid Inputs!')




# 2 ==> Second largest number and Second smallest numbers in a list
def largest_smallest_numbers():
    try:
        list_1 = eval(input('Enter a list of numbers: '))
        list_1.sort()
        second_smallest_number = list_1[1]
        second_largest_number = list_1[len(list_1) - 2]
        print(f'Second Smallest Number ==> {second_smallest_number}')
        print(f'Second Largest Number ==> {second_largest_number}')
    except:
        print('Please Enter Valid Inputs!')



# 3 ==> Removing the 0th, 4th and 5th elements from a list
def removing_elements():
    try:
        list_1 = eval(input('Enter a list of at least 6 elements: '))
        del(list_1[5])
        del(list_1[4])
        del(list_1[0])
        print(list_1)
    except IndexError:
        print('Please Enter a list of at least 6 elements :)')
    except:
        print('Please check again!')

