#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools



def replay(method: Callable):
    """Display the history of calls of a particular function"""
    r = self._redis.Redis()

    # Get function name
    method_name = method.__qualname__

    # Keys for storing inputs and outputs in Redis
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    # Retrieve stored input and output history
    inputs = r.lrange(inputs_key, 0, -1)  # Get all inputs
    outputs = r.lrange(outputs_key, 0, -1)  # Get all outputs
    num_calls = len(inputs)

    # Print the call history
    print(f"{method_name} was called {num_calls} times:")

    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        print(f"{method_name}(*{inp.decode()}) -> {out.decode()}")

def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        input_key = "{}:inputs".format(key)
        output_key = "{}:outputs".format(key)
        self._redis.rpush(input_key, str(args))
        results = method(self, *args ,**kwargs)
        self._redis.rpush(output_key, str(results))
        return results
    return wrapper



class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid1())
        self._redis.set(random_key, data)
        return random_key
    
    def get(self, key: str, fn: Optional[Callable]= None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda d: d(int))
    


