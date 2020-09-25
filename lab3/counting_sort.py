def martian_sort(wordlist, order):
    """
    Input: wordlist | a list of Martian words, consisting of lowercase letters and all the same length k
    Input: order | a permutation of [0, ..., k-1]

    Return the list of words in wordlist sorted based on order, as described in the problem set

    Runs in O(kn) time.
    """
    # go through ever index in order --> go in reverse from least to most significant
    # use ord(char) - 97 to get the index of the letter in the counting array

    # Helper function used for each index in order
    def counting_word(words, index):
        # initialize arrays to hold sorted list, and counts
        sorted_words = [''] * len(words)
        counting_arr = [0] * 26

        # find the count of character (a-z) for all word[index] in words
        for elt in words:
            counting_arr[ord(elt[index]) - 97] += 1

        # maniuplate counting_arr
        count = counting_arr[0]
        for i, elt in enumerate(counting_arr):
            if i != 0:
                count += elt
                counting_arr[i] = count
            # counting_arr

        counting_arr = [0] + counting_arr[0:-1]

        # add words to sorted_words using the index given from countting_arr
        for elt in words:
            ind = counting_arr[ord(elt[index])-97]
            sorted_words[ind] = elt
            counting_arr[ord(elt[index])-97] += 1

        return sorted_words

    # reverse order - least to most significant
    order.reverse()

    # copy wordlist
    sorted_list = wordlist.copy()
    # update sorted_list after each sort
    for index in order:
        sorted_list = counting_word(sorted_list, index)

    return sorted_list


