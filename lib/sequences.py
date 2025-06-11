def print_fibonacci(length):
    fibonacci_sequence = []
    if length >= 1:
        fibonacci_sequence.append(0)
    if length >= 2:
        fibonacci_sequence.append(1)
    for i in range(2, length):
        next_num = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_num)
    print(fibonacci_sequence)