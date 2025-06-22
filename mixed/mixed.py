def fibonacci(n):
    if n <= 0:
        return []
    elif n = 1:
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
        break
    return int(length)

print(fibonacci(get_length())
