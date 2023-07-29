# Example Datasets

my_dataset=[{ "name": "James", "class": "FC01", "exam score": 75, "coursework score": 45 },
{ "name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85 },
{ "name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75 },
{ "name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55 },
{ "name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80 },
{ "name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75 }]

'''
my_dataset=[{ "name": "Amir", "class": "FC01", "exam score": 75, "coursework score": 45 },
{ "name": "Amin", "class": "FC02", "exam score": 95, "coursework score": 85 },
{ "name": "Abbas", "class": "FC02", "exam score": 85, "coursework score": 75 },
{ "name": "Auklin", "class": "FC01", "exam score": 75, "coursework score": 55 },
{ "name": "Amine", "class": "FC01", "exam score": 80, "coursework score": 80 },
{ "name": "Atez", "class": "FC02", "exam score": 90, "coursework score": 75 }]
'''
'''
my_dataset=[{ "name": "James", "class": "FC01", "exam score": 75, "coursework score": 45, "age": 19 },
{ "name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85, "age": 18 },
{ "name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75, "age": 19 },
{ "name": "Tariq", "class": "FC03", "exam score": 75, "coursework score": 55, "age": 21 },
{ "name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80, "age": 21 },
{ "name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75, "age": 20 },
{ "name": "Tina", "class": "FC03", "exam score": 85, "coursework score": 95, "age": 17 }]
'''
# This function is for checking whether the key exists or not.
def existCheck(dataset, key): #It receives the dataset and key as parameters and return a boolean.
    if key in dataset[0].keys():
        return True
    else: 
        return False

# This function is for checking whether the key value is integer or not.
def integerCheck(dataset, key): #It receives the dataset and key as parameters and return a boolean.
    if type(dataset[0][key])==int: #If the type of the value of the key is an integer, it will return True, otherwise, it will return False.
        return True
    else:
        return False
    
# This function is to ask the user whether he/she wants to continue or not.
def continueCheck(): #It receives no parameter and return a boolean.
    answer=input("\nDo you want to continue testing this algorithm? If Yes, type 'y', if no, type 'n'. Your answer: ").lower() 
    #In case the user types uppercase character, the lowercase character is automatically changed not to show error status.
    if answer=='y': #If the user types 'y' or 'Y', it will return True, otherwise, it returns False.
        return True
    else:
        return False

# This function is to add the elements into the list
def add(myList,data): #It receives two parameters, the data to be added and the list in which the data is added.
    myList+=[data]
    return myList  #After the data is added, the function will return the updated list. 

# This function is to show an error message for non-existing keys
def nonExistKey():
    noKeyErrorMessage="Sorry! This key is not included in this datalist."
    return noKeyErrorMessage

#This function is to perform filtering algorithm.
def filter(dataset, key,keyvalue): #It receives 3 parameters, dataset, key and keyvalue. It returns a filtered list.
    filtered_list=[] #An empty list is initialized as a new filtered list
    for item in dataset:  #For every item in the dataset list, if the key value is the same as the one to be filtered, that item will be added into the new filtered list.
        if item[key]==keyvalue:
            filtered_list=add(filtered_list, item)
    return filtered_list

#This function is to perform aggregation algorithm.
def aggregate(dataset, key): #It receives 2 parameters, dataset, and key. It returns an aggregation value.
    sum=0 #Sum and count are initialized as 0.
    count=0
    for item in dataset: #For every item in the dataset list, the value of the key is added to the sum and in every loop, count is incremented by one
        sum+=item[key]
        count+=1
    average=round(sum/count, 2) #The average can be obtained by dividing the sum by count and the answer is rounded to two decimal numbers.
    return average

#This function is to perform sorting algorithm. This specifically is a bubble sort algorithm.
def sort(dataset, key): #It receives 2 parameters, dataset and key. It returns a sorted list.
    length=len(dataset) #Length of the dataset
    for item in range (length-1): #Outer Loop
        unsortedLength=length-item-1 #The unsorted length in each loop
        for item in range(unsortedLength): #Inner loop
            if dataset[item][key]>dataset[item+1][key]: #If the value of an item is greater than that of an item next to it, these two items are flipped. 
                dataset[item],dataset[item+1]=dataset[item+1],dataset[item]
    return dataset

# It is a main Do-while Loop. It will stop when the user enters 'z'.
while True:
    #First, the user is asked for the function he/she wants to perform and store it in the variable "my_function".
    # In case the user writes in uppercase character, the lowercase character is changed not to show error status.
    my_function=input("Which function do you want to perform? Type the letter. 'f' for filter, 'a' for aggregate, 's' for sort and 'z' for stop. Your answer: ").lower()
    
    # Filter Function works when the user types 'f'.
    if my_function=='f':
        # It's a do-while loop. It will stop when the continue_check is false.
        while True:
            key=input("Enter the key in the dataset that you want to filter: ") #First, the filtering key is asked to the user.
            result1=existCheck(my_dataset,key) #The filtering key is checked whether it exists or not. If it doesn't exist, the error message is shown to the user.
            if result1==True: #If the key exists, the value of the key is checked whether it is an integer or not.
                result2=integerCheck(my_dataset,key)
                # Then, the value of the filtering key is asked to the user.
                if result2==True: #If the value is an integer, the value will be casted into an integer.
                    keyvalue=int(input("Enter the key value: "))
                else: #If the value is not an integer, it is not necessary to cast into an integer.
                    keyvalue=input("Enter the key value: ")
                filtered_list=filter(my_dataset,key,keyvalue) #The dataset is filtered using the filtering key and the key value. The filtered list will be stored in the variable 'filtered_list'.
                print("The filtered List using the key '"+key+ "' and the keyvalue '"+ str(keyvalue)+ "'")
                print(filtered_list) #Finally, the filtered list is printed.
            else:
                print(nonExistKey())
            continue_check=continueCheck() #Then, the user is asked whether he/she wants to continue or not.
            if continue_check==False: #If the continue_check is False, the loop stops.
                break

    # Aggregate Function works when the user types 'a'.
    elif my_function=='a':
        # It's a do-while loop. It will stop when the continue_check is false.
        while True:
            key=input("Enter the key that you want to aggregate: ")#First, the aggregration key is asked to the user.
            result1=existCheck(my_dataset,key) 
            #The aggregation key is checked whether it exists or not. If it doesn't exist, the error message is shown to the user.
            if result1==True: 
                #If the key exists, the value of the aggregation key is checked whether it is an integer or not. If the value is not an integer, the error message is shown to the user.
                result2=integerCheck(my_dataset,key)
                if result2==True: #If the value is an integer, the average value is calculated and finally, print it to the user.
                    average=aggregate(my_dataset,key)
                    print("The aggregation of '"+key+ "' is "+str(average))
                else:
                    print("Sorry! Invalid Key to find the aggregation.")
            else: 
                print(nonExistKey())
            continue_check=continueCheck() #Then, the user is asked whether he/she wants to continue or not.
            if continue_check==False: #If the continue_check is False, the loop stops.
                break

    # Sort Function works when the user types 's'.
    elif my_function=='s':
        # It's a do-while loop. It will stop when the continue_check is false.
        while True:
            key=input("Enter the key that you want to sort: ") #First, the sorting key is asked to the user.
            #The sorting key is checked whether it exists or not. If it doesn't exist, the error message is shown to the user.
            result1=existCheck(my_dataset,key)
            if result1==True: #If the key exists, the datalist is sorted using the sorting key and finally, print it to the user.
                sortedList=sort(my_dataset, key)
                print("The sorted List using the key '"+ key+ "'")
                print(sortedList)
            else:
                print(nonExistKey())
            continue_check=continueCheck()#Then, the user is asked whether he/she wants to continue or not.
            if continue_check==False: #If the continue_check is False, the loop stops.
                break

    #The main loop will exit when the user types 'z'.
    elif my_function=='z':
        print("Thanks for using our system.")
        break

    # If the user types other letters except ('f', 'a', 's' and 'z'), the "invalid input" message will be shown to the user.
    else:
        print("Invalid letter. Please type the valid letter. Try again.")