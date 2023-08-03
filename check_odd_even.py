"""
[*args] Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.
"""

#########################################################

def check_odd_even(number: int) -> str:
    """
    Check if a given integer is even or odd using a ternary operator.

    Args:
        number (int): The integer to check.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    return "Even" if number % 2 == 0 else "Odd"

def main():
    """
    Test the check_odd_even function with a sample integer.
    """
    number = 5
    result = check_odd_even(number)
    print(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()
