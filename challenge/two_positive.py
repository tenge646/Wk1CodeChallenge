# two_positive.py

def two_positive(a, b, c):
    positives = [x for x in [a, b, c] if x > 0]
    return len(positives) == 2
