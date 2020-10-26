def my_range(stop, start=0, step=1):
    while start < stop:
        yield start
        start += step


def my_reduce(func, *args):
    curr_result = args[0]
    args = args[1:]
    arg_num = len(args)
    while arg_num > 0:
        curr_result = func(curr_result, args[0])
        args = args[1:]
        arg_num -= 1
    return curr_result
