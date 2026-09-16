data = []

def inputData():
    
    size = int(input("Enter Size of Array:\n"))
    
    for i in range(size):
        items = int(input("Enter Data for a 1D array (Separated by spaces): "))
        data.append(items)
     
    print("\n Data has been stored Successfully\n")
        

def displayData():
    if len(data) == 0:
        print("Please enter data first!")
        return
    print("Data Summary: \n")
    
    totalValue()
    min()
    max()
    sum()
    avg()
    
    
def totalValue():
    j = 0
    for i in data:
        j += 1
    print(f" - Total Elements: {j}")
    return j

def min():
    min = data[0]
    for i in data:
        if i < min:
            min = i
            
    print(f" - Minimum Value: {min}")
    return min

def max():
    max = data[0]
    for i in data:
        if i > max:
            max = i
            
    print(f" - Maximum Value: {max}")
    return max
        
def sum():
    sum = 0
    for i in data:
        sum += i
    print(f" - Sum of all values: {sum}")
    return sum

def avg():
    sum = 0
    for i in data:
        sum += i
        
    j = 0
    for i in data:
         j += 1
         
    avg = sum / j
    print(f" - Average value: {avg}")
    return avg

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

def sortData():
    if len(data) == 0:
     print("Please enter data first!")
     return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    sortChoice = int(input("\nEnter your choice: "))

    if sortChoice == 1:
        data.sort()
        print("\nSorted Data in Ascending Order:")
        print(*data, sep=", ")

    elif sortChoice == 2:
        data.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
        print(*data, sep=", ")

def statistics():
    minimum = data[0]
    maximum = data[0]
    total = 0
    count = 0

    for i in data:
        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i

        total += i
        count += 1

    average = total / count

    return minimum, maximum, total, average

def filterData():
    if len(data) == 0:
        print("Please enter data first!")
        return
    threshold = int(input("Enter Threshold value to filter out data above: "))

    filteredData = list(filter(lambda x: x >= threshold, data))

    print(f"\nFiltered Data (Values >= {threshold}):")
    print(*filteredData, sep=", ")
    
    
while True:
    print("\n Welcome to Data Analyzer and Transformer Program\n")
    
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function) ")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple data)")
    print("7. exit Program")
    
    choice = int(input("Please enter your choice: "))
    
    match choice:
        
        case 1:
            inputData()
            
        
        case 2:
            displayData()
        
        case 3:
            num = int(input("\nEnter a number to calculate its factorial: "))
            result = fact(num)
            print(f"\nFactorial of {num} is: {result}")
        
        case 4:
            filterData()
        
        case 5:
            sortData()
        
        case 6:
            minimum, maximum, total, average = statistics()

            print("\nDataset Statistics:")
            print(f" - Minimum Value: {minimum}")
            print(f" - Maximum Value: {maximum}")
            print(f" - Sum of all values: {total}")
            print(f" - Average value: {average}")
        
        case 7:
            print("\nThank you for using the Data Analyzer and Transformer Program!")
            break

        case _:
            print("\nInvalid choice! Please try again.")
    