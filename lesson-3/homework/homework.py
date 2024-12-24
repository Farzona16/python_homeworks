# ### List Tasks

# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
# mylist=[1,2,'hello',3,4,'good','hello']
# print(mylist.count('hello'))

# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
# mylist=[1,2,5,3,4,6,7]
# total=sum(mylist)
# print(total)
        
# 3. **Max Element**: From a given list, determine the largest element.
# mylist=[1,2,5,3,4,6,7,10,20,40,1,25,19,30]
# mylist.sort(reverse=True)
# print(mylist[0])

# 4. **Min Element**: From a given list, determine the smallest element.
# mylist=[1,2,5,3,4,6,7,10,20,40,1,25,19,30]
# smallest=min(mylist)
# print(smallest)

# 5. **Check Element**: Given a list and an element, check if the element is present in the list.
# mylist=[1,2,5,3,4,6,7,10,20,40,1,25,19,30]
# if 7 in mylist:
#     print("yes")

# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
# mylist=[7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# if len(mylist)!=0:
#     print(mylist[0])
# else: print("empty")

# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
# mylist=[7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# if len(mylist)!=0:
#     print(mylist[-1])
# else: print("empty")


# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
# mylist=[7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# newlist=mylist[:3]
# print(newlist)

# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
# mylist=[7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# mylist.reverse()
# print(mylist)

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
# mylist=[7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# mylist.sort()
# print(mylist)

# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
# mylist=[1,5,7,2,5,3,4,6,7,10,20,40,1,25,19,30]
# unique_list=[]
# for x in mylist:
#     if x not in unique_list:
#         unique_list.append(x)
# print(unique_list)
      
# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
# mylist=["apple","banana","cherry","apricot","pineapple"]
# mylist.insert(2,"hello")
# print(mylist)

# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
# mylist=["apple","banana","cherry","apricot","pineapple"]
# print(mylist.index("banana"))

# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
# mylist=[]
# if  mylist==[]:
#     print("True")

# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
# mylist=[1,2,3,4,5,6,9,14,15,13,18,17,25,27,43]
# even_count=0
# for i in range(len(mylist)):
#     if mylist[i]%2==0:
#         even_count+=1
# print(f"{even_count} even number(s) ")

# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
# mylist=[1,2,3,4,5,6,9,14,15,13,18,17,25,27,43]
# odd_count=0
# for i in range(len(mylist)):
#     if mylist[i]%2==1:
#         odd_count+=1
# print(f"{odd_count} odd number(s)")

# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
# mylist=[1,2,3,4,5,6,9,14]
# my_2list=[15,13,18,17,25,27,43]
# my_3list=mylist+my_2list
# print(my_3list)

# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
'''# mylist=[1,2,3,0,5,6,9,14]
# sublist=[3,4,5]
# n=len(mylist)
# m=len(sublist)
# for i in range(n):
#     if mylist[i]=sublist[0] and 
        
#     else:
#         print("no")'''

# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
# mylist=[1,2,3,0,5,6,9,14]
# given_element=5
# another_element=90
# for i in range(len(mylist)):
#     if mylist[i]==given_element:
#         mylist[i]=another_element
# print(mylist)

# 20. **Find Second Largest**: From a given list, find the second largest element.
# mylist=[1,2,3,0,5,6,9,14]
# mylist.sort(reverse=True)
# print(mylist[1])

# 21. **Find Second Smallest**: From a given list, find the second smallest element.
# mylist=[1,2,3,0,5,6,9,14]
# mylist.sort()
# print(mylist[1])

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
# mylist=[1,2,3,0,5,6,9,14]
# new_list=[]
# for i in range(len(mylist)):
#     if mylist[i]%2==0:
#         new_list.append(mylist[i])
# print(new_list)

# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
# mylist=[1,2,3,0,5,6,9,14]
# new_list=[]
# for i in range(len(mylist)):
#     if mylist[i]%2==1:
#         new_list.append(mylist[i])
# print(new_list)

# 24. **List Length**: Determine the number of elements in the list.
# mylist=[1,2,3,0,5,6,9,14]
# num=len(mylist)
# print(num)

