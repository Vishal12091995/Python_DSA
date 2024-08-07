# Reverse  an array in provided list
list=[a for a in input("enter number with space").split(" ")]
# print(list[::-1])

# by using function

def reverse_list(list):
    list.reverse()
    return " ".join(list)


print(reverse_list(list))
