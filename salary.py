import math
years = int(input("Enter the number of years taught: "))
salary = int(input("Enter the starting salary: "))
increasePercent = int(input("Enter the percent of annual increase: "))
year = 1
print(f"{'Year':<10}{'Salary':<15}")
print("-" * 25)

while year <= years and year <= 10:
    salary = salary * (increasePercent / 100 + 1)
    print(f"{year:<10}${round(salary, 2):<15.2f}")
    year += 1
