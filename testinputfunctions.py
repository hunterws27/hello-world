"""File: testinputfunctions.py
Defines functions for robust input of ints and floats."""
#Hunter Standifer

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs a floating-point number,
    using the given prompt. Returns the float."""
    while True:
        theString = input(prompt)
        try:
            # Try converting input to float
            floatValue = float(theString)
            return floatValue
        except ValueError:
            print("Error: the input must be a valid floating-point number")

def main():
    n = inputInt("Please enter an integer: ")
    print(f"You entered the integer: {n}")
    
    f = inputFloat("Please enter a floating-point number: ")
    print(f"You entered the floating-point number: {f}")

if __name__ == "__main__":
    main()

