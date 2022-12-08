import time
from functools import wraps
from statistics import fmean, stdev


def timeit(n: int = 10):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        exec_times = []
        for _ in range(n):
            start_time = time.time()
            result = func(*args, **kwargs)
            exec_times.append(time.time() - start_time)
        mean = fmean(exec_times)
        rel_stdev = round((stdev(exec_times) / mean) * 100,2)
        print(f"'{func.__name__}()' took on average {mean} seconds with a stdev of {rel_stdev}%. ({n} runs)")
        return result
    return wrapper
  return decorator
