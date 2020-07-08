if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) #splitting the elements and converting the inputs in to a list
    arr=list(set(arr)) #first converting in to a set because the the duplicate element will be removed
                       #then again converting into the list so that we can use index to fetch the output
    
    arr=sorted(arr,reverse=True) #normally sorted method sorts the list into ascending order
                                 #but reverse=True make the list sorted in to descending order
                                 #descending order because the we know the exact output is in the 1st index
    print(arr[1])