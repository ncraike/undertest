

class FunctionUnderTest:

    NO_RESULT_YET = '__ NO RESULT YET __'
    NO_RESULT_AS_EXCEPTION_RAISED = '__ NO AS EXCEPTION RAISED __'
    
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = list(args)
        self.kwargs = kwargs
        self.result = self.NO_RESULT_YET

        self.expected_exceptions = []
        self.exception_caught = None

    def add_args(self, *args, **kwargs):
        self.args.extend(args)
        self.kwargs.update(kwargs)

    def expect_exception(self, exception):
        self.expected_exceptions.append(exception)

    def call(self):
        expected_exceptions = tuple(self.expected_exceptions)

        try:
            self.result = self.func(*self.args, **self.kwargs)
        except expected_exceptions as exception_raised:
            self.exception_caught = exception_raised
            self.result = self.NO_RESULT_AS_EXCEPTION_RAISED
