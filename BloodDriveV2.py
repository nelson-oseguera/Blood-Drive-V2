# Nelson Oseguera

# April 22, 2023

# Programming Project 10

# The American Red Cross wants you to write a program that will calculate the average pints of blood donated during a blood drive.  The program should take in the number of pints donated during the drive, based on a seven hour drive period.  The average pints donated during that period should be calculated and written to a file.  If the user wants to print data from the file, read it in and then display it.  Store the pints per hour and the average pints donated in a file called blood.txt.

# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        print()
        print('Enter 1 to enter in new data and store to file')
        print('Enter 2 to display data from the file')
        option = int(input('Enter now ->'))
        print()

        #declare variables
        pints = [0] * 7
        totalPints = 0
        averagePints = 0

        if option == 1:
            # function calls
            pints = getPints(pints)
            totalPints = getTotal(pints)
            averagePints = getAverage(totalPints)
            writeToFile(averagePints, pints)
        elif option == 2:
            readFromFile(averagePints, pints)

        endProgram = input('Do you want to end program?(Enter no or yes): ')
        while not(endProgram == 'yes' or endProgram == 'no'):
            print('please enter a yes or no')
            endProgram = input('Do you want to end program?(Enter no or yes): ')

# the getPints function
def getPints(pints):
    counter = 0
    while counter < 7:
        pints[counter]=int(input('Enter pints collected:'))
        counter = counter + 1
    return pints

# the get total function
def getTotal(pints):
    counter = 0
    totalPints = 0
    while counter < 7:
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints

# the getAverage function
def getAverage(totalPints):
    averagePints = float(totalPints) / 7
    return averagePints

# the writeToFile function
def writeToFile(averagePints, pints):
    outFile = open('blood.txt','a')
    outFile.write('Pints Each Hour')
    counter = 0
    while counter < 7:
        outFile.write(str(pints[counter]) + '\n')
        counter = counter + 1
    outFile.write('AveragePints\n')
    outFile.write(str(averagePints)+'\n\n')
    outFile.close

# the readFromFile function
def readFromFile(averagePints, pints):
    inFile = open('blood.txt', 'r')
    str1 = inFile.read()
    print(str1)
    pints = inFile.read()
    print(pints)
    print() #adds a blank line
    averagePints = inFile.read()
    print(averagePints)
    inFile.close()

# start the program
main()
