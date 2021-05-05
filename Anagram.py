import timeit
from timeit import Timer

# this solution for anagram requires O(n^2) time to execute. This is because it checks each character and thus time complexity increases


def anagram_solution_1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2+1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 = pos1+1
    return still_ok


print(anagram_solution_1('abcd', 'bdac'))
print(anagram_solution_1('abcd', 'adac'))
Time1 = Timer("anagram_solution_1('abcd', 'bdac')",
              "from __main__ import anagram_solution_1")
print(Time1.timeit(number=10000), "milliseconds")
# this function is sorting and comparing the list but it too requires O(n^2)or O(nlogn)to execute


def anagram_solution_2(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos+1
        else:
            matches = False

    return matches


print(anagram_solution_2('abcd', 'bdac'))
print(anagram_solution_2('abcd', 'adac'))
Time2 = Timer("anagram_solution_2('abcd', 'bdac')",
              "from __main__ import anagram_solution_2")
print(Time2.timeit(number=10000), "milliseconds")
# this function uses O(n) time to execute which is faster than the two functions above and therefore this function is better


def anagram_solution_3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        # ord() is the function used to unicode of passed argument for eg ord('a')=97
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos]+1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j+1
        else:
            still_ok = False
    return still_ok


print(anagram_solution_3('abcd', 'bdac'))
print(anagram_solution_3('abcd', 'adac'))
Time3 = Timer("anagram_solution_3('abcd', 'bdac')",
              "from __main__ import anagram_solution_3")
print(Time3.timeit(number=10000), "milliseconds")
