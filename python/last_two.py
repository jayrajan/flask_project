# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def last_two(mystring):
    if len(mystring)<2:
        return ('Error')
    else:
        return (mystring[-2:])


print(last_two('j'))