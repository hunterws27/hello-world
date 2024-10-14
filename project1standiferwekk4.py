sideA = float(input("Enter the length of the first side: "))
sideB = float(input("Enter the length of the second side: "))
sideC = float(input("Enter the length of the third side: "))

if sideA == sideB and sideA == sideC:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
