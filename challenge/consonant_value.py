def solve(word):
    vowels = 'aeiou'
    max_value = current_value = 0

    # Iterate through each character in the word
    for char in word:
        if char not in vowels:
            # If the character is a consonant, calculate its value and add to current_value
            current_value += ord(char) - ord('a') + 1
            
            # Check if the current cumulative value of consonants is greater than the max_value
            if current_value > max_value:
                max_value = current_value  # Update max_value if needed
        else:
            # Reset current_value to 0 when a vowel is encountered (consecutive consonants end)
            current_value = 0

    return max_value  # Return the maximum value found for consecutive consonants

# Calculate the highest value of consecutive consonants in the word "Sam"
result = solve("Sam")

# Print the result - the highest value of consecutive consonants in the word
print(f"The highest value of consonants is {result}")
