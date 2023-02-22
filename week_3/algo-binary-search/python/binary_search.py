import random

def binary_search(x, arr):
    low = 0
    high = len(arr) -1

    while low <= high:

        mid = (high+low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1
        
        else: 
            return mid
    
    return -1

search_length = 1

values = random.sample(list(range(1,search_length*100)), search_length)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

print(binary_search(537, values)) # this returns the index of 537 in values if it exists and -1 if it doesn't exist
