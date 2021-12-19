import time


def time_it(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {int((end-start)*1000)}ms")

    return wrapper


@time_it
def some_op(x):
    print(f"Starting op {x}")
    time.sleep(1)
    print("We are done")
    return 123


if __name__ == "__main__":
    # some_op()
    # time_it(some_op)()
    some_op(3)
