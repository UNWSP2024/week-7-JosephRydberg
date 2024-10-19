#US_Population Joseph Rydberg 10/14/2024

def main():
    year_to_sum = 0
    all_entered_values = []
    while True:
        all_entered_values.append([input("enter year "), input("enter state "), input("enter population ")])
        if str(input("want to add more info enter, yes")) == "yes":
            continue
        else:

            year_to_sum = input("Enter year of wanted information ")
            sum_population_for_year(all_entered_values, year_to_sum)
            break
totalPopulation = 0.0

def sum_population_for_year(all_entered_values, year_to_sum):
    global totalPopulation
    for i, element in enumerate(all_entered_values):
        if all_entered_values[i][0] == year_to_sum:

            totalPopulation += float(all_entered_values[i][2])

    print("Total Population", totalPopulation)
    #Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()