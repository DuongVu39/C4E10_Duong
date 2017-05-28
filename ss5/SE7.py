
def get_even_list(integer_list):
    new_list=[]
    for num in integer_list:
        if num % 2 == 0:
            new_list.append(num)
    return (new_list)

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

