'''
CPE106L - B3
    GROUP1:
        BRIOL
        CACANANTA
        GUTIERREZ
'''

def getMean(numList):
    #if list is empty
    if len(numList) == 0:
        return 0
    else:
        #returns average/mean
        return sum(numList)/len(numList) 

def getMedian(numList):
    numList_len = len(numList)

    #sort the list without affecting the original list 
    sorted_numList = sorted(numList)

    #if list is empty
    if numList_len == 0:
        return 0
    
    #if list length is even
    elif numList_len%2 == 0:
        #getting the two median numbers
        median1 = sorted_numList[numList_len//2] 
        median2 = sorted_numList[numList_len//2 - 1] 

        #returning the averaged median numbers
        return (median1 + median2)/2
    
    #if list length is odd
    else:
        #returns the median number
        return sorted_numList[numList_len//2]

def getMode(numList):
    #if the list is empty
    if len(numList) == 0:
        return 0
    else:
        #find the maximum count of any number in the list
        max_count = max(numList.count(num) for num in numList)
        
        #create a set of numbers that have the maximum count
        mode_set = {num for num in numList if numList.count(num) == max_count}
        
        #return all unique modes
        return mode_set




scores = [21, 43, 56, 87, 23, 21]

mean = getMean(scores)
print("Mean is " + str(mean)+ "\n")

median = getMedian(scores)
print("Median is " + str(median)+ "\n")

mode = getMode(scores)
print("Mode is " + str(mode)+ "\n")