# 25. **Create a Copy**: Create a new list that is a copy of the original list.
# mylist=[1,2,3,0,5,6,9,14]
# new_list=mylist.copy()
# print(new_list)

# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
# mylist=[1,2,3,4,6,5,7,9,14]
# num=len(mylist)
# my_num=0
# a=int(num/2)
# if num%2==1:
#     my_num=(mylist[a])
# else:my_num=(mylist[a-1],mylist[a])
# print(my_num)

# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
# mylist=[1,2,3,4,6,5,7,9,14]
# sublist=mylist[3:7]
# print(max(sublist))

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
# mylist=[1,2,3,4,6,5,7,9,14]
# sublist=mylist[3:7]
# print(min(sublist))

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
# mylist=[1,2,3,4,6,5,7,9,14]
# mylist.pop(3)
# print(mylist)

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
# mylist=[1,2,3,4,5,7,9,14]
# is_sorted=all(mylist[i]<=mylist[i+1] for i in range(len(mylist)-1))
# print(is_sorted)

# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
# mylist=[1,2,3,4,5,7,9,14]
# num=4
# new_list=[]
# for i in range(len(mylist)):
#     new_list.extend([mylist[i]]*num)
# print(new_list)

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
# mylist=[1,2,3,4,5,7,9,14]
# second=[15,19,18,0]
# mylist.sort()
# second.sort()
# third=mylist+second
# third.sort()
# print(third)

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
# mylist=[1,2,3,4,5,7,9,14]
# num=7
# for i in range(len(mylist)):
#     if mylist[i]==num:
#         print(i)

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# mylist=[1,2,0,3,4,5,7,9,14]
# mylist.reverse()
# print(mylist)

# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
# number1=int(input("enter the beginning point: "))
# number2=int(input("enter the ending point: "))
# for i in range(number2-number1):
#     number1+=1
#     print(number1-1)
#     if number1==number2:
#         break

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14]
# sum=0
# for i in range(len(mylist)):
#     if mylist[i]>0:
#         sum+=mylist[i]
# print(sum)

# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14]
# sum=0
# for i in range(len(mylist)):
#     if mylist[i]<0:
#         sum+=mylist[i]
# print(sum)

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14]
# new_list=list(reversed(mylist))
# print(mylist.reverse()==new_list)


# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9]
# num=3
# result=[mylist[i:i+num] for i in range(0,len(mylist),num)]
# print(result)

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9]
# new_list=[]
# for i in mylist:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# ### Tuple Tasks

# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3)
# element=3
# num=0
# for i in range(len(mytuple)):
#     if element == mytuple[i]:
#         num+=1
# print(num)

# 2. **Max Element**: From a given tuple, determine the largest element.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# print(max(mytuple))

# 3. **Min Element**: From a given tuple, determine the smallest element.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# print(min(mytuple))

# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# element=8
# print(element in mytuple)

# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# empty=tuple()
# if mytuple!=empty:
#     print(mytuple[0])
# else:print(empty)

# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# empty=tuple()
# if mytuple!=empty:
#     print(mytuple[-1])
# else:print(empty)

# 7. **Tuple Length**: Determine the number of elements in the tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# print(len(mytuple))

# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# print(mytuple[0:3])

# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# my_2tuple=(30,40,50)
# my_3tuple=mytuple+my_2tuple
# print(my_3tuple)

# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# empty=tuple()
# if mytuple!=empty:
#     print("it is not empty")
# else:print("empty")

# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# element=7
# indecis=[]
# for i in range(len(mytuple)):
#     if element==mytuple[i]:
#         indecis.append(i)
# new_tuple=tuple(indecis)
# print(new_tuple)

# 12. **Find Second Largest**: From a given tuple, find the second largest element.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# new_list=list(mytuple)
# new_list.sort(reverse=True)
# print(new_list[1])

# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# new_list=list(mytuple)
# new_list.sort()
# print(new_list[1])

# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
# mytuple=(40,)
# print(mytuple)

# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21]
# mytuple=tuple(mylist)
# print(mytuple)

# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
# mytuple=(1,2,3,4,5,6,7)
# is_sorted=True
# for i in range(len(mytuple)-1):
#    if mytuple[i]>=mytuple[i+1]:
#       is_sorted=False
# print(is_sorted)

# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# subtuple=mytuple[7:16]
# print(max(subtuple))

# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# subtuple=mytuple[7:16]
# print(min(subtuple))

# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# element=3
# mylist=list(mytuple)
# if element in mylist:
#     mylist.remove(element)
# print(mylist)

# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# num=3
# newlist=[]
# for i in range(0,len(mytuple),num):
#     newlist.append(tuple(mytuple[i:i+num]))
# nested_tuple=tuple(newlist)
# print(nested_tuple)

# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# mytuple=(1,2,3,45,89)
# num=3
# mylist=[]
# for i in range(len(mytuple)):
#     mylist.extend([mytuple[i]]*num)
# newlist=tuple(mylist)
# print(newlist)

# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# start=int(input("enter the beginning point: "))
# end=int(input("enter the endning point: "))
# num=[start]
# for i in range(end-start):
#     start+=1
#     num.append(start)
# print(tuple(num))

# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# mylist=list(mytuple)
# newlist=tuple(reversed(mylist))
# print(newlist)

# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# mytuple=(1,2,3,2,1,4)
# mylist=list(mytuple)
# new_list=list(reversed(mylist))
# if mylist==new_list:
#     print("it is polindrome")
# else:print("it is not polindrome")

# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# mytuple=(1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21)
# mylist=list(mytuple)
# newlist=[]
# for i in range(len(mylist)):
#     if mylist[i] not in newlist:
#         newlist.append(mylist[i])
# print(tuple(newlist))

# ### Set Tasks

# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
# first_set={1,2,3,4,5,'e','r','t','h'}
# second_set={'a','s','d','f','g','h','t','e','r'}
# union_set=first_set.union(second_set)
# print(union_set)

# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
# first_set={1,2,3,4,5,'e','r','t','h'}
# second_set={'a','s','d','f','g','h','t','e','r'}
# inter_set=first_set.intersection(second_set)
# print(inter_set)

# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
# first_set={1,2,3,4,5,'e','r','t','h'}
# second_set={'a','s','d','f','g','h','t','e','r',1}
# differ_set=first_set.difference(second_set)
# print(differ_set)

# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
# first_set={1,2,3,4,5,'e','r','t','h'}
# second_set={1,2,'e',8}
# print(second_set.issubset(first_set))

# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
# first_set={1,2,3,4,5,'e','r','t','h'}
# element='l'
# print(element in first_set)

# 6. **Set Length**: Determine the number of unique elements in a set.
# first_set={1,2,3,4,5,'e','r','t','h',1,2}
# print(len(first_set))

# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
# mylist=[1,2,-4,-7,-3,0,3,4,5,7,9,14,3,4,7,9,6,3,21]
# my_set=set((mylist))
# print(my_set)

# 8. **Remove Element**: Given a set and an element, remove the element if it exists.
# first_set={1,2,3,4,5,'e','r','t','h',1,2}
# element=5
# first_set.remove(element)
# print(first_set)

# 10. **Check if Set is Empty**: Determine if a set has any elements.
# myset={}
# empty={}
# print(myset!=empty)

# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
# first_set={1,2,3,4,5,'e','r','t','h'}
# second_set={'a','s','d','f','g','h','t','e','r',1}
# sym_set=first_set.symmetric_difference(second_set)
# print(sym_set)

# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
# first_set={1,2,3,4,5,'e','r','t','h'}
# element='g'
# first_set.add(element)
# print(first_set)

# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
# first_set={1,2,3,4,5,'e','r','t','h'}
# element=first_set.pop()
# print(element)
# print(first_set)

# 14. **Find Maximum**: From a given set of numbers, find the maximum element.
# first_set={1,2,3,4,5}
# element=max(first_set)
# print(element)

# 15. **Find Minimum**: From a given set of numbers, find the minimum element.
# first_set={1,2,3,4,5}
# element=min(first_set)
# print(element)

# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
# first_set={1,2,3,4,5,6,8,9,10,13,16,28}
# newlist=[]
# my_list=list(first_set)
# for i in range(len(my_list)):
#     if my_list[i]%2==0:
#         newlist.append(my_list[i])
# newset=set(newlist)
# print(newset)

# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
# first_set={1,2,3,4,5,6,8,9,10,13,16,28}
# newlist=[]
# my_list=list(first_set)
# for i in range(len(my_list)):
#     if my_list[i]%2==1:
#         newlist.append(my_list[i])
# newset=set(newlist)
# print(newset)

# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
# start=int(input("enter the beginning point: "))
# end=int(input("enter the ending point: "))
# num=[start]
# for i in range(end-start):
#     start+=1
#     num.append(start)
# print(set(num))

# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
# first_list=[1,2,3,4,5,6,7,4,3,2]
# second_list=[3,7,8,9,4,5,6]
# third_list=first_list+second_list
# my_set=set(third_list)
# print(my_set)

# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
# set_1={1,2,3,4,5,66,9}
# set_2={7,8,10,12,13,15,1,4}
# set_3=set_1.intersection(set_2)
# empty=set()
# if set_3!=empty:
#     print("there is(are) some common elements") 
# else:print("there is(are) not any  common element")

# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
# my_list=[1,3,2,3,4,5,6,7,8,9,10,3]
# my_set=set(my_list)
# newlist=list(my_set)
# print(my_set)

# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
# my_list=[1,3,2,3,4,5,6,7,8,9,10,3]
# my_set=set(my_list)
# newlist=list(my_set)
# print(len(my_set))

# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.
# start=int(input("enter the starting point: "))
# end=int(input("enter the ending point: "))
# num=[start]
# for i in range(end-start):
#     start+=1
#     num.append(start)
# set(num)
# print(num)


# ### Dictionary Tasks

# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# my_dict={'a':1,'b':2,'c':3}
# key='d'
# value=my_dict.get(key)
# print(value)

# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
# my_dict={'a':1,'b':2,'c':3}
# key='d'
# print(key in my_dict)
    
# 3. **Count Keys**: Determine the number of keys in the dictionary.
# my_dict={'a':1,'b':2,'c':3}
# num=len(my_dict)
# print(num)

# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
# my_dict={'a':1,'b':2,'c':3}
# key=list(my_dict.keys())
# print(key)

# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
# my_dict={'a':1,'b':2,'c':3}
# values=list(my_dict.values())
# print(values)

# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
# my_dict={'a':1,'b':2,'c':3}
# my_2dict={'d':5,'e':7,'f':9}
# my_3dict={**my_2dict,**my_dict}
# print(my_3dict)

# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# my_dict={'a':1,'b':2,'c':3}
# key='a'
# my_dict.pop(key)
# print(my_dict)

# 8. **Clear Dictionary**: Create a new empty dictionary.
# my_dict={'a':1,'b':2,'c':3}
# my_dict.clear()
# print(my_dict)

# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
# my_dict={}
# empty={}
# if my_dict==empty:
#     print("it is empty")
# else: print("it is not empty")

# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# my_dict={'a':1,'b':2,'c':3}
# print(my_dict.values())

# 11. **Update Value**: Given a dictionary, update the value for a specified key.
# my_dict={'a':1,'b':2,'c':3}
# my_dict['c']=8
# print(my_dict)

# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
# my_dict={'a':1,'b':2,'c':3,'d':1}
# value_given=1
# count=sum(1 for i in my_dict.values() if i==value_given)
# print(count)

# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
'''my_dict={'a':1,'b':2,'c':3,'d':6}
newdict={}
for i in my_dict.values():
    my_dict'''

# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
''' -------------------- '''

# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# keys=['a','b','c','d']
# values=[1,2,3,4]
# my_dict={}
# for i in range(len(keys)):
#     my_dict[keys[i]]=values[i]
# print(my_dict)

# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
'''mydict={
    'ism':
}'''

# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# mydict={
#     1:'a',
#     2:'b',
#     3:{4:'e', 5:'f'},
#     6:'g'
# }
# print(mydict[3][5])

# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
''' -----------------------------------  
-----------------
-----------------------'''

# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
# my_dict={'a':1,'b':2,'c':3,'d':6, 'e':6}
# values=my_dict.values()
# print(len(set(values)))

# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
my_dict={'b':1,'d':2,'c':3,'a':6, 'e':6}
newdict=sorted(my_dict)
print(my_dict)
print(newdict)
# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
