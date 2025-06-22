def average(numbers):
    total = sum(numbers)
    avg = total / len(number)
    return avg

def find_max():
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

nums = [4, 7, 1, 9]
print("Average:", average(nums))
print("Max Value:", find_max())
