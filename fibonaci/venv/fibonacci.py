def compute_nth_fib(num):
    # if base case...
    if num < 0:

        print("Incorrect input")

        # First Fibonacci number is 0
    elif num == 0:
        # return base case value ...
        return 0
    # second base case
    # Second Fibonacci number is 1
    elif num == 1:
        # return base case value ...
        return 1
    else:
        # recursively call compute_nth_fib() ...
        return compute_nth_fib(num - 1) + compute_nth_fib(num - 2)


# Driver Program

n = int(input('Enter fib(number)'))
print(compute_nth_fib(n))
