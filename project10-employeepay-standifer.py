hourlyWage = float(input("Hourly wage: "))
hoursWorked = float(input("Amount of hours worked not including overtime: "))
overtimeHours = float(input("Amount of overtime hours: "))

overtimeWage = hourlyWage * 1.5
totalHourly = hourlyWage * hoursWorked
totalOvertime = overtimeWage * overtimeHours
totalPay = totalHourly + totalOvertime
print("The total pay is $",totalPay)
