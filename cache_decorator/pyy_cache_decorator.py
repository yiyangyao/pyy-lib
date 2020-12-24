import functools
import threading
import time


class PyyCache(object):
    """Pyy Cache"""

    _max_size = DEFAULT_MAX_SIZE = 10000
    _duration = DEFAULT_DURATION = 60

    _instance_lock, _cache = threading.Lock(), {}

    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(PyyCache, "_instance"):
            with PyyCache._instance_lock:
                if not hasattr(PyyCache, "_instance"):
                    PyyCache._instance = object.__new__(cls)
        return PyyCache._instance

    def __contains__(self, key):
        """return key in _cache keys()"""
        return key in self._cache

    def get(self, key):
        """get value and time from _cache"""
        if key not in self._cache:
            return
        entry = self._cache[key]
        if self._expired(entry):
            return
        entry['time'] = int(time.time())
        return entry['value']

    def add(self, key, value):
        """update _cache, if > _max_size, delete oldest _cache item"""
        if key not in self._cache and len(self._cache) >= self._max_size:
            self._remove_oldest()
        self._cache[key] = {
            'time': int(time.time()),
            'value': value
        }

    def set_max_size(self, max_size):
        if isinstance(max_size, int):
            if max_size < 0:
                max_size = PyyCache.DEFAULT_MAX_SIZE
        elif max_size is not None:
            raise TypeError('Expected maxsize to be an integer or None')
        self._max_size = max_size

    def set_duration(self, duration):
        if isinstance(duration, int):
            if duration < 0:
                duration = PyyCache.DEFAULT_DURATION
        elif duration is not None:
            raise TypeError('Expected maxsize to be an integer or None')
        self._duration = duration

    @property
    def size(self):
        return len(self._cache)

    def _expired(self, entry):
        timestamp = int(time.time()) - entry['time']
        return timestamp > self._duration

    def _remove_oldest(self):
        """remove oldest item visited"""
        oldest_time, oldest_key = int(time.time()), None
        for key, entry in self._cache.items():
            entry_time = entry['time']
            if entry_time < oldest_time:
                oldest_time, oldest_key = entry_time, key
        self._cache.pop(oldest_key)


def pyy_cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache = PyyCache()
        key = _cache_key(*args, **kwargs)
        value = cache.get(key)
        if value is not None:
            return value
        result = func(*args, **kwargs)
        if result is not None:
            cache.add(key, result)
        return result
    return wrapper


def _cache_key(*args, **kwargs):
    cache_key = ""
    if args is not None and len(args) != 0:
        args_list = ["({})".format(_dict_cache_key(k)) for k in sorted(args, key=str)]
        cache_key += "$".join(args_list)
    if kwargs is not None and len(kwargs) != 0:
        kwargs_list = ["({}: {})".format(k, _dict_cache_key(kwargs[k])) for k in sorted(kwargs.keys(), key=str)]
        cache_key += "$".join(kwargs_list)
    return cache_key


def _dict_cache_key(kwargs):

    def _dict_cache_key_part(kwargs, cache_key):
        if not isinstance(kwargs, dict):
            return str(kwargs)

        keys = sorted(kwargs.keys(), key=str)
        for key in keys:
            cache_key += "({}: {})".format(key, _dict_cache_key(kwargs[key]))

        return cache_key

    return _dict_cache_key_part(kwargs, "")
