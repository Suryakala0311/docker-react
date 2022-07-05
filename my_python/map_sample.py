#Map function
def myMapFunc(n):
    return n.upper()

my_string = "Welcome to map function"
new_string = map(myMapFunc, my_string)

print(new_string)
for i in new_string:
    print(i, end="") #end->adds the string 

#Lambda function
my_list = [2,3,4,5,6]
new_list = map(lambda x : x*10, my_list)
print(new_list)
print(list(new_list))

#reduce function
import functools
list1 = [3, 5, 6, 1, 9, 2]
new_list1 = functools.reduce(lambda a, b: a if a > b else b, list1)
print(new_list1)

#filter function
def new_func(n):
    sequence = ['a', 'e', 'i', 'o', 'u']
    if n in sequence:
        return True
    else:
        return False
list2 = ['r', 't', 'e', 'i', 'z']
new_list2 = filter(new_func, list2)
print(new_list2)
for i in new_list2:
    print(i)
