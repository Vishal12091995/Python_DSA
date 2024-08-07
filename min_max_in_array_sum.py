# Input list of numbers as space-separated values
input_list = [int(a) for a in input("Enter numbers with space: ").split(" ")]

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sorting the first half
        merge_sort(left_half)

        # Recursively sorting the second half
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test the merge_sort function
merge_sort(input_list)

# Print the max and min numbers in the list
print("Sorted list: ", input_list)
print("Max number in this list is: ", input_list[-1])
print("Min number in this list is: ", input_list[0])
print("Sum of Min and Max number in an array is : ", input_list[0]+input_list[-1])
