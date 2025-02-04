from time import perf_counter
from contextlib import redirect_stdout
from inspect import signature, getsource
from io import StringIO
from lib import handle_indent
from task4 import decorator_4


# really great documentation
def decorator_2(func):
    """
        A decorator for
            1) printing out the amount of times a function was executed and
            2) the time of execution for each execution
            3) the name of the function
            4) the type of the function
            5) the docstring of the function
            6) the signature of the function
            7) the source of the function
            8) and any output during the execution of the function
        :param func: The function to be decorated
        :return wrapper: the reference to the wrapped function
    """
    counter = 0

    @decorator_4
    def wrapper(*args, **kwargs):
        """
        The decorated function. In addition to executing the function,
        It also prints the following
            1) the amount of times a function was executed
            2) the time of execution for each execution
            3) the name of the function
            4) the type of the function
            5) the docstring of the function
            6) the signature of the function
            7) the source of the function
            8) and any output during the execution of the function
        :param args: list of positional arguments
        required by the decorated function
        :param kwargs: list of keyword arguments
        required by the decorated function
        :return: None
        """
        nonlocal counter
        counter += 1
        start_time = perf_counter()
        result = None
        with redirect_stdout(StringIO()) as output:
            result = func(*args, **kwargs)
        end_time = perf_counter()
        details_store = {
            'name': func.__name__,
            'type': type(func),
            'sign': signature(func),
            'args': 'positional {} \nkey=worded {}'.format(args, kwargs),
            'doc': func.__doc__.strip(),
            'source': getsource(func),
            'output': output.getvalue()
        }
        print("{0} call {1} executed in {2:.4f}".format(func.__name__, counter, end_time - start_time))
        for key, value in details_store.items():
            print(handle_indent('{:10} {}'.format(key.title()+":", value)))
        return result

    return wrapper
