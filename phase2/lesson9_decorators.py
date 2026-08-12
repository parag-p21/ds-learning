def uppercase_result(func):
    def wrapper (*args,**kwargs):
        result=func(*args,**kwargs)
        result=result.upper()
        return result
    return wrapper
@uppercase_result
def greet():
    return "hello parag"
print(greet())


import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper
@timer
def million_loop():
    for i in range(1000000):
        pass
million_loop()

def validate_marks(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and (arg < 0 or arg > 100):
                print(f"Invalid mark: {arg}. Marks must be between 0 and 100.")
                return

        return func(*args, **kwargs)

    return wrapper


@validate_marks
def show_marks(*marks):
    print("Valid marks:", marks)


print(show_marks(85, 90, 76))
print(show_marks(85, 150, 76))

import random
import functools

def retry(max_attempts):           # outer layer — takes the argument
    def decorator(func):           # middle layer — takes the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):   # inner layer — runs each time
            for attempt in range(max_attempts):
                try:
                  return func(*args, **kwargs)   # try calling the function
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            print("All attempts failed.")
        return wrapper
               # retry() returns the decorator
    return decorator

@retry(max_attempts=3)
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

result = unstable_function()
print(result)