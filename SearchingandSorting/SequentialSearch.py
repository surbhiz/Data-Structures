# this sequential search is unordered with time complexity as O(n)
def unordered_sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found


list1 = [5, 7, 50, 11, 18, 72]
print(unordered_sequential_search(list1, 18))
print(unordered_sequential_search(list1, 8))

# this is ordered sequential search with tie complexity  if item is present and item is not present best case is O(1) orelse worst case is O(n)


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found


list1 = [5, 7, 9, 11, 18, 72]
print(ordered_sequential_search(list1, 18))
print(ordered_sequential_search(list1, 8))
