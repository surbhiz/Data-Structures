# binary search list should be ordered list and time complexity is O(log n)

def binarysearch(a_list, item):
    first = 0
    last = len(a_list)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


list1 = [5, 7, 11, 18, 50, 72]
print(binarysearch(list1, 11))
print(binarysearch(list1, 8))

# binary search with recursive call


def binarysearch_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binarysearch_recursive(a_list[:midpoint], item)
        else:
            return binarysearch_recursive(a_list[midpoint+1:], item)


list1 = [5, 7, 11, 18, 50, 72]
print(binarysearch_recursive(list1, 11))
print(binarysearch_recursive(list1, 8))
