height = float(input("Enter the height in feet that the ball was dropped from: "))
bounces = int(input("Enter how many times the ball bounces: "))
bounceRatio = .6
totalDistance = height

for eachPass in range(bounces):
        height *= bounceRatio
        totalDistance += 2 * height

totalDistance = totalDistance - height
print("The distance the ball traveled was", totalDistance, "ft")

        


        
