PRIME = 2 ** 31 - 1


def search_lyrics(L, Q):
    """
    Input: L | an ASCII string
    Input: Q | an ASCII string where |Q| < |L|

    Return `True` if Q appears inside the lyrics L and `False` otherwise.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # Return ASCII value of substring
    def substring_value(substring, return_base=False):
        val = 0
        base = 1

        # Start from end of string and run to beginning
        for i in range(len(substring) - 1, -1, -1):
            # Increment val by char value * current_base
            val += ord(substring[i]) * base
            # Increment base by 128 each time through loop --> saves having to compute each exponent seperately
            base *= 128

        # return base value to save computing it again
        if return_base:
            return val % PRIME, base % PRIME
        else:
            return val % PRIME

    # Q substring value - goal value
    Q_value = substring_value(Q)

    # Find value of first substring in L
    # Get f_prime from prior calculations
    substring_sum, f_prime = substring_value(L[:len(Q)], return_base=True)

    current_index = len(Q)

    # Run until end of L
    while current_index < len(L):
        # If values are equal, substring found
        if substring_sum == Q_value:
            return True

        # Multiply by 128 to shift values over
        substring_sum *= 128
        # Subtract highest impact value
        substring_sum -= ord(L[current_index-len(Q)])*f_prime
        # Add new value
        substring_sum += ord(L[current_index])
        # Find substring_sum mod PRIME
        substring_sum = substring_sum % PRIME

        current_index += 1

    return False



