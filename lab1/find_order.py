##################################################
##  Problem 5b. Find order
##################################################

def find_order(all_orders, order):
    # j is mid point of list
    j = int(len(all_orders) / 2)

    # Check to see if len(orders) == 0 or (== 1 and not == order)
    if len(all_orders) == 0 or (len(all_orders) == 1 and all_orders[0] != order):
        return None

    # Case 3
    if all_orders[j] == order:
        return j
    else:
        # Elements i --> j are sorted
        if all_orders[j] > all_orders[0]:
            # Case 2
            if all_orders[0] <= order < all_orders[j]:
                return find_order(all_orders[:j], order)
            # Case 1
            else:
                ind = find_order(all_orders[j+1:], order)
                if ind is not None:
                    # add extra terms to account for index in starting array, not just final array
                    return j+1+ind
                else:
                    return ind
        else:
            # check if (j, k] is sorted
            if all_orders[-1] >= all_orders[j]:
                # elements j --> k is sorted
                if all_orders[j] < order <= all_orders[-1]:
                    ind = find_order(all_orders[j + 1:], order)
                    if ind is not None:
                        # add extra terms to account for index in starting array, not just final array
                        return j + 1 + ind
                    else:
                        return ind
                else:
                    return find_order(all_orders[:j], order)
            else:
                return None


if __name__ == '__main__':
    orders = (22, 28, 30, 33, 58, 85, 94, 99, 8, 12, 17, 19, 20)
    print(orders)
    print(find_order(orders,12))

