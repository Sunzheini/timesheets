import time


def time_measurement_decorator(some_function: callable) -> callable:
    """
    Decorator to measure time of function execution
    :param some_function: function to measure
    :return: wrapper, which measures the time of the function execution
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = some_function(*args, **kwargs)
        end = time.time()
        measurement = end - start

        # turn to seconds
        if measurement < 0.001:
            measurement *= 1000
            print(f"generated in: {measurement:.3f}ms")
        else:
            print(f"generated in: {measurement:.3f}s")

        return result
    return wrapper
