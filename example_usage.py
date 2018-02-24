import type_check as tc


def print_sum(a, b):
    """This function takes in 2 integers and prints their sum"""
    try:
        tc.type_int(a, b)
    except Exception as e:
        return 0, e
    return a + b, None


def print_sums(*args):
    """This function takes in n integers and prints their sum"""
    try:
        tc.type_int(*args)
    except Exception as e:
        return 0, e
    return reduce(lambda x, y: x + y, args), None


def run():
    for data in [(1, 2), (3, 'a')]:
        result, err = print_sum(data[0], data[1])
        print("\nrunning print_sum, on data set : {}\nResult:".format(data))
        print err if err else result

    for data in [[1, 2], [3, 'a'], [3, 2, 1, 3, 3, 4, 5], [51, 21, 42, 54]]:
        result, err = print_sums(*data)
        print("\nrunning print_sums on data set : *{}\nResult:".format(data))
        print err if err else result


run()
