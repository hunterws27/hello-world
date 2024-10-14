initialPopulation = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the growth rate (must be greater than 0): "))
growthPeriod = int(input("Enter the number of hours to achieve this growth rate: "))
totalHours = int(input("Enter the total number of hours for growth: "))

finalPopulation = initialPopulation
periods = totalHours // growthPeriod
for eachPass in range(periods):
    finalPopulation *= growthRate

print("The new population is:", int(finalPopulation))
