# average.py
#Hunter Standifer

def read_numbers(filename):
    """Reads numbers from a text file and returns them as a list of floats."""
    with open(filename, 'r') as file:
        return list(map(float, file.readlines()))

def compute_average(numbers):
    """Computes the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    filename = input("Enter the name of the text file: ")
    numbers = read_numbers(filename)
    average = compute_average(numbers)
    print(f"The average of the numbers in {filename} is {average:.2f}")

if __name__ == "__main__":
    main()
