# stats.py
def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_numbers[midpoint]
    else:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

def mode(numbers):
    if not numbers:
        return 0
    from collections import Counter
    counter = Counter(numbers)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [47, 34, 86, 9, 13, 9, 34, 9]
    print("Numbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()
