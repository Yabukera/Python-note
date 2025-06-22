### **Fixed Solutions**:
<details>
<summary>Project 1 Solution</summary>

```python
def calculate_total():
    adult_price = 25  # Removed quotes
    child_price = 12
    discount = 5
    
    adults = 3
    children = 2
    
    total = (adult_price * adults) + (child_price * children)
    final_total = total - discount  # Fixed discount logic
    
    print("Final Price: $" + str(final_total))

calculate_total()
```
</details>

<details>
<summary>Project 2 Solution</summary>

```python
def print_tables():
    for i in range(1, 6):  # Added colon
        result = i * 3
        print(f"3 x {i} = {result}")

def sum_numbers():
    total = 0
    numbers = [5, 10, 15, 20]  # Removed quotes
    for num in numbers:
        total += num
    print("Total:", total)

print_tables()
sum_numbers()
```
</details>

<details>
<summary>Project 3 Solution</summary>

```python
def countdown():
    counter = 5
    while counter > 0:
        print(counter)  # Fixed indentation
        counter -= 1
    print("Go!")

def get_age():
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            break
        print("Invalid input!")  # Moved inside loop
    print(f"Age: {age}")  # Removed redundant conversion

countdown()
get_age()
```
</details>

<details>
<summary>Project 4 Solution</summary>

```python
def average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)  # Fixed variable name
    return avg

def find_max(nums):  # Added parameter
    max_val = nums[0]  # Proper initialization
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

nums = [4, 7, 1, 9]
print("Average:", average(nums))
print("Max Value:", find_max(nums))  # Passed argument
```
</details>

<details>
<summary>Project 5 Solution</summary>

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:  # Fixed comparison operator
        return [0]
    
    a, b = 0, 1
    sequence = [a, b]
    
    for i in range(2, n):
        next_num = a + b
        sequence.append(next_num)
        a = b
        b = next_num
    
    return sequence

def get_length():
    while True:
        length = input("Sequence length: ")
        if length.isdigit() and int(length) > 0:
            break  # Fixed indentation
    return int(length)

print(fibonacci(get_length()))
```
</details>

