from cache_decorator import pyy_cache_decorator


@pyy_cache_decorator.pyy_cache
def test_pyy_cache(ssid, attr):
    print('----------------')
    return {'1': ssid, '2': attr}


if __name__ == '__main__':
    # cache = PyyCache(_max_size=2, duration=10)
    # cache.add('k1', 1)
    # cache.add('k2', 2)
    # print(cache._cache.get('k1'))
    # time.sleep(2)
    # print(cache.get('k1'))
    # print(cache._cache.get('k1'))
    #
    # cache.add('k3', 3)
    # print(cache._cache.get('k2'))
    # print(cache._cache.get('k3'))

    # print(_cache_key("aass", {1: 'a', '3': 3, '1': 1, '2': 2}))
    # print(_cache_key(ssid="aass", attr={1: 'a', '3': 3, '1': 1, '2': 2}))
    for i in range(10):
        test_pyy_cache(ssid="aass", attr={1: 'a', '3': 3, '1': 1, '2': 2})
