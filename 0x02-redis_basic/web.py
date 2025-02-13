#!/usr/bin/env python3
import redis
import requests
from functools import wraps
from typing import Callable

# Connect to Redis
r = redis.Redis()

def cache_page(method: Callable) -> Callable:
    """Decorator to cache page content and track access count."""
    @wraps(method)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        # Increment URL access count
        r.incr(count_key)

        # Check if response is cached
        cached_response = r.get(cache_key)
        if cached_response:
            return cached_response.decode("utf-8")

        # Otherwise, fetch from the web
        response = method(url)

        # Cache result with expiration of 10 seconds
        r.setex(cache_key, 10, response)

        return response

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """Fetches a web page and caches it for 10 seconds."""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk"
    
    # First call (fetches and caches)
    print("Fetching page...")
    print(get_page(test_url))

    # Second call (retrieves from cache)
    print("Fetching again (should be cached)...")
    print(get_page(test_url))

    # Display access count
    print(f"URL accessed: {redis_client.get(f'count:{test_url}').decode()} times")



