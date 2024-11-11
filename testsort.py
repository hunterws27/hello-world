# testsort.py
#Hunter Standifer

def isSorted(lst):
    """Checks if a list is sorted in ascending order."""
    if len(lst) < 2:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def main():
    # Prompt the user for input
    user_input = input("Enter a list of numbers separated by spaces: ")
    # Convert the input string into a list of integers
    lst = list(map(int, user_input.split()))
    
    # Check if the list is sorted and print the result
    if isSorted(lst):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")

if __name__ == "__main__":
    main()
