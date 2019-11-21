# For this script you will get familiar with lists, indexes, and basic list functions

# Before anything else, I will define a list for you containing primary and secondary colors
colors = ['Red','Orange','Yellow','Green','Blue','Purple']


# Elements of a list can be called by referencing their index.
# As with most programming languages, indexes in python start with 0
# so calling the first element of the above list can be done as follows: "first = colors[0]"
# This can be unintuitive, because that means calling the third element looks like this: "third = colors[2]"
# Indexes can be regular numbers, ranges, or negative values. 
# With all of this in mind, let's get started.


# Using the index call method, print the 3 primary colors
print(colors[0], colors[2], colors[4])

# Next, try printing several colors by calling a range as an index.
# this should take the form: "print (colors[lower_index : upper_index])"
# note: ranges usually end one number before you expect to, so the range [1:4]
# will actually only print [1],[2], and [3]
print(colors[1:4])

# Then print 'Blue' by calling a negative index
print(colors[-2:-1])

# lastly, use the ".append()" function to add a 7th color to the list, and print the updated list
colors.append("Black")
print(colors)