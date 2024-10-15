#Joseph Rydberg RainFall 10/14/2024

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
rainfall = []
largestRainFall = 0.0
largestRainFallMonth = 0.0
smallestRainFall = 999999.0
smallestRainFallMonth = 0.0
totalRainFalls = 0.0

def enter_rainfall():
    for i in months:
        print("rainfall in month ", i)
        rainfall.append(float(input()))

    rain_calculations()

def rain_calculations():
    global largestRainFall
    global smallestRainFall
    global largestRainFallMonth
    global smallestRainFallMonth
    global totalRainFalls

    for i, element in enumerate(rainfall):
        totalRainFalls += element
        if rainfall[i] > largestRainFall:
            largestRainFall = rainfall[i]
            largestRainFallMonth = rainfall.index(i + 1)

        if rainfall[i] < smallestRainFall:
            smallestRainFall = rainfall[i]
            smallestRainFallMonth = rainfall.index(i + 1)

    print("Average Rainfall", totalRainFalls/12)
    print("Largest Rainfall", largestRainFall, "in month", largestRainFallMonth)
    print("Smallest Rainfall", smallestRainFall, "in month", smallestRainFallMonth)

enter_rainfall()