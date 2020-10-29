# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    if (n1+n2) == 10:
        return True
    else:
        return (n1+n2)

print(check_ten_sum(5,5))