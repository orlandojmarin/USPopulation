import pydoc

'''
Orlando Marin
CSC 212 - Data Structures
Project number 1
This program reads US population data from a file and calculates the annual 
population increases. It finds and prints the years with the highest and lowest 
increases along with the corresponding population numbers. The code is 
organized into functions for getting data (getdata), calculating increases 
(calculate_differences), and displaying results (putdata).
'''

'''
Phase 1 - reading text from a file
The attached file USPopulation.txt contains the US population in thousands, 
during the years 1950 through 1990. The first line in the file contains the 
population for 1950, the second line contains the population for 1951, and so 
forth. Write a Python program to read each population number from the file and 
output it in the shell.
'''

'''
Phase 2 - using functions and reading into a list
Change your program so your main logic calls a function named getdata( ) to 
read the text file data into a list. Pass this list back to the main function. 
Create another function named putdata(list) that takes as parameter this list 
and output it in the shell.
'''

'''
Phase 3 - reporting the years with the highest and smallest population increase
You probably have already noted that the population increased every year from 
1950 to 1990. 

Using the list, create another function to generate a separate 
list for the annual increase in population. For example, if you name this new 
list annual_increase, the first cell annual_increase[0] will be 1951's 
population (153982) minus 1950's population (151868). 

The annual_increase[1] 
will be the difference between 1952 and 1951. Based on the given data, create 
this list of annual increase in population for the 40 years. Return this list 
to the main function. 

Main function will call function putdata(annual_increase) to output this list. 

The main function will then find the year with the highest 
increase and the smallest increase in the population. Output that findings with 
the year range and the population readings.
'''


def main():
    """
    Main function that orchestrates the program flow:
    reads population data from a file, calculates annual increases,
    and identifies the years with the highest and lowest increases,
    printing the relevant information.
    """
    # call the function getdata to add the content of the USPopulation.txt
    # file to the empty list
    populationList = getdata()
    
    # call the function putdata to print the list
    putdata(populationList)
    
    # Call the function calculate_differences to get the annual population 
    # increases
    populationIncreaseList = calculate_differences(populationList)
    
    # Print the population differences
    putdata(populationIncreaseList)
    
    # determine the largest increase and the smallest increase
    maxIncrease = max(populationIncreaseList)
    minIncrease = min(populationIncreaseList)
    
    # Find the corresponding indices for the highest and smallest increases
    maxIndex = populationIncreaseList.index(maxIncrease)
    minIndex = populationIncreaseList.index(minIncrease)
    
    # The years correspond to the index + 1950 (since the data starts in 1950)
    maxYearStart = 1950 + maxIndex
    minYearStart = 1950 + minIndex
    
    # Output the findings
    print(f"Highest increase: {maxIncrease} from {maxYearStart} to {maxYearStart + 1}")
    print(f"Population in {maxYearStart}: {populationList[maxIndex]}")
    print(f"Population in {maxYearStart + 1}: {populationList[maxIndex + 1]}")
    
    print(f"Smallest increase: {minIncrease} from {minYearStart} to {minYearStart + 1}")
    print(f"Population in {minYearStart}: {populationList[minIndex]}")
    print(f"Population in {minYearStart + 1}: {populationList[minIndex + 1]}")


def getdata():
    """
    Reads population data from the USPopulation.txt file and stores it in a 
    list.

    Returns:
    list: A list of population numbers for each year from 1950 to 1990.
    """
    
    # create an empty list with the population for each year from 1950 - 1990
    populationList = []
    
    # open the file USPopulation.txt
    infile = open("/Users/orlandomarin/Downloads/USPopulation.txt", "r")

    # read the file's contents into the populationList
    for line in infile:
        # strip the new line characters from the end of each line
        listLine = line.rstrip("\n")
        
        # cast each line as an int
        listLineInt = int(listLine)
        
        # add each line as an int to the end of the populationList
        populationList.append(listLineInt)
           
    # close the file
    infile.close()
        
    # return the list
    return populationList

   
def calculate_differences(populationList):
    """
    Calculates the annual population increases from a list of population 
    numbers.

    Args:
    populationList (list): A list of population numbers.

    Returns:
    list: A list of annual population increases.
    """
    # Create an empty list for the population increase
    populationIncreaseList = []
    
    # Calculate the annual increase in population
    for index in range(len(populationList) - 1):
        populationIncrease = populationList[index + 1] - populationList[index]
        populationIncreaseList.append(populationIncrease)
    
    # Return the list of population increases
    return populationIncreaseList
    

def putdata(list):
    """
    Prints the provided list of data.

    Args:
    data (list): The data to be printed.
    """
    print(list)
    
   
main()


pydoc.writedoc("main")





