def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    # we need to instantiate the returned dictionary if we want to add {key -> value} pairs
    # we cannot modify any object that is uninstantiated
    di = zipmap(keys[1:], values[1:])
    di[keys[0]] = values[0]
    return di


#-------------------------------------------------------------------------------------------


print(zipmap([1, 2, 3], [4, 5, 6]))
