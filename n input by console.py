def even_numbers(n):
    """
    Generate even numbers between 0 and n (inclusive).

    Parameters:
    - n (int): Upper limit for the range of numbers.

    Yields:
    - int: Even numbers between 0 and n.
    """
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            result = even_numbers(n)
            print("Even numbers between 0 and", n, "are:", end=" ")
            print(*result, sep=", ")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
