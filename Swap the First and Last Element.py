# Python Program to Swap the First and Last Element in a List

l = [10, 14, 5, 9, 56, 12]

def swapList(sl):
    n = len(sl)
      
    # Swapping 
    temp = sl[0]
    sl[0] = sl[n - 1]
    sl[n - 1] = temp
      
    return sl

print("Swapped list: ",swapList(l))
