#!/usr/bin/env python3
'''Redis module
'''
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    '''Represent the cache class
    '''
    def __init__(self) -> None:
        '''initializes cache
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores redis data
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
