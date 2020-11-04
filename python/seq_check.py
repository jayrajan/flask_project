# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.



def seq_check(nums):
    seq = [1,2,3]

    for i in range(len(nums)-2):
        if nums[i]==seq[0] and nums[i+1]==seq[1] and nums[i+2]==seq[2]:
            print(True)
        else:
            continue

seq_check([1,4,6,2,3])
