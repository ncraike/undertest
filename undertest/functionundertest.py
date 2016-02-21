

class FunctionUnderTest:

    NO_RESULT_YET = '__ NO RESULT YET __'
    
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = list(args)
        self.kwargs = kwargs
        self.result = self.NO_RESULT_YET

    def add_args(self, *args, **kwargs):
        self.args.extend(args)
        self.kwargs.update(kwargs)

    def call(self):
        self.result = self.func(*self.args, **self.kwargs)
