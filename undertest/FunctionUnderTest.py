

class FunctionUnderTest:

    NO_RESULT_YET = '__ NO RESULT YET __'
    NO_RESULT_AS_EXCEPTION_RAISED = '__ NO RESULT AS EXCEPTION RAISED __'
    
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

    def perform_call_under_test(self):
        return self.func(*self.args, **self.kwargs)

    def call(self):
        try:
            self.result = self.perform_call_under_test()
        except Exception as exception_caught:
            self.exception_caught = exception_caught
            self.result = self.NO_RESULT_AS_EXCEPTION_RAISED
