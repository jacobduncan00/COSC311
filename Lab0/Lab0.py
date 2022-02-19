# Function to calculate the house with the lowest price
def calculateMin(houseList):
    # Assign starting 'placeholder' dict with large price
    minPriceHouse = {"Price": 100000} 
    # Iterate through all houses in our 'houseList' list of dicts
    for house in houseList:
        # Compare the price of the current iteration house with the minPriceHouse already set
        if int(house["Price"]) < int(minPriceHouse["Price"]):
            # If condition holds, assign it as the new lowest price house
            minPriceHouse = house 

    # Return that house dict
    return minPriceHouse 


# Function to calculate the house with the highest price
def calculateMax(houseList):
    # Assign starting 'placeholder' dict with no price
    maxPriceHouse = {"Price": 0} 
    # Iterate through all houses in our 'houseList' list of dicts
    for house in houseList:
        # Compare the price of the current iteration house with the maxPriceHouse already set
        if int(house["Price"]) > int(maxPriceHouse["Price"]):
            # If condition holds, assign it as the new highest price house
            maxPriceHouse = house 

    # Return that house dict
    return maxPriceHouse

# Function to calculate the mean price of all houses
def calculateMean(houseList):
    # Set sum variable to be zero
    sum = 0
    # Iterate over all houses in our 'houseList' list of dicts
    for house in houseList:
        # Add the price of the current iteration house to the sum
        sum = sum + int(house["Price"])

    # Return the mean by dividing the sum by the number of houses
    return round(sum / len(houseList)) 


def main():
    import csv
    filename = open("house-prices.csv", "r")
    file = csv.DictReader(filename)
    # List for all dicts to be held in
    houseList = []
    # Iterate through all rows in the csv
    for row in file:
        # Append them to houseList
        houseList.append(row)
        
    
    # Get values back from functions
    minPrice = calculateMin(houseList)
    maxPrice = calculateMax(houseList)
    meanPrice = calculateMean(houseList)


    # Pretty print all key / values the corresponding house dict has
    print(f"House with Minimum Price: ${minPrice['Price']}")
    print("========================")
    print(f"Home: {minPrice['Home']}")
    print(f"Price: ${minPrice['Price']}")
    print(f"SqFt: {minPrice['SqFt']}")
    print(f"Bedrooms: {minPrice['Bedrooms']}")
    print(f"Bathrooms: {minPrice['Bathrooms']}")
    print(f"Offers: {minPrice['Offers']}")
    print(f"Brick: {minPrice['Brick']}")
    print(f"Neighborhood: {minPrice['Neighborhood']}")
    print("========================")
    print("")
    print(f"House with Maximum Price: ${maxPrice['Price']}")
    print("========================")
    print(f"Home: {maxPrice['Home']}")
    print(f"Price: ${maxPrice['Price']}")
    print(f"SqFt: {maxPrice['SqFt']}")
    print(f"Bedrooms: {maxPrice['Bedrooms']}")
    print(f"Bathrooms: {maxPrice['Bathrooms']}")
    print(f"Offers: {maxPrice['Offers']}")
    print(f"Brick: {maxPrice['Brick']}")
    print(f"Neighborhood: {maxPrice['Neighborhood']}")
    print("========================")
    print("")
    print(f"Mean House Price: ${meanPrice}")



if __name__ == "__main__":
    main()
