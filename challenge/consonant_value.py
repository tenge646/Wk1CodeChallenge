def solve(word):
    vowels = 'aeiou'
    max_value = current_value = 0

    for char in word:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0

    return max_value
