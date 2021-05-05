# using concatenation to see the time complexity
import timeit
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l+[i]
# using append function to see the time complexity


def test2():
    l = []
    for i in range(1000):
        l.append(i)

# using list comprehension to see the time complexity


def test3():
    l = [i for i in range(1000)]
# using list constructor to see the time complexity


def test4():
    l = list(range(1000))


# from the output we can see concatenation requires most time compared to the list constructor
t1 = Timer("test1()", "from __main__ import test1")
print("concat time", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append time", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("list comprehension time", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list time", t4.timeit(number=1000), "milliseconds")
