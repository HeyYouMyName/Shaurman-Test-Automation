import decorator


class testrail:
    """
    Decorator to decorate tests for easier identification and printing out their IDs
    """

    def __init__(self, test_case_id, output=True):
        self.test_case_id = test_case_id
        self.output = output

    def __call__(self, fn):
        def wrapper(fn, fn_self, *args):
            if self.output:
                print(self.test_case_id, end=" ")

            return fn(fn_self, *args)

        return decorator.decorator(wrapper, fn)
