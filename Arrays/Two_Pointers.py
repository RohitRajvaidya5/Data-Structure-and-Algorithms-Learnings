import array as arr


def pair_sum(array, target):
    array = list(array)
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return (array[left], array[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

numbers = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
target_sum = 10
result = pair_sum(numbers, target_sum)
if result:
    print(f"Pair found: {result[0]} + {result[1]} = {target_sum}")
else:
    print("No pair found that sums to the target.")