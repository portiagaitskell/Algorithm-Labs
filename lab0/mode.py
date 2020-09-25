##################################################
##  Problem 1. mode
##################################################

# Given a tuple of numbers, return the mode or the mean of modes if
# there are more than one mode. The mode is a number that appears
# most often in the tuple. It does not have to be unique, since
# several different numbers may appear the same number of times.
# In those cases, you need to return the mean of the modes.

def mode(numbers):
    '''
    Input:  numbers  | Python Tuple of positive integers
    Output: modeval  | possibly fractional value of mode
    '''
    modeval = 0
    ##################
    # YOUR CODE HERE #

    # create a count dictionary
    # check for key, if there add to count, if not create new key with count 1
    count_dict = {}

    for elt in numbers:
        if elt in count_dict:
            count_dict[elt] += 1
        else:
            count_dict[elt] = 1

    # sort dictionary into list of tuples (key, count)
    # sorted in descending order based on value
    sorted_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    # Get max count
    # Find all other values with the same count
    max_count = sorted_dict[0][1]
    max_keys = [sorted_dict[0][0]]
    for k, c in sorted_dict[1:]:
        if c == max_count:
            max_keys.append(k)

    # modeval = mean of max_keys
    modeval =sum(max_keys)/len(max_keys)


    ##################
    return modeval
