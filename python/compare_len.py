# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    diff = abs(len(s1) - len(s2))
    return diff

a = compare_len('jay','rajan')
print(a)