# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):

    if len(mylist)%2 == 0:
        print(sum(mylist))
    else:
        print(max(mylist))

sum_or_max([1,2,3,4])