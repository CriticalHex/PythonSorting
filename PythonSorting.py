import random

def linearSearch(list,searchNum):
    for i in range(len(list)):
        if list[i] == searchNum:
            return i;

def binarySearch(list,searchNum,currentLocation,min,max):
    
    print(int(currentLocation))

    if list[int(currentLocation)] == searchNum:
        return int(currentLocation)
    elif list[int(currentLocation)] > searchNum:
        tempCurrent = currentLocation
        currentLocation -= abs(currentLocation - min)/2
        max = tempCurrent
        binarySearch(list,searchNum,currentLocation,min,max)
    else:
        tempCurrent = currentLocation
        currentLocation += abs(currentLocation - max)/2
        min = tempCurrent
        binarySearch(list,searchNum,currentLocation,min,max)

    
if __name__ == '__main__':
    numberList = []
    for i in range(100):
        numberList.append(random.randrange(1,50))

    listHalf = len(numberList)/2

    searchNumber = random.randrange(1,50)
    print(searchNumber)
    numberList.sort()

    print("The number you're looking for is in slot", linearSearch(numberList,searchNumber))

    print()

    print("The number you're looking for is in slot", binarySearch(numberList,searchNumber,int(listHalf),0,len(numberList)))
