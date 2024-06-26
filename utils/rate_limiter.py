import time
from functools import wraps

class RateLimiter:
    def __init__(self, max_calls, time_frame):
        self.max_calls = max_calls
        self.time_frame = time_frame
        self.calls = []

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            now = time.time()
            self.calls = [call for call in self.calls if call > now - self.time_frame]
            if len(self.calls) >= self.max_calls:
                raise Exception(f"Rate limit exceeded. Max {self.max_calls} calls per {self.time_frame} seconds.")
            self.calls.append(now)
            return func(*args, **kwargs)
        return wrapped