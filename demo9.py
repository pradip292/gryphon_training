import time

class MeasureExecutionTime:
    def __call__(self, *args,**kwargs):
        print("i am inside class and methods __call__")
        start_time=time.time()
        result=self.func(*args, **kwargs)
        end_time=time.time()
        execution_time=end_time - start_time
        print("I am inside the class and method")
        
        