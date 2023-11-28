def two_positive(a, b, c):
    # Create a list 'positives' containing all values greater than 0 from the input arguments
    positives = [x for x in [a, b, c] if x > 0]

    # Check if the length of the 'positives' list is equal to 2
    # This checks if exactly two numbers among the input arguments are positive
    return len(positives) == 2

# Example usage: Check if exactly two out of the three numbers (1, 2, 3) are positive
print(two_positive(1, 2, 3))
